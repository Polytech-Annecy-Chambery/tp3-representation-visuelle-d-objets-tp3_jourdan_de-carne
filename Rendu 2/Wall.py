# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Section import Section

class Wall:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
            
        # Objects list
        self.objects = []

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color'],
                                      'position': self.parameters['position']})
        self.objects.append(self.parentSection) 
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self                 

    # Finds the section where the object x can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            print(item[1].canCreateOpening(x))
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None
        
    
    # Adds an object    
    def add(self, x):    
        # A compléter en remplaçant pass par votre code
        item = self.findSection(x)
        if item != None:
            self.objects.pop(item[0])
            self.objects.extend(item[1].createNewSections(x, self.parameters['position']))
        return self
                    
    # Draws the faces
    def draw(self):
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        #gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        for i in range(len(self.objects)):
            #Section.setParameter(self.objects[i], 'edges', True)
            Section.draw(self.objects[i])
        gl.glPopMatrix()
  