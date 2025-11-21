# MIT License
# 
# Copyright (c) 2025 Jeff Wilkinson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
from machine import Pin, I2C, SPI
from ssd1306 import SSD1306_SPI
import time

class TeensyView_SPI(SSD1306_SPI):
    
    WIDTH, HEIGHT = 128, 32
    char_width, char_height = 8, 8

    def __init__(self, hspi, dc=Pin(4), rst=Pin(25), cs=Pin(24)):
        
        super().__init__(self.WIDTH, self.HEIGHT, hspi, dc, rst, cs)
        
    def log(self, msg, smooth_scroll=True):
        """scroll new line onto bottom of display"""
        
        n_chars_wide = self.width/self.char_width
        n_chars_high = self.height/self.char_height
        
        if len(msg) > n_chars_wide:
            msg = msg[:n_chars_wide-1] + "."
        
        if smooth_scroll:
            for ii in range(1, self.char_height+1):
                self.scroll(0, -1)
                yy = self.height - ii
                self.fill_rect(0, yy, self.width-1, self.height-1, 0)
                self.text(msg, 0, yy)
                self.show()
                time.sleep_ms(2)
        else:
            self.scroll(0, -self.char_height)
            self.fill_rect(0, self.height-self.char_height,
                           self.width-1, self.height-1, 0)
            self.text(msg, 0, self.height-self.char_height)
            self.show()
            
