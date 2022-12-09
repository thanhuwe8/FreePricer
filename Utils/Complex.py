import numpy as np


class Complex:
    
    def __init__(self, rPart, iPart) -> None:
        self.real = rPart
        self.imag = iPart
    
    #? Overloading object operators/data model for object
    def __repr__(self):
        return f'Complex Number: real={self.real}, imag={self.imag};'

    def __eq__(self, obj):
        return isinstance(obj, Complex) and self.real == obj.real and self.imag == obj.imag
    
    def __ne__(self, obj):
        return not self == obj

    #? Overloading mathematical operators/data model for mathematics
    def __add__(self, obj):
        if isinstance(obj, Complex):
            output = self.ccAdd(self,obj)
            return(output)
        else:
            print("Cannot plus non-complex number")

        
    def __sub__(self, obj):
        if isinstance(obj, Complex):
            output = self.ccSub(self, obj)
            return(output)
        else:
            print("Cannot minus non-complex number")
    
    def __mul__(self, obj):
        if isinstance(obj, Complex):
            output = self.ccProd(self, obj)
            return(output)
        elif isinstance(obj, int) or isinstance(float):
            output = self.ccProdScalar(self,obj)
            return(output)

    def __truediv__(self, obj):
        if isinstance(obj, Complex):
            output = self.ccDiv(self, obj)
            return(output)
        else:
            print("Cannot divide non-complex number")
    
    def __pow__(self, obj):
        if isinstance(obj, int) or isinstance(obj, float):
            output = self.ccPow(self, obj)
            return(output)
        else:
            print("Cannot perform power of non-int/non-float number")
            
        
    #? Object method
    def cReal(self):
        return(self.real)
    
    def cImag(self):
        return(self.imag)
    
    def cAdd(self, cNum):
        self.real += cNum.real
        self.imag += cNum.imag
    
    def cSub(self, cNum):
        self.real -= cNum.real
        self.imag -= cNum.imag
    
    def cProd(self, cNum):
        self.real = (self.real*cNum.real) - (self.imag*cNum.imag)
        self.imag = (self.real*cNum.imag) + (self.imag*cNum.real)
    
    def cProdScalar(self, Num):
        self.real = Num*self.real
        self.imag = Num*self.imag
    
    def cConj(self):
        self.real = self.real
        self.imag = -1*self.imag

    def cDiv(self, cNum):
        yc = Complex.cConj(self)
        self.real = (self.real * yc.real - self.imag * yc.imag) / (cNum.real * cNum.real + cNum.imag * cNum.imag)
        self.imag = (self.real * yc.imag + self.imag * yc.real) / (cNum.real * cNum.real + cNum.imag * cNum.imag)


    def cArg(self):
        pi = np.pi
        x = self.real
        y = self.imag
        
        if x > 0 and y > 0:
            theta = np.arctan(y/x)
        elif x < 0 and y > 0:
            theta = pi + np.arctan(y/x)
        elif x < 0 and y < 0:
            theta = -1*pi + np.arctan(y/x)
        elif x > 0 and y < 0:
            theta = np.arctan(y/x)
        elif x > 0 and y == 0:
            theta = 0
        elif x == 0 and y > 0:
            theta = pi/2
        elif x < 0 and y == 0:
            theta = pi
        elif x == 0 and y < 0:
            theta = -pi/2
        elif x == 0 and y == 0:
            print("Erorr, argument of input z is not defined")
            theta = "Error"
        return(theta)


    def cPow(self, Num):
        x = self.real
        y = self.imag
        r = np.sqrt(x*x + y*y)
        if y == 0:
            self = Complex(rPart=x**Num,iPart=0)
        elif x == 0:
            self = Complex(rPart=-1*y**Num,iPart=0)
        else:
            theta = self.cArg(self)
            self.real = r**Num*np.cos(theta*Num)
            self.imag = r**Num*np.sin(theta*Num)
    
    def cExp(self):
        self.real = np.exp(self.real)*np.cos(self.imag)
        self.imag = np.exp(self.real)*np.sin(self.imag)
    
    def cLog(self):
        x = self.real
        y = self.imag
        T = self.cArg()
        
        absx = np.sqrt(x*x+y*y)
        self.real = np.log(absx)
        self.imag = T
    
    def cSqrt(self, cNum):
        r = np.sqrt(self.real*self.real + self.imag*self.imag)
        y = self.cArg()
        
        self.real = r**(cNum.real)*np.exp(-1*cNum.imag*y)*np.cos(cNum.real*y+cNum.imag*np.log(r))
        self.imag = r**(cNum.real)*np.exp(-1*cNum.imag*y)*np.sin(cNum.real*y+cNum.imag*np.log(r))
    
    #? Class method
    @classmethod
    def ccConj(cls, x):
        result = Complex(rPart=x.real, iPart=-1*x.imag)
        return(result)
    
    @classmethod
    def ccAdd(cls, x, y):
        return(Complex(rPart=x.real+y.real, iPart=x.imag+y.imag))
    
    @classmethod
    def ccSub(cls, x, y):
        return(Complex(rPart=x.real-y.real, iPart=x.imag-y.imag))

    @classmethod
    def ccProd(cls, x, y):
        real_part = (x.real*y.real) - (y.imag*y.imag)
        imag_part = (x.real*y.imag) + (y.imag*y.real)
        return(Complex(rPart=real_part,iPart=imag_part))
    
    @classmethod
    def ccProdScalar(cls,x,a):
        return(Complex(a*x.real, a*x.imag))

    @classmethod
    def ccArg(cls,cNum):
        pi = np.pi
        x = cNum.real
        y = cNum.imag
        
        if x > 0 and y > 0:
            theta = np.arctan(y/x)
        elif x < 0 and y > 0:
            theta = pi + np.arctan(y/x)
        elif x < 0 and y < 0:
            theta = -1*pi + np.arctan(y/x)
        elif x > 0 and y < 0:
            theta = np.arctan(y/x)
        elif x > 0 and y == 0:
            theta = 0
        elif x == 0 and y > 0:
            theta = pi/2
        elif x < 0 and y == 0:
            theta = pi
        elif x == 0 and y < 0:
            theta = -pi/2
        elif x == 0 and y == 0:
            print("Erorr, argument of input z is not defined")
            theta = "Error"
        return(theta)


    @classmethod
    def ccPow(cls, cNum, Num):
        x = cNum.real
        y = cNum.imag
        
        result = Complex(1,0)
        
        r = np.sqrt(x*x + y*y)
        if y == 0:
            result = Complex(rPart=x**Num,iPart=0)
        elif x == 0:
            result = Complex(rPart=-1*y**Num,iPart=0)
        else:
            theta = result.ccArg(cNum)
            result.real = r**Num*np.cos(theta*Num)
            result.imag = r**Num*np.sin(theta*Num)
        return(result)


    @classmethod
    def ccExp(cls, cNum):
        result = Complex(1,0)
        result.real = np.exp(cNum.real)*np.cos(cNum.imag)
        result.imag = np.exp(cNum.real)*np.sin(cNum.imag)
        return(result)


    @classmethod
    def ccLog(cls, cNum):
        result = Complex(1,0)
        x = cNum.real
        y = cNum.imag
        T = cNum.cArg()
        absx = np.sqrt(x*x+y*y)
        result.real = np.log(absx)
        result.imag = T
        return(result)


    @classmethod
    def ccSqrt(cls, cNum1, cNum2):
        result = Complex(1,0)
        r = np.sqrt(cNum1.real*cNum1.real + cNum1.imag*cNum1.imag)
        y = cNum1.cArg()
        result.real = r**(cNum2.real)*np.exp(-1*cNum2.imag*y)*np.cos(cNum2.real*y+cNum2.imag*np.log(r))
        result.imag = r**(cNum2.real)*np.exp(-1*cNum2.imag*y)*np.sin(cNum2.real*y+cNum2.imag*np.log(r))
        return(result)

###############################################################################
