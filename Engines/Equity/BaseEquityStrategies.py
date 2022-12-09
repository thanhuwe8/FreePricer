from Models.Analytical.BlackScholes import *

from abc import abstractmethod
from typing import List


class EquityBaseStrategy:
    
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def calcualte(self):
        raise NotImplementedError
    
    @abstractmethod
    def payoff(self):
        raise NotImplementedError
    
    @abstractmethod
    def greeks(self):
        raise NotImplementedError



class CallSpread(EquityBaseStrategy):
    def __init__(self, K1, K2, Vol1, Vol2, r, q, T) -> None:
        super().__init__()


class PutSpread(EquityBaseStrategy):
    def __init__(self) -> None:
        super().__init__()


class ButterflySpread(EquityBaseStrategy):
    def __init__(self) -> None:
        super().__init__()


class Straddle(EquityBaseStrategy):
    def __init__(self) -> None:
        super().__init__()


class Strangle(EquityBaseStrategy):
    def __init__(self) -> None:
        super().__init__()


class BoxSpread(EquityBaseStrategy):
    def __init__(self) -> None:
        super().__init__()


