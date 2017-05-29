import sys
import numpy as np


X = []
with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        X.append(map(float, line.split(" ")))
means = np.mean(X, axis=0)
means = means.tolist()

with open(sys.argv[2], 'a') as out_file:
    out_file.write( sys.argv[1] + " " + " ".join(map(str, means)) + "\n")
