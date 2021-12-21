#!/usr/bin/python3

'''
PoreBuilder 2

--> generating Graphene sheets with multiple layers
--> generating carbon nanotubes
--> generating pore systems
'''

#General section
import os
import math
import numpy as np
from numpy.core.defchararray import count

#Moving and generating files
os.system("rm -rf old")
os.system("mkdir old")
os.system("mv build.log graphenesheet.xyz pore* tube.xyz old/ 2>/dev/null ")
#os.system("touch build.log")

#General questions
print('#_____________Porebuilder2____________#')
print('---------------------------------------')
choice_length= float(input('Write coordinate file in [1]Angström or [2]Bohr?    '))
iflayer= float(input('Do you want to generate a pore structure? [1]Yes [2]No    '))
if iflayer==1:
    iflayer2=1
else:
    iflayer2= float(input('Do you want to generate graphene layers? [1]Yes [2]No    '))
if iflayer2==1:
    size_graphsheet = float(input('How large should the graphene sheets be? [Angström]  '))
    num_layer= float(input('How many graphene layers?   '))

#Generating graphene sheet
    anginbohr=1.8897259886
    carbon_distance=1.42
    distance_row_y=1.229756
    interlayer_distance=3.35
    if choice_length == 2:
        carbon_distance=1.42*anginbohr
        distance_row_y=1.229756*anginbohr
        interlayer_distance=3.35*anginbohr
        size_graphsheet = size_graphsheet*anginbohr
        print('--> Multiplying values by %0.6f'%(anginbohr))
    print('--> C-C distance %0.6f'%(carbon_distance))
    print('--> Distance carbon per row %0.6f'%(distance_row_y))
    print('--> Interlayer distance %0.6f'%(interlayer_distance))

    atomcount=0
    xyz=open("graphenesheet.xyz", "x")
    xyz.write("   XXX\n")
    xyz.write("#Made by Porebuilder\n")


    coord_x=-carbon_distance*1.5
    coord_y=0
    coord_z=0
    maximumx=0
    maximumy=0
    maximumz=0
    counterx=0
    countery=0
    runx=2
    runy=1
    runz=1
    while True:
        while True:
            if (runy%2)==0:
                runx=2
            else:
                runx=3
            while True:
                coord_x=coord_x+carbon_distance
                if maximumx <= coord_x:
                    maximumx=coord_x
                if runx == 3:
                    runx=1
                    continue
                if (runz%2)==0:
                    xyz.write("C    {:.6f}        {:.6f}        {:6f}\n".format(coord_x, coord_y, coord_z))
                else:
                    xshift=coord_x+carbon_distance
                    xyz.write("C    {:.6f}        {:.6f}        {:6f}\n".format(xshift, coord_y, coord_z))   
                runx=runx+1
                atomcount=atomcount+1
                counterx=counterx+1
                if coord_x >= size_graphsheet:
                    if (counterx%2)==0:
                        break
            if (runy%2)==0:
                coord_x=-carbon_distance*1.5
            else:
                coord_x=-carbon_distance
            runy=runy+1
            countery=countery+1
            if coord_y >= size_graphsheet:
                if (countery%2)==0:
                    break
            coord_y=coord_y+distance_row_y
            if maximumy <= coord_y:
               maximumy=coord_y
        coord_y=0
        if runz==num_layer:
            break
        coord_z=coord_z+interlayer_distance
        if maximumz <= coord_z:
            maximumz=coord_z
        runz=runz+1
    xyz.close()
    os.system("sed -i 's/XXX/{0}/g' graphenesheet.xyz".format(atomcount))
    print('--> Sheet size in x direction %0.6f'%(maximumx))
    print('--> Sheet size in y direction %0.6f'%(maximumy))
    print('--> Sheet size in z direction %0.6f'%(maximumz))

#CNT SECTION
#Input
if iflayer==1:
    tube=1
else:
    if iflayer2==1:
        tube=float(input('Do you also want to produce a CNT? [1]Yes [2]No    '))
    else:
        tube=float(input('Do you want to produce a CNT? [1]Yes [2]No    '))
