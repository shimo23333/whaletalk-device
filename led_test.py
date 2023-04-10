from LedControl import LedControl



led = LedControl()
for i in range(3):
    led.spin((0,0,255), 0.04)

