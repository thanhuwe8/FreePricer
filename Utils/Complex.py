

class Complex:
    
    def __init__(self, rPart, iPart) -> None:
        self.real = rPart
        self.imag = iPart
    
    #? Object Utils
    def __repr__(self):
        return f'Complex Number: real={self.real}, imag={self.imag};'

    #? Object method
    def cReal(self):
        return(self.real)
    
    def cImag(self):
        return(self.imag)
    
    def cAdd(self, y):
        self.real += y.real
        self.imag += y.imag
    
    def cSub(self, y):
        self.real -= y.real
        self.imag -= y.imag
    
    def cProd(self, y):
        self.real = (self.real*y.real) - (self.imag*y.imag)
        self.imag = (self.real*y.imag) + (self.imag*y.real)
    
    def cProdScalar(self, a):
        self.real = a*self.real
        self.imag = a*self.imag
    
    def cConj(self):
        self.real = self.real
        self.imag = -1*self.imag
        
    def cDiv(self, y):
        yc = Complex.cConj(self)
        self.real = (self.real * yc.real - self.imag * yc.imag) / (y.real * y.real + y.imag * y.imag)
        self.imag = (self.real * yc.imag + self.imag * yc.real) / (y.real * y.real + y.imag * y.imag)
    
    
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



###############################################################################

a = Complex(5,2)
x = Complex.ccConj(a)
a.cConj()
Complex.ccConj(a)
a