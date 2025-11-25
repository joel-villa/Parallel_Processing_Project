# Parallel_Processing_Project
Communication Performance, CPU v GPU

## Notes on the Locality Aware Directory

- Important file: locality_aware/include/locality_aware.h

- The "v" in PMPI_Alltoallv and MPIX_Alltoallv stands for vectorized
- PMPI Calls the underlying MPI implementation. 

## Micro Benchmarks
To clone the microbenchmarks along with this repo, run this command after cloning:
```
git submodule update --init --recursive
```

### Running Tests
```
mkdir build
cd build
ccmake .. ## change CUDA to ON, MPI to srun, CUDA_ARCH to 90
make all ## might not be needed
make install ## might not be needed
make 
```

### Numbers She Said to use in benchmarks/microbenchmarks.cpp for Easley
```
#define NODES 2 //number of nodes
#define SPN 2   //number of sockets per node
#define PPNUMA 32 // number of processes per NUMA region
#define PPS 32  //number of processes per socket
#define PPN 64 //number of processes per node
```

### Update main directories CMake lines 27 & 28

```
set(MPIRUN "srun" CACHE STRING "MPIRUN command")
set(CUDA_ARCH "90" CACHE STRING "CUDA Architecture")
```

### OpenMPI Micro Benchmarks
https://github.com/mpi-advance/locality_aware/tree/microbenchmarks/benchmarks
