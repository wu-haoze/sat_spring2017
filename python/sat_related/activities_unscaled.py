import os
import sys
import shutil
import subprocess
from decimal import Decimal

"""
!!! Change the directory below
"""
minisat_dir = "DIRECTORY_OF_MINISAT/minisats/minisat_act/core/minisat"

def main():
    in_name = sys.argv[1]
    out = open(in_name.split('.')[0]+ "_" + sys.argv[2] + '.log','w')
    with open (sys.argv[3], 'a') as out_file1:
        rnd_seed = "-rnd-seed=" + sys.argv[2]
        subprocess.call([minisat_dir, in_name, "-rnd-init", rnd_seed], stdout=out)
        out.close()
        with open (in_name.split('.')[0]+ "_" + sys.argv[2] +'.log', 'r') as in_file:
            f = in_file.readlines()
            vals = map(float, f[-10].split())
            norm = vals
            out_file1.write(" ".join(map(str, norm)) + " " + f[-3].split()[-2] + " " + f[-8].split()[-3] + "\n")
    os.remove(in_name.split('.')[0]+ "_" + sys.argv[2] + '.log')



if __name__ == "__main__":
    main()


