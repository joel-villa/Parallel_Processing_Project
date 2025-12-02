# Parallel_Processing_Project
Communication Performance, CPU v GPU

## Notes on the Locality Aware Directory

- Important file for some basic comments: locality_aware/include/locality_aware.h
- The "v" in PMPI_Alltoallv and MPIX_Alltoallv stands for variable size, we are going to not worry about this implementation
- PMPI calls the underlying MPI implementation.
- MPIX can be changed to any of their all-to-all implementations by editing the constant at the top of locality_aware/src/collective
/alltoall.c
- IMPORTANT: in src/heterogeneous/gpu_alltoall.c
  - Edit `gpu_aware_alltoall()` to have only the following line:
    `int ierr = f(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, comm);`


Joel's Code:
`// ASSUMES 1 CPU CORE PER GPU (Standard for applications)
int gpu_aware_alltoall(alltoall_ftn f,
        const void* sendbuf, 
        const int sendcount,
        MPI_Datatype sendtype,
        void* recvbuf, 
        const int recvcount, 
        MPI_Datatype recvtype,
        MPIX_Comm* comm)
{

    int ierr = f(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, comm);

    return ierr;
}`

  - Edit `copy_to_cpu_alltoall()` to call malloc and free instead of gpuMallocHost and gpuFreeHost

 `int copy_to_cpu_alltoall(alltoall_ftn f,
        const void* sendbuf, 
        const int sendcount,
        MPI_Datatype sendtype,
        void* recvbuf, 
        const int recvcount, 
        MPI_Datatype recvtype,
        MPIX_Comm* comm)
{
    int ierr = 0;

    int num_procs;
    MPI_Comm_size(comm->global_comm, &num_procs);

    int send_bytes, recv_bytes;
    MPI_Type_size(sendtype, &send_bytes);
    MPI_Type_size(recvtype, &recv_bytes);

    int total_bytes_s = sendcount * send_bytes * num_procs;
    int total_bytes_r = recvcount * recv_bytes * num_procs;

    char* cpu_sendbuf;
    char* cpu_recvbuf;
    cpu_sendbuf = (char*)malloc(total_bytes_s);
    cpu_recvbuf = (char*)malloc(total_bytes_r);
    //gpuMallocHost((void**)&cpu_sendbuf, total_bytes_s);
    //gpuMallocHost((void**)&cpu_recvbuf, total_bytes_r);

    // Copy from GPU to CPU
    ierr += gpuMemcpy(cpu_sendbuf, sendbuf, total_bytes_s, gpuMemcpyDeviceToHost);

    // Collective Among CPUs
    ierr += f(cpu_sendbuf, sendcount, sendtype, cpu_recvbuf, recvcount, recvtype, comm);

    // Copy from CPU to GPU
    ierr += gpuMemcpy(recvbuf, cpu_recvbuf, total_bytes_r, gpuMemcpyHostToDevice);

    free(cpu_sendbuf);
    free(cpu_recvbuf); 
    //gpuFreeHost(cpu_sendbuf);
    //gpuFreeHost(cpu_recvbuf);
    
    return ierr;
}`


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
