#!/usr/bin/env python3

from copy import copy
import time

from typing import AnyStr

class PIDController:

    class PIDState:

        def __init__(self, output: float = 0, prev_error: float = 0, last_updated_ns: int = time.monotonic()) -> None:
            self._output = output
            self._prev_error = prev_error
            self._last_updated_ns = last_updated_ns

        def dump(self) -> AnyStr:
            return f"output = {self._output}, prev_error = {self._prev_error}, last_updated_ns = {self._last_updated_ns}"

        def __str__(self) -> AnyStr:
            return self.dump()

    def __init__(self, kP : float, kI: float, kD: float, target: float) -> None:
        self._kP = kP
        self._kI = kI
        self._kD = kD
        self._target = target
        self._state = PIDController.PIDState()

    def dump(self) -> AnyStr:
        return f"kP = {self._kP}, kI = {self._kI}, kD = {self._kD}, target = {self._target}, {self._state.dump()}"

    def update(self, current: float) -> None:
        pass

    def get(self) -> PIDState:
        return copy(self._state)

    def __str__(self) -> AnyStr:
        return self.dump()

if __name__ == '__main__':
    pid = PIDController(1.3, 3, 4, 1000)
    print(pid)
    print(pid.get())