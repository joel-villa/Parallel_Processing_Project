#!/bin/bash
#SBATCH --job-name=CS542_gpu_alltoall
#SBATCH --partition=h100
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:45:00
#SBATCH --output=../gpu_alltoall.out
#SBATCH --error=../errors/gpu_alltoall.err
#SBATCH -G1

module load openmpi/4.1.7-cuda-6zaq

srun --nodes=1  --ntasks-per-node=1 --partition=h100 ../../../locality_aware/build/benchmarks/./gpu_alltoall 
