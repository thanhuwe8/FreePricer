import pytest
import json
import tempfile

from Utils.Complex import *

#* Test object initialization

def test_complex_initialization1():
    a = Complex(rPart=1.5, iPart=0.8)
    assert a.real == 1.5
    assert a.imag == 0.8
    
    b = Complex(rPart=6, iPart=2)
    assert b.real == 6
    assert b.imag == 2
    
    c = Complex(rPart=3, iPart=-4)
    assert c.real == 3
    assert c.imag == -4


def test_complex_datamodel1():
    '''
    Testing examples from Schaum's Outline of Complex Variables 2nd (2009), Solved Problems 1.1
    '''
    a = Complex(3,2) + Complex(-7,-1)
    assert a.real == -4.0
    assert a.imag == 1.0
    
    b = Complex(-7,-1) + Complex(3,2)
    assert b.real == -4.0
    assert b.imag == 1.0
    
    c = Complex(8,-6) - Complex(-7,2)
    assert c.real == 15.0
    assert c.imag == -8.0
    
    d = Complex(5,3) + (Complex(-1,2) + Complex(7,-5))
    assert d.real == 11.0
    assert d.imag == 0.0


# #* Operation
# a = 1.5
# b = 0.8
# c = a + b*1j
# print(c)
# c2 = complex(a,b)
# print(c2)
# (3-4j).conjugate()

# #* test object method
# a = Complex(rPart=5, iPart=3)
# a.cConj()

# b = Complex(rPart=3, iPart=-4)
# b.cConj()




# #* test class method
# Complex.ccConj(a)
# Complex.ccSub(a, b)
# Complex.ccProd(a, b)
# Complex.ccProdScalar(a,5)
# Complex.ccArg(a)
# Complex.cPow(a, 5)
# Complex.cExp(a)
# Complex.cLog(a)
# Complex.cSqrt(a,b)

#######################################################
