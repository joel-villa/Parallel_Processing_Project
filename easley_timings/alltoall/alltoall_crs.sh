#!/bin/bash
#SBATCH --job-name=CS542_alltoall_crs
#SBATCH --partition=debug
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=64
#SBATCH --time=00:45:00
#SBATCH --output=alltoall_crs.out
#SBATCH --error=alltoall_crs.err

module load openmpi/4.1.7-cuda-6zaq

srun --nodes=2  --ntasks-per-node=64 --partition=debug ../../locality_aware/build/benchmarks/./alltoall_crs
