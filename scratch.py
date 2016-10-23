import numpy
import scipy
import sympy

class Mass:
    def __init__(self,m,x,y,z,xdot,ydot,zdot):
        self.m = m
        self.x = x
        self.y = y
        self.z = z
        self.xdot = xdot
        self.ydot = ydot
        self.zdot = zdot

        self.xsymbol = sympy.symbols("x"+str(id(self)))
        self.ysymbol = sympy.symbols("y"+str(id(self)))
        self.zsymbol = sympy.symbols("z"+str(id(self)))
        
        self.xdotsymbol = sympy.symbols("xdot"+str(id(self)))
        self.ydotsymbol = sympy.symbols("ydot"+str(id(self)))
        self.zdotsymbol = sympy.symbols("zdot"+str(id(self)))


class Spring:
    def __init__(self,firstmass,othermass):
        self.firstmass = firstmass
        self.othermass = othermass

M1 = Mass(1,1,1,1,0,0,0)
M2 = Mass(2,2,2,2,0,0,0)
S = Spring(M1,M2)
