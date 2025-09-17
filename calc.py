#A simple calculator
class Calculator:
  #empty constructor
  def __init__(self):
    pass
  #add method - given two numbers, return the addition
  def add(self, x1, x2):
    return x1 + x2
  #multiply method - given two numbers, return the 
  #multiplication of the two
  def multiply(self, x1, x2):
    return x1 * x2
  #subtract method - given two numbers, return the value
  #of first value minus the second
  def subtract(self, x1, x2):
    return x1 - x2
  #divide method - given two numbers, return the value
  #of first value divided by the second
  def divide(self, x1, x2):
    if x2 != 0:
      return x1/x2
    
  def koren(self, x1):
    return x1**0.5
  
  def modul(self, x1):
    if x1<0: 
      return x1*-1 
    else:
      return x1
    
  def stepen(self, x1, x2):
    return x1**x2