if tube==1:
    tube_xyz=open("tube.xyz", "x")
    tube_xyz.write("   XXX\n")
    tube_xyz.write("#Made by Porebuilder\n")
    #which_conf=float(input('Which conformation of the CNT? [1]armchair [2]zigzag  '))
    which_conf=2
    print('--> CNT in zigzag conformation (for now no armchair)')
    print('---------------------------------------')
    atom_circ=float(input('How many atoms for the circumference of CNT?    '))
    tubelength=float(input('How long do you want the tube to be?   '))
    print('--> Adjusting tube length for periodicity in z direction)')
    carbon_distance=1.42
    hex_d=2.459512
    tubel_z=0
    interlayer_distance=3.35
    if choice_length == 2:
        carbon_distance=1.42*anginbohr
        hex_d=2.459512*anginbohr
        interlayer_distance=3.35*anginbohr
        size_graphsheet = size_graphsheet*anginbohr
        print('--> Multiplying values by %0.6f'%(anginbohr))

#Calculating distances from given input
    step=360/atom_circ 
    #armcnt
    if which_conf==1:
        circumference=atom_circ*carbon_distance*1.5
        diameter=circumference/3.14159265
        print('--> Circumference: %0.6f'%(circumference))
        print('--> Diameter: %0.6f'%(diameter))
        while True:
            if tubel_z >= tubelength:
                break
            tubel_z=tubel_z+hex_d*2
        print('--> Tubelength: %0.6f'%(tubel_z))

    #zigzag
    if which_conf==2:
        circumference=atom_circ*hex_d
        diameter=circumference/3.14159265
        print('--> Circumference: %0.6f'%(circumference))
        print('--> Diameter: %0.6f'%(diameter))
        distx=(np.sin(np.deg2rad(0))*diameter/2-np.sin(np.deg2rad(step/2))*diameter/2)
        disty=(np.cos(np.deg2rad(0))*diameter/2-np.cos(np.deg2rad(step/2))*diameter/2)
        zstep=(carbon_distance**2-distx**2-disty**2)**0.5
        print('--> Zstep in tube: %0.6f'%(zstep))  
        tubel_z=carbon_distance+zstep
        while True:
            if tubel_z >= tubelength:
                break
            tubel_z=tubel_z+carbon_distance*2+zstep*2
        print('--> Tubelength: %0.6f'%(tubel_z))

#Defining the xy-center of the tube at z=0
    if iflayer2==1:
        centerx=maximumx/2
        centery=maximumy/2 
    else:
        centerx=0
        centery=0
    tube_count=0
    centerz=0
    count_deg=0
    tubez=0
    count_stepz=1
    runz=2
    stopz=tubel_z+carbon_distance*1.5
    radius=diameter/2

    while True: 
        if runz<=2:
            count_deg=0
        else:
            count_deg=step/2
        while True:
            tubex=centerx+np.sin(np.deg2rad(count_deg))*radius
            tubey=centery+np.cos(np.deg2rad(count_deg))*radius
            tube_xyz.write("C    {:.6f}        {:.6f}        {:.6f}\n".format(tubex, tubey, tubez))
            tube_count=tube_count+1
            count_deg=count_deg+step
            if count_deg >= 360:
                break        
        count_stepz=count_stepz+1
        if  count_stepz==3:
            tubez=tubez+carbon_distance
            count_stepz=1
        else:
            tubez=tubez+zstep 
        runz=runz+1
        if runz > 4:
            runz=1
        if tubez >= stopz:
            break


    tube_xyz.close()
    os.system("sed -i 's/XXX/{0}/g' tube.xyz".format(tube_count))

