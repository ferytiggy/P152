# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:11:05 2023

@author: Aidan
"""

import matplotlib.pyplot as ptl

data = [[0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,10,10,10,10,10,10,10,10,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,10,10,10,10,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]]

ptl.imshow(data, cmap="hot")

ptl.show()