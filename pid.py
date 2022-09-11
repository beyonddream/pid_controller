#!/usr/bin/env python3

from copy import copy
import time
import math

class PIDController:

    class PIDState:

        def __init__(self, prev_error: float = 0, prev_integral: float = 0, last_updated_s: float = time.time()) -> None:
            self._prev_error = prev_error
            self._prev_integral = prev_integral
            self._last_updated_s = last_updated_s
            self._output = 0
            
        def dump(self) -> str:
            return f"output = {self._output}, prev_error = {self._prev_error}, prev_integral = {self._prev_integral}, last_updated_s = {self._last_updated_s}"

        def clear(self) -> None:
            self._output = 0
            self._prev_error = 0
            self._prev_integral = 0
            self._last_updated_s = time.time()

        def __str__(self) -> str:
            return self.dump()

        def __repr__(self) -> str:
            return self.__str__()

    def __init__(self, kP : float, kI: float, kD: float, target: float) -> None:
        self._kP = kP
        self._kI = kI
        self._kD = kD
        self._target = target
        self._state = PIDController.PIDState()

    def dump(self) -> str:
        return f"kP = {self._kP}, kI = {self._kI}, kD = {self._kD}, target = {self._target}, {self._state}"

    def update(self, current: float, dt: float = 0) -> float:
        state = self._state

        now_ns = time.time()
        # not used, use the value passed from client.
        _dt = now_ns - state._last_updated_s

        if not math.isclose(self._target, current, abs_tol=0.5):
            error = self._target - current
        else:
            error = 0

        porportional = self._kP * error

        if error == 0:
            integral = 0
        else:
            integral = state._prev_integral + self._kI * (error * (1 if dt == 0 else dt))

        derivative = self._kD * ((error - state._prev_error) / (1 if dt == 0 else dt))

        output = porportional + integral + derivative

        state._prev_error = error
        state._prev_integral = integral
        state._last_updated_s = time.time()
        state._output = output
        
        return output

    def get(self) -> PIDState:
        return copy(self._state)

    def clear(self) -> None:
        self._state.clear()

    def tune(self, kP : float, kI: float, kD: float) -> None:
        self.clear()
        self._kP = kP
        self._kI = kI
        self._kD = kD

    def __str__(self) -> str:
        return self.dump()

    def __repr__(self) -> str:
        return self.__str__()

if __name__ == '__main__':
    target = 10
    p = PIDController(1, 0.15, 0.3, target)
    input = 13
    output = p.update(input)
    print(f"input = {input}, output = {output}, target = {target}, actual = {input + output}")
    input = input + output
    output = p.update(input)
    print(f"input = {input}, output = {output}, target = {target}, actual = {input + output}")
    input = input + output
    output = p.update(input)
    print(f"input = {input}, output = {output}, target = {target}, actual = {input + output}")
    input = input + output
    output = p.update(input)
    print(f"input = {input}, output = {output}, target = {target}, actual = {input + output}")
    input = input + output
    output = p.update(input)
    print(f"input = {input}, output = {output}, target = {target}, actual = {input + output}")
    input = input + output
    output = p.update(input)
    print(f"input = {input}, output = {output}, target = {target}, actual = {input + output}")

    print(f"\nDump state\n{p}")