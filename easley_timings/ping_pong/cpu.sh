#!/bin/bash
#SBATCH --job-name=CS542_Microbenchmarks
#SBATCH --partition=debug
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=64
#SBATCH --time=00:45:00
#SBATCH --output=cpu_ppong.out
#SBATCH --error=cpu_ppong.err

module load openmpi/4.1.7-cuda-6zaq

srun --nodes=2  --ntasks-per-node=64 --partition=debug ../../locality_aware/build/benchmarks/./microbenchmarks 
