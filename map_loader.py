#!/usr/bin/python

'''
 Search demonstrations using Python code from AI:MA by Russell and Norvig

    This code loads a map from an image file and creates a discretized map based on the image.

    The MIT License (MIT)

    Copyright (c) 2015 David Conner (david.conner@cnu.edu)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
'''

import cv2
import numpy as np
from copy import deepcopy

class MapLoader:

    def __init__(self):
        self.current_image = -1
        self.image = None
        self.map   = None
        self.color = False

    def addFrame(self, src_path, file):
        sourcepath=src_path+"/"+file
        try:
            print "Add frame from "+sourcepath+" ..."
            self.image=cv2.imread(sourcepath,cv2.IMREAD_UNCHANGED)
            #print self.image
            print "done!"

        except Exception as msg:
            print msg
            return False

        return True

    def createMap(self, scale = 1.0):
        print "Create map from existing black (obstacle) and white image ..."

        self.map = np.zeros((self.image.shape[0],self.image.shape[1], 3) ,dtype=np.uint8)
        print "  Create map = ",self.map.shape

        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                self.map[i][j][0] =   0 #self.image[i][j][0]
                self.map[i][j][1] =   0 #self.image[i][j][1]
                self.map[i][j][2] =   0 #self.image[i][j][2]
                if self.image[i][j][0] > 120: # white background is OK  (cv2 is BGR ordering)
                    self.map[i][j][1] = 192  # green is safe
                else:
                    self.map[i][j][2] = 192  # red is obstacle

        if (scale != 1.0):
            self.map = cv2.resize(self.map, (0,0),fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        print "Done creating map!"

    def plotPath(self, path, scale):
        self.path = deepcopy(self.map)

        print path[0].state
        prior_point = list(path[0].state)
        prior_point[0] *= scale
        prior_point[1] *= scale
        prior_point = ( int(prior_point[0]), int(prior_point[1]) )
        for ndx, point in enumerate(path):
          if (ndx):
            scaled_point = list(point.state)
            scaled_point[0] *= scale
            scaled_point[1] *= scale
            scaled_point = (int(scaled_point[0]), int(scaled_point[1]))

            #print "plot path from",prior_point, " to ",scaled_point

            # line is x,y  while point is (j,i) row major
            cv2.line(self.path,(prior_point[1], prior_point[0]),
                               (scaled_point[1], scaled_point[0]), color=(255,255,0),thickness=1)
            prior_point = deepcopy(scaled_point)
          else:
              # Start
              self.path[prior_point[0]][prior_point[1]][0] = 255
              self.path[prior_point[0]][prior_point[1]][1] = 255

          # Start
          self.path[prior_point[0]][prior_point[1]][1] = 255
          self.path[prior_point[0]][prior_point[1]][2] = 255

