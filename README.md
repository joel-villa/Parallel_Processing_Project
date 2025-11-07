# Parallel_Processing_Project
Communication Performance, CPU v GPU

## Micro Benchmarks
To clone the microbenchmarks along with this repo, run this command after cloning:
```
git submodule update --init --recursive
```

### Running Tests
```
mkdir build
cd build
cmake ..
make all
make tests
```

### Update main directories CMake lines 27 & 28

```
set(MPIRUN "srun" CACHE STRING "MPIRUN command")
set(CUDA_ARCH "90" CACHE STRING "CUDA Architecture")
```

### OpenMPI Micro Benchmarks
https://github.com/mpi-advance/locality_aware/tree/microbenchmarks/benchmarks
