from importlib import resources
import io
import random

class Operators:
    def __init__(self, name, firstnumber, lastnumber):
        self.name = name
        self.firstnum = firstnumber
        self.lastnumber = lastnumber
    
    def addition(self):
        return  self.firstnumber + self.lastnumber
    
    def subtraction(self):
        return self.firstnumber - self.lastnumber

    def multiplication(self):
        return self.firstnumber * self.lastnumber

    def success(self):
        return self.name