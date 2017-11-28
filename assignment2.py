import numpy
import urllib
import scipy.optimize
import random
import sklearn.metrics
from collections import Counter

def parseData(fname):
  for l in urllib.urlopen(fname):
    yield eval(l)

print "Reading data..."
data = list(parseData("beer_50000.json"))
print "done"