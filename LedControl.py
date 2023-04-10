
import time
import board
import neopixel

class LedControl:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D12, 16, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

    def spin(self, color, delaytime):
        for s in range(16):
            for i in range(16):
                if i == s:
                    self.pixels[i] = color
                else:
                    self.pixels[i] = (0, 0, 0)
            self.pixels.show()
            time.sleep(delaytime)

    def flash(self, color, delaytime, repeat):
        for i in range(repeat):
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(delaytime)

            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(delaytime)

    def boot(self):
        self.spin((0, 255, 0), 0.05)
        self.spin((0, 255, 0), 0.05)
        


    def off(self):
        for i in range(16):
            self.pixels[i] = (0, 0, 0)
        self.pixels.show()

    def on(self, color, n):
        self.pixels.fill((0, 0, 0))
        self.pixels[n] = color
        self.pixels.show()

    def ons(self, color, list):
        self.pixels.fill((0, 0, 0))
        for n in list:
            self.pixels[n] = color
        self.pixels.show()

    def fetching(self):
        # self.on((255, 255, 255), 7)
        # time.sleep(0.1)
        # self.off()
        # time.sleep(0.1)
        # self.on((255, 255, 255), 7)
        # time.sleep(0.1)
        # self.off()
        for i in range(64):
            c = i * 4
            self.on((c, c, c), 7)
            time.sleep(0.01)

        for i in range(64):
            c = 255 - (i * 4)
            self.on((c, c, c), 7)
            time.sleep(0.01)
        
        self.off()

    def breath_up(self, color, speed_sec):
        div = 20 
        t = speed_sec / div
        for s in range(div):
            r = int((color[0] / div) * s)
            g = int((color[1] / div) * s)
            b = int((color[2] / div) * s)
            self.pixels.fill((r,g,b))
            self.pixels.show()
            time.sleep(t)

    def breath_down(self, color, speed_sec):
        div = 20
        t = speed_sec / div
        for s in range(div):
            r = color[0] - int((color[0] / div) * s)
            g = color[1] - int((color[1] / div) * s)
            b = color[2] - int((color[2] / div) * s)
            self.pixels.fill((r, g, b))
            self.pixels.show()
            time.sleep(t)

