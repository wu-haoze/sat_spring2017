import os
import sys
import shutil
import subprocess
from decimal import Decimal

"""
!!! Change the directory below
"""
minisat_dir = "DIRECTORY/minisats/minisat_pick_backbone/core/minisat"

def main():
    dic = {}
    in_name = sys.argv[1]
    out = open(in_name.split('.')[0]+ "_" + sys.argv[2] + "_" + sys.argv[3] + '.log','w')
    with open (sys.argv[4], 'a') as out_file1:
        rnd_seed = "-rnd-seed=" + sys.argv[2]
        bb_rat = "-bb-rat=" + str(float(sys.argv[3])/100.0)
        subprocess.call([minisat_dir, in_name, "-rnd-init", rnd_seed, bb_rat], stdout=out)
        out.close()
        with open (in_name.split('.')[0]+ "_" + sys.argv[2] + "_" + sys.argv[3] +'.log', 'r') as in_file:
            for line in in_file:
                if "conflicts             :" in line:
                    out_file1.write(sys.argv[3] + " " + line.split()[2] + "\n")
    os.remove(in_name.split('.')[0]+ "_" + sys.argv[2] + "_" + sys.argv[3] + '.log')

if __name__ == "__main__":
    main()
