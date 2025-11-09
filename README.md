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

### History
 974  cd benchmarks/
  975  ls
  976  git checkout microbenchmarks
  977  cd ..
  978  git checkout microbenchmarks
  979  git branch
  980  ccmake ..
  981  ls
  982  ls benchmarks/
  983  ls Testing/
  984  make install
  985  make microbenchmarks
  986  ls
  987  rm -rf *
  988  ls
  989  rm -rf Testing/
  990  cmake -DUSE_CUDA=ON ..
  991  make
  992  cd benchmarks/
  993  ls
  994  cd ..
  995  vi ../benchmarks/CMakeLists.txt 
  996  git checkout ../benchmarks/
  997  make
  998  ls
  999  cd benchmarks/
 1000  srun -n4 ./microbenchmarks
 1001  ls
 1002  cd ..
 1003  ls
 1004  cd ..
 1005  ls
 1006  cd benchmarks/
 1007  ls
 1008  cd ..
 1009  ls
 1010  cd benchmark
 1011  cd benchmarks/
 1012  ls
 1013  vim microbenchmarks.cpp 
 1014  ls
 1015  cd build/
 1016  make
 1017  cd ../..
 1018  ls
 1019  cd build/
 1020  make
 1021  cd benchmarks/
 1022  ls
 1023  srun -N2 -n128 ./microbenchmarks
 1024  srun -N2 -n128 --parititon debug ./microbenchmarks
 1025  srun -N2 -n128 --partition debug ./microbenchmarks
 1026  ls
 1027  history 
[jvillarreal3@easley benchmarks]$ 


### Update main directories CMake lines 27 & 28

```
set(MPIRUN "srun" CACHE STRING "MPIRUN command")
set(CUDA_ARCH "90" CACHE STRING "CUDA Architecture")
```

### OpenMPI Micro Benchmarks
https://github.com/mpi-advance/locality_aware/tree/microbenchmarks/benchmarks
