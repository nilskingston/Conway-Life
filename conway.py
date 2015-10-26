"""
conway.py
Author: Nils Kingston   
Credit: Roger
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

c1 = RectangleAsset (10,10, thinline, black)
Sprite(c1, (0,0))
Sprite(c1, (12,0))




myapp = App()
myapp.run()