#Producing pore
graph_count=0
tube_count=0
if iflayer==1:
    print('---------------------------------------')
    print('Combining layers and tube...')

    with open("graphenesheet.xyz", "r") as xyz:
            graph_count=int(xyz.readline())
    with open("tube.xyz", "r") as tube_xyz:
            tube_count=int(tube_xyz.readline())
    
    print('Number of graph sheet atoms:  {0}'.format(graph_count))
    print('Number of tube atoms:  {0}'.format(tube_count))
    poreatoms=graph_count+tube_count
    print('--> Initial Number of pore atoms:  {0}'.format(poreatoms))
    
    with open("pore.xyz", "x") as pore_xyz:
        pore_xyz.write(" XXX\n")
        pore_xyz.write("#Made by Porebuilder\n")

    os.system("tail -n +3 'graphenesheet.xyz' > adaptx.xyz")
    os.system("sed 's/C//g' adaptx.xyz > adapt.xyz")
    os.system("rm -rf adaptx.xyz")

    with open("adapt.xyz", "r") as ada_xyz:
        content= ada_xyz.readlines()

    counterq=0
    tubekind=float(input('[1]Pore with walls on both ends or [2]Closed Pore with 1 wall (left and right)?   '))  
    if tubekind==1: 
        with open('pore.xyz', "a") as pore_xyz:
            for line in content:
                    content=line.split()
                    dist=((centerx-float(content[0]))**2+(centery-float(content[1]))**2)**0.5
                    if dist >= diameter/2+carbon_distance:
                        pore_xyz.write("C    {:.6f}        {:.6f}        {:.6f}\n".format(float(content[0]), float(content[1]), float(content[2])))
                        counterq=counterq+1
        with open("adapt.xyz", "r") as ada_xyz:
            content= ada_xyz.readlines()
        with open('pore.xyz', "a") as pore_xyz:
            for line in content: 
                    content=line.split()
                    dist=((centerx-float(content[0]))**2+(centery-float(content[1]))**2)**0.5                   
                    if dist >= diameter/2+carbon_distance:
                        posx=float(content[0])
                        posy=float(content[1])
                        posz=float(content[2])+tubel_z+zstep-(num_layer-1)*interlayer_distance
                        pore_xyz.write("C    {:.6f}        {:.6f}        {:.6f}\n".format(posx, posy, posz))
                        counterq=counterq+1
    if tubekind==2: 
        os.system('cp pore.xyz pore_right.xyz')
        with open('pore_right.xyz', "a") as pore_xyz:
            for line in content:
                    content=line.split()
                    dist=((centerx-float(content[0]))**2+(centery-float(content[1]))**2)**0.5
                    if dist >= diameter/2+carbon_distance:
                        pore_xyz.write("C    {:.6f}        {:.6f}        {:.6f}\n".format(float(content[0]), float(content[1]), float(content[2])))
                        counterq=counterq+1
                    if dist <= diameter/2-carbon_distance:
                        if float(content[2])==0:
                            floatz=tubel_z+zstep
                            pore_xyz.write("C    {:.6f}        {:.6f}        {:.6f}\n".format(float(content[0]), float(content[1]), floatz))
                            counterq=counterq+1
        counterq=0
    with open("adapt.xyz", "r") as ada_xyz:
        content= ada_xyz.readlines()
    if tubekind==2:
        os.system('mv pore.xyz pore_left.xyz') 
        with open('pore_left.xyz', "a") as pore2_xyz:
            for line in content:
                    content=line.split()
                    dist=((centerx-float(content[0]))**2+(centery-float(content[1]))**2)**0.5
                    if dist >= diameter/2+carbon_distance:
                        posx=float(content[0])
                        posy=float(content[1])
                        posz=float(content[2])+tubel_z+zstep-(num_layer-1)*interlayer_distance
                        pore2_xyz.write("C    {:.6f}        {:.6f}        {:.6f}\n".format(posx, posy, posz))
                        counterq=counterq+1
                    if dist <= diameter/2-carbon_distance:
                        if float(content[2])==0:
                            floatz=0
                            pore2_xyz.write("C    {:.6f}        {:.6f}        {:.6f}\n".format(float(content[0]), float(content[1]), floatz))
                            counterq=counterq+1
    atom_pore=counterq+tube_count
    if tubekind==1:
        os.system("tail -n +3 'tube.xyz' >> pore.xyz")
        os.system("sed -i 's/XXX/{0}/g' pore.xyz".format(atom_pore))
    else:
        os.system("tail -n +3 'tube.xyz' >> pore_right.xyz")
        os.system("tail -n +3 'tube.xyz' >> pore_left.xyz")   
        os.system("sed -i 's/XXX/{0}/g' pore_left.xyz".format(atom_pore))
        os.system("sed -i 's/XXX/{0}/g' pore_right.xyz".format(atom_pore))
    os.system("rm -rf adapt.xyz")

    mw_inp=float(input('Produce elektrode input files for metalwalls? [1]Yes [2]No   ')) 
    if mw_inp==1:
        if tubekind==1:
            os.system("tail -n +3 'pore.xyz' > planar_elec_ua")
            os.system("sed -i 's/C//g' planar_elec_ua")
        else:
            os.system("tail -n +3 'pore_right.xyz' > porous_right_ua")
            os.system("sed -i 's/C//g' porous_right_ua")
            os.system("tail -n +3 'pore_left.xyz' > porous_left_ua")
            os.system("sed -i 's/C//g' porous_left_ua")
