import tkinter
import tkinter as tk
from tkinter import ttk

from abc import abstractmethod
from typing import List


#? Used for MVC pattern
class View(tk.Frame):
    @abstractmethod
    def create_view():
        raise NotImplementedError