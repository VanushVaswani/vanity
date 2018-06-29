import machine
import time, math

def test_pulse(num):
    led = machine.PWM(machine.Pin(5), freq=400)
    for i in range(num):
        pulse(led, 20)
    led.deinit()

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)
