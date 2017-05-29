import os
import sys
import shutil
import subprocess
from decimal import Decimal

"""
!!! Change the directory below
"""
minisat_dir = "DIRECTORY/minisats/minisat_var_rank/core/minisat"

def main():
    in_name = sys.argv[1]
    out = open(in_name.split('.')[0]+ '.log','w')
    with open (sys.argv[2], 'a') as out_file1:
        subprocess.call([minisat_dir, in_name], stdout=out)
        out.close()
        with open (in_name.split('.')[0]+ '.log', 'r') as in_file:
            out_file1.write(in_name + ", ")
            for line in in_file:
                if "conflicts             :" in line:
                    out_file1.write(line.split()[2] + ", ")
                if "CPU time" in line:
                    out_file1.write(line.split()[3] + "\n")

    os.remove(in_name.split('.')[0]+ '.log')

if __name__ == "__main__":
    main()


