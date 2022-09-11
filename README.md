# pid_controller
A PID (Proportional Integral Derivative) controller written in python.

## Resources

* georgegillard.com/documents/2-introduction-to-pid-controllers

## Run - with arbitrary (kP, kI, kD)


```
$ python pid.py 
input = 13, output = -4.35, target = 10, actual = 8.65
input = 8.65, output = 2.4074999999999998, target = 10, actual = 11.057500000000001
input = 11.057500000000001, output = -2.1858750000000016, target = 10, actual = 8.871625
input = 8.871625, output = 1.5472687500000002, target = 10, actual = 10.41889375
input = 10.41889375, output = -0.33851250000000005, target = 10, actual = 10.08038125
input = 10.08038125, output = 0.0, target = 10, actual = 10.08038125

Dump state
kP = 1, kI = 0.15, kD = 0.3, target = 10, output = 0.0, prev_error = 0, prev_integral = 0, last_updated_s = 1662927536.9509828
```

## Tune (kP, kI, kD) dynamically
```
>>> import pid
>>> p = pid.PIDController(1, 0.15, 0.3, 10)
>>> p
kP = 1, kI = 0.15, kD = 0.3, target = 10, output = 0, prev_error = 0, prev_integral = 0, last_updated_s = 1662927637.899916
>>> p.tune(0.85, 0.20, 0.6)
>>> p
kP = 0.85, kI = 0.2, kD = 0.6, target = 10, output = 0, prev_error = 0, prev_integral = 0, last_updated_s = 1662927704.4295008
>>> p.update(13)
-4.949999999999999
>>> p
kP = 0.85, kI = 0.2, kD = 0.6, target = 10, output = -4.949999999999999, prev_error = -3, prev_integral = -0.6000000000000001, last_updated_s = 1662927926.18669
>>> p.clear()
>>> p
kP = 0.85, kI = 0.2, kD = 0.6, target = 10, output = 0, prev_error = 0, prev_integral = 0, last_updated_s = 1662927960.496434
```

