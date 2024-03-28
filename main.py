from datetime import datetime
import time


# Part 1
def clock(n):
  """ Test """
  for i in range(n):
    print(datetime.now().strftime("%H:%M:%S"), end="\r")
    time.sleep(1)


# Part 2
def lcm(a, b):
  """ Test """
  val = (a, b)
  while a != b:
    if a > b:
      b += val[1]
    else:
      a += val[0]
  return a


# Part 3
def gcf(a, b):
  """ Test """
  while b != 0:
    r = a % b
    a = b
    b = r
  return a 

