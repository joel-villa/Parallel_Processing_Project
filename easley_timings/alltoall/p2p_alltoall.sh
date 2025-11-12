#!/bin/bash
#SBATCH --job-name=CS542_p2p_alltoall
#SBATCH --partition=debug
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=64
#SBATCH --time=00:45:00
#SBATCH --output=p2p_alltoall.out
#SBATCH --error=p2p_alltoall.err

module load openmpi/4.1.7-cuda-6zaq

srun --nodes=2  --ntasks-per-node=64 --partition=debug ../../locality_aware/build/benchmarks/./p2p_alltoall
