#!/bin/bash
rm traj_sys.tcl 2>/dev/null
touch traj_sys.tcl

for i in {00000..00666}
    do 
    echo "animate goto $i" >> traj_sys.tcl
    #echo "rotate x by 0.5" >> traj_sys.tcl
    echo "render Tachyon /home/dick/Desktop/presentation_traj/sys/sys$i.dat /usr/local/lib/vmd/tachyon_LINUXAMD64 -mediumshade -aasamples 12 %s -format TARGA -res 1920 1080 -o %s.tga" >> traj_sys.tcl
done

