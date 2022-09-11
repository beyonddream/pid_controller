#!/usr/bin/env python3

from copy import copy
import time

from typing import AnyStr

class PIDController:

    class PIDState:

        def __init__(self, prev_error: float = 0, prev_integral: float = 0, last_updated_ns: int = time.monotonic()) -> None:
            self._prev_error = prev_error
            self._prev_integral = prev_integral
            self._last_updated_ns = last_updated_ns
            self._output = 0
            
        def dump(self) -> AnyStr:
            return f"output = {self._output}, prev_error = {self._prev_error}, prev_integral = {self._prev_integral}, last_updated_ns = {self._last_updated_ns}"

        def __str__(self) -> AnyStr:
            return self.dump()

    def __init__(self, kP : float, kI: float, kD: float, target: float) -> None:
        self._kP = kP
        self._kI = kI
        self._kD = kD
        self._target = target
        self._state = PIDController.PIDState()

    def dump(self) -> AnyStr:
        return f"kP = {self._kP}, kI = {self._kI}, kD = {self._kD}, target = {self._target}, {self._state}"

    def update(self, current: float) -> float:
        state = self._state

        now_ns = time.monotonic_ns()
        dt = now_ns - state._last_updated_ns

        error = self._target - current

        porportional = self._kP * error
        integral = state._prev_integral + self._kI * (error * dt)
        derivative = self._kD * (error - state._prev_error) / dt

        output = porportional + integral + derivative

        state._prev_error = error
        state._prev_integral = integral
        state._last_updated_ns = now_ns
        state._output = output
        
        return output

    def get(self) -> PIDState:
        return copy(self._state)

    def __str__(self) -> AnyStr:
        return self.dump()

if __name__ == '__main__':
    pid = PIDController(1.3, 3, 4, 1000)
    print(pid)
    print(pid.get())