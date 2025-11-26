import matplotlib.pyplot as plt

# gpu_alltoall timings
TEST_SIZE                 = [           1,            2,            4,            8,           16,           32,           64,          128,          256,          512,         1024,         2048,         4096,         8192,        16384,        32768,        65536,       131072,       262144,       524288]
# PMPI_TIMES                = [7.371147e-06, 7.363185e-06, 7.361157e-06, 7.364657e-06, 7.362917e-06, 7.356881e-06, 7.385159e-06, 7.388837e-06, 7.389716e-06, 7.397343e-06, 7.416003e-06, 7.479695e-06, 7.621184e-06, 7.645173e-06, 7.704429e-06, 7.724955e-06, 7.887628e-06, 7.923775e-06, 8.183318e-06, 8.881558e-06]
GPU_P_WISE_TIMES          = [6.870522e-04, 6.856073e-04, 6.856778e-04, 6.845764e-04, 6.851729e-04, 6.842542e-04, 6.845944e-04, 6.854029e-04, 6.847766e-04, 6.846961e-04, 6.838248e-04, 6.857002e-04, 6.836948e-04, 6.879169e-04, 6.917843e-04, 7.003560e-04, 7.163912e-04, 7.454135e-04, 1.520770e-03, 2.946504e-03]
GPU_NON_BLOCKING_TIMES    = [6.864572e-04, 6.863279e-04, 6.860292e-04, 6.857140e-04, 6.863580e-04, 6.851268e-04, 6.854083e-04, 6.860709e-04, 6.851120e-04, 6.843392e-04, 6.856143e-04, 6.860100e-04, 6.822670e-04, 6.893121e-04, 6.923034e-04, 7.009618e-04, 7.179974e-04, 7.457572e-04, 1.520328e-03, 2.960296e-03]
CTC_P_WISE_TIMES          = [6.987214e-04, 6.972971e-04, 6.979407e-04, 6.975813e-04, 6.985528e-04, 6.973423e-04, 6.979871e-04, 6.985840e-04, 6.980454e-04, 6.984976e-04, 7.011740e-04, 7.003597e-04, 7.021022e-04, 7.129453e-04, 7.231965e-04, 8.060664e-04, 8.552497e-04, 9.643857e-04, 1.862845e-03, 3.445407e-03]
CTC_NON_BLOCKING_TIMES    = [6.987074e-04, 6.983300e-04, 6.982004e-04, 6.985613e-04, 6.985036e-04, 6.990171e-04, 6.991852e-04, 6.991420e-04, 6.996042e-04, 7.378021e-04, 7.571471e-04, 7.602690e-04, 7.624456e-04, 7.692210e-04, 7.809033e-04, 8.075441e-04, 8.549010e-04, 9.631673e-04, 1.864799e-03, 3.460144e-03]

# Test size for MPI without GPU-Acceleration
TEST_SIZE_MPI         = [           1,            2,            4,            8,           16,           32,           64,          128,          256,          512,         1024,         2048,         4096,         8192,        16384]
# Non vectorized, non-GPU-Accelerated times
PMPI_TIMES            = [4.258114e-05, 4.286320e-05, 4.815905e-05, 6.156236e-05, 8.125006e-05, 1.338939e-04, 2.487242e-04, 9.844402e-04, 4.678897e-04, 1.169374e-03, 1.658039e-03, 3.033246e-03, 6.050317e-03, 1.173416e-02, 2.289635e-02]
MPIX_TIMES            = [2.630234e-03, 3.538980e-04, 4.142768e-04, 6.652896e-04, 3.661942e-04, 7.952576e-04, 5.041786e-04, 8.766378e-04, 9.734534e-04, 9.066051e-04, 1.665729e-03, 3.514598e-03, 6.826788e-03, 1.310346e-02, 2.582901e-02]
# MPI (non-GPU-accelerated) with vectorization
PMPI_VECTORIZED_TIMES = [1.402051e-04, 1.394434e-04, 1.477697e-04, 9.126485e-04, 2.181496e-04, 3.558985e-04, 3.291239e-04, 4.996010e-04, 5.688856e-04, 1.215114e-03, 1.668159e-03, 3.042503e-03, 6.055685e-03, 1.176972e-02, 2.301293e-02]
MPIX_VECTORIZED_TIMES = [1.966063e-04, 2.011106e-04, 2.140012e-04, 2.545202e-04, 3.525960e-04, 4.404482e-04, 5.929759e-04, 7.617561e-04, 1.028282e-03, 9.132279e-04, 1.661844e-03, 3.391091e-03, 6.942222e-03, 1.307528e-02, 2.577212e-02]

# Plot the GPU times
def plot_gpu_alltoall():
    #graph
    plt.plot(TEST_SIZE, GPU_P_WISE_TIMES,       '-o', label="GPU-Aware Pairwise Exchange",   markersize=3)
    plt.plot(TEST_SIZE, GPU_NON_BLOCKING_TIMES, '-*', label="GPU-Aware Nonblocking",         markersize=3)
    plt.plot(TEST_SIZE, CTC_P_WISE_TIMES,       ':s', label="Copy-to-CPU Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE, CTC_NON_BLOCKING_TIMES, ':+', label="Copy-to-CPU Nonblocking",       markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()

def plot_cpu_alltoall():
    #graph
    plt.plot(TEST_SIZE_MPI, PMPI_TIMES,       '-o', label="MPI Alltoall",   markersize=3)
    plt.plot(TEST_SIZE_MPI, MPIX_TIMES, '-*', label="MPIX Alltoall",         markersize=3)
    plt.plot(TEST_SIZE_MPI, PMPI_VECTORIZED_TIMES,       ':s', label="MPI Alltoallv", markersize=3)
    plt.plot(TEST_SIZE_MPI, MPIX_VECTORIZED_TIMES, ':+', label="MPIX Alltoallv",       markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()
   

if __name__ == "__main__":
  plot_gpu_alltoall()
  plot_cpu_alltoall()