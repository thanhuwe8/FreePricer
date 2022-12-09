from abc import abstractmethod

class BaseModel():
    @abstractmethod
    def Calc(self):
        raise NotImplementedError
