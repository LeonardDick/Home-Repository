#!/bin/bash
rm out.txt 2>/dev/null
touch out.txt
i=1
j=1
while [ $i -le 1206 ]
do
    echo "! Create images of structure formulas with atom labels (y/n)? [no]" >> out.txt
    echo "n"  >> out.txt
    echo "! Change some atom types (y/n)? [no]" >> out.txt
    echo "y"  >> out.txt
    echo "! Change atom type in which molecule (1-4)?"  >> out.txt
    echo "1"  >> out.txt
    echo "! Which atom type to change in C1206 (e.g. 'C1'):"  >> out.txt
    echo C$i  >> out.txt
    echo "! Enter new type of atom C1206  C1 :"  >> out.txt
    echo "CA"  >> out.txt
    echo "! Choice (0-80):"  >> out.txt
    echo "2"  >> out.txt
    ((i++))
done

while [ $j -le 416 ]
do
    echo "! Create images of structure formulas with atom labels (y/n)? [no]" >> out.txt
    echo "n"  >> out.txt
    echo "! Change some atom types (y/n)? [no]" >> out.txt
    echo "y"  >> out.txt
    echo "! Change atom type in which molecule (1-4)?"  >> out.txt
    echo "2"  >> out.txt
    echo "! Which atom type to change in C1206 (e.g. 'C1'):"  >> out.txt
    echo "C$j"  >> out.txt
    echo "! Enter new type of atom C1206  C1 :"  >> out.txt
    echo "CA"  >> out.txt
    echo "! Choice (0-80):"  >> out.txt
    echo "2"  >> out.txt
    ((j++))
done

k=$(($i+$j-2))
run=1
echo "! Create images of structure formulas with atom labels (y/n)? [no]" >> out.txt
echo "n"  >> out.txt
echo "! Change some atom types (y/n)? [no]" >> out.txt
echo "n"  >> out.txt
echo "! Modify some atomic charges (y/n)? [no]" >> out.txt
echo "y"  >> out.txt
echo "! Manually enter all atomic charges (y/n)? [no]" >> out.txt
echo "y"  >> out.txt

while [ $run -le $k ]
do 
    echo "! Enter new charge of  C$run : [ 0.0000]" >> out.txt
    echo "0" >> out.txt
    ((run++))
done 

