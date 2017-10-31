import os
import subprocess

# import csv as csv
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz

# reader = csv.reader(open("CampusCrimesMerged.csv", "rb"), delimiter=",", skiprows=1)
# x = list(reader)
# result = numpy.array(x).astype("float")

r = np.genfromtxt("CampusCrimesMerged.csv", skip_header=1, delimiter=',')

print r[:1]

