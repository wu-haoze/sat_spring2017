import os
import sys
import shutil
import subprocess
from decimal import Decimal

"""
!!! Change the directory below
"""
minisat_dir = "DIRECTORY/minisats/minisat_act_all/core/minisat"

def main():
    in_name = sys.argv[1]
    out = open(in_name.split('.')[0]+ "_" + sys.argv[2] + '.log','w')
    with open (sys.argv[3], 'a') as out_file1:        
        rnd_seed = "-rnd-seed=" + sys.argv[2]       
        subprocess.call([minisat_dir, in_name, "-rnd-init", rnd_seed], stdout=out)
        out.close()
        with open (in_name.split('.')[0]+ "_" + sys.argv[2] +'.log', 'r') as in_file:
            for line in in_file:
                if "Number of variables:" in line:
                    for i in range(int(line.split()[4])):
                        dic[i + 1] = []
                if line and line[0] == 'x':
                    line = line.split()[1:]
                    for i in range(len(dic)):
                        dic[i + 1].append(float(line[i]))
            for i in range(len(dic)):
                out_file1.write(str(i + 1) + ", " +  ", ".join(map(str, dic[i + 1])) + "\n")
    os.remove(in_name.split('.')[0]+ "_" + sys.argv[2] + '.log')

if __name__ == "__main__":
    main()
