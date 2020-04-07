class MyCalculator:
  def __init__(self):
    self.current = 0
  
  def add(self, amount):
        sum = self.current += amount
        return sum

  def difference(self, val1, val2):
    difference = float(val1) - float(val2)
    return difference

  def multiply(self, val1, val2):
    product = float(val1) * float(val2)
    return product

  def divide(self, val1, val2):
      quotient = float(val1) / float(val2)
      print(quotient)
  
  def getCurrent(self):
    return self.current



if __name__ == '__main__':
  calc = MyCalculator()
  calc.add(5, 10)
  calc.subtract(9, 4)
  calc.multiply(70, 5)
  calc.divide(40, 2)
  print('Done')