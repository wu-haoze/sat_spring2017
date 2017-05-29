import scipy.stats
import numpy
import sys
import re

with open(sys.argv[1], 'r') as in_file:
    content = in_file.read().splitlines()
out_file = open(sys.argv[2], 'w')
out_file.write("filename skewness kurtosis\n")
for i in range(len(content)):
    x = re.split(', | ', content[i])
    filename = x[0]
    data = map(float, x[1:])
    sa = scipy.stats.skew(data)
    ka = scipy.stats.kurtosis(data)
    out_file.write(filename + " " + str(sa) + " " + str(ka) + "\n")

out_file.close()
