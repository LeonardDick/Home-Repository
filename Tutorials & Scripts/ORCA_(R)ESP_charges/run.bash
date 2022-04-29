#!/bin/bash
#PBS -N r-but-m1
#PBS -l nodes=1:ppn=8
#PBS -e error.out
#PBS -o bash.out
#PBS -q berta
#PBS -W umask=022

name="opt"

# Scratch
SCRATCH=/tmp1
mkdir -pv $SCRATCH/$USER/$PBS_JOBID
cd $SCRATCH/$USER/$PBS_JOBID
cp -vL $PBS_O_WORKDIR/* .


# GCC
base="/home/domaros/local/gcc-6.3.0"
PATH="$base/bin:$PATH"
LD_LIBRARY_PATH="$base/lib64:$LD_LIBRARY_PATH"

# OpenMPI
base="/home/domaros/local/openmpi-2.1.0"
PATH="$base/bin:$PATH"
CPATH="$base/include:$CPATH"
LD_LIBRARY_PATH="$base/lib64:$LD_LIBRARY_PATH"

# FFTW
base="/home/domaros/local/fftw-3.3.6-pl1"
PATH="$base/bin:$PATH"
CPATH="$base/include:$CPATH"
LD_LIBRARY_PATH="$base/lib64:$LD_LIBRARY_PATH"

# Exports
export PATH
export LD_LIBRARY_PATH
export CPATH

# Command
/software/cluster/orca_4_0_0_linux_x86-64/orca orca.inp | tee orca.out

OUTDIR=$name"_out"
i=$(find $PBS_O_WORKDIR/ -type d -name $name"_out*" | wc -l)

mkdir -pv $PBS_O_WORKDIR/$OUTDIR$i
cd $PBS_O_WORKDIR/$OUTDIR$i
cp -r $SCRATCH/$USER/$PBS_JOBID/* .
rm *.tmp
