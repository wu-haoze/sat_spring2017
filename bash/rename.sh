#change the filenames of all cnf files in a directory to 1.cnf, 2.cnf, 3.cnf...

var=1
for file in *.cnf
do
    mv $file $var.cnf
    ((var++))
done

