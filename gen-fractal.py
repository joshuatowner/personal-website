import math
import time
import numpy as np
import matplotlib.pyplot as plt
import csv

# based on https://stackoverflow.com/questions/8370637/complex-numbers-usage-in-python

MAX_ITER = 100

def f(z):
  return z**2 -0.512511498387847167 + 0.521295573094847167j

def get_point(x, y):
  z = x + y*1j
  color = math.exp(-abs(z))

  count = 0
  while count < MAX_ITER and abs(z) < 30:
    z = f(z)
    color += math.exp(-abs(z))
    count += 1

  return color

def write_data():
  X_DIMEN = 2000
  Y_DIMEN = 1500
  X_MIN = -0.5
  X_MAX = 1.5
  Y_MIN = -0.5
  Y_MAX = 1

  pixels = [0] * Y_DIMEN
  for i in range(Y_DIMEN):
      pixels[i] = [0] * X_DIMEN
    
  total = X_DIMEN * Y_DIMEN
  done = 0
  for x in range(0, X_DIMEN):
    for y in range(0, Y_DIMEN):
      re = (1 / X_DIMEN) * x * (X_MAX - X_MIN) + X_MIN
      im = (1 / Y_DIMEN) * y * (Y_MAX - Y_MIN) + Y_MIN
      pixels[y][x] = get_point(re, im)
      done += 1
      print("finished {}/{}".format(done, total))

  with open("pixels.csv","w") as my_csv:
      csvWriter = csv.writer(my_csv,delimiter=',')
      csvWriter.writerows(pixels)

def plot_data():
  pixels = np.loadtxt(open("pixels.csv", "rb"), delimiter=",")
  plt.imshow(np.array(pixels).astype("float"))
  plt.show()

#write_data()
plot_data()