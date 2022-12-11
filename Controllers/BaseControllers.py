from abc import ABC, abstractmethod
from Views.BaseViews import *


class Controller(ABC):
    @abstractmethod
    def bind(view:View):
        raise NotImplementedError