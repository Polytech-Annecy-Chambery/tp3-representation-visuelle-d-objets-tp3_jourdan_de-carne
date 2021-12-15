# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
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
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False            
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [
                [0, 0, 0 ], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                [0,self.parameters['thickness'],0],
                [0,self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],0],
                # Définir ici les sommets
                ]
        self.faces = [
                [0, 3, 2, 1],
                [1, 5, 6, 2],
                [4, 5, 6, 7],
                [0, 4, 7, 3],
                [0, 4, 5, 1],
                [3, 2, 6, 7],
                # définir ici les faces
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        if x.parameters['thickness'] != self.parameters['thickness']:
            return False
        elif x.parameters['position'][0] + x.parameters['width'] - self.parameters['position'][0] > self.parameters['width']:
            return False
        elif x.parameters['position'][2] + x.parameters['height'] - self.parameters['position'][2] > self.parameters['height']:
            return False
        return True
        
    # Creates the new sections for the object x
    def createNewSections(self, x, y):
        # A compléter en remplaçant pass par votre code
        objects = []
        for i in range(4):
            if i == 0:
                section = Section({'position': [self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2]], 'width':x.parameters['position'][0] - (self.parameters['position'][0] - y[0]), 'height':self.parameters['height'], 'thickness':self.parameters['thickness']})
            elif i == 1:
                section = Section({'position': [x.parameters['position'][0] - (self.parameters['position'][0] - y[0]) + self.parameters['position'][0], self.parameters['position'][1], x.parameters['position'][2] + x.parameters['height'] + self.parameters['position'][2]], 'width':x.parameters['width'], 'height':self.parameters['height'] - x.parameters['position'][2] - x.parameters['height'] , 'thickness':self.parameters['thickness']})
            elif i == 2:
                section = Section({'position': [x.parameters['position'][0] - (self.parameters['position'][0] - y[0]) + self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2]], 'width':x.parameters['width'], 'height':x.parameters['position'][2] , 'thickness':self.parameters['thickness']})
            elif i == 3:
                section = Section({'position': [(x.parameters['position'][0] - (self.parameters['position'][0] - y[0])) + x.parameters['width'] + self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2]], 'width':self.parameters['width'] - (x.parameters['position'][0] - (self.parameters['position'][0] - y[0])) - x.parameters['width'], 'height':self.parameters['height'], 'thickness':self.parameters['thickness']})
            
            if section.parameters['width'] != 0 and section.parameters['height'] != 0:
                objects.append(section)
        return objects
            
                   
        
        
        
    # Draws the edges
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les arêtes : GL_LINE
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.25, 0.25, 0.25]) # Couleur gris moyen
        for i in range(len(self.faces)):
            for j in range(len(self.faces[0])):
                gl.glVertex3fv(self.vertices[self.faces[i][j]])
        gl.glEnd()
        
        
                    
    # Draws the faces
    def draw(self):
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        if self.parameters['edges'] == True:
            self.drawEdges()
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        for i in range(len(self.faces)):
            for j in range(len(self.faces[0])):
                gl.glVertex3fv(self.vertices[self.faces[i][j]])
        gl.glEnd()
        gl.glPopMatrix()