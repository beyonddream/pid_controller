#!/usr/bin/env python3

from typing import AnyStr

class PIDController:

    class PIDState:

        def __init__(self, kP : int, kI: int, kD: int) -> None:
            self.kP = kP
            self.kI = kI
            self.kD = kD

        def dump(self) -> AnyStr:
            return f"kP = {self.kP}, kI = {self.kI}, kD = {self.kD}"

    def __init__(self, kP : float, kI: float, kD: float) -> None:
        self.state = PIDController.PIDState(kP, kI, kD)


    def dump(self) -> AnyStr:
        return self.state.dump()


if __name__ == '__main__':
    print(PIDController(1.3, 3, 4).dump())