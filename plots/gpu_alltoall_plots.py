import matplotlib.pyplot as plt


# New GPU Times (with Amanda's suggested changes - had comm errors for big sizes):
TEST_SIZE                  = [           1,            2,            4,            8,           16,           32,           64,          128,          256,          512,         1024,         2048]
PMPI_TIMES                 = [7.218749e-06, 7.207187e-06, 7.205507e-06, 7.206931e-06, 7.201176e-06, 7.200824e-06, 7.223923e-06, 7.227737e-06, 7.229175e-06, 7.237945e-06, 7.263101e-06, 7.328521e-06]
GPU_P_WISE_TIMES           = [3.409981e-06, 3.411037e-06, 3.416509e-06, 3.421593e-06, 3.458747e-06, 2.824896e-06, 2.855862e-06, 2.896217e-06, 2.982784e-06, 3.188929e-06, 3.342124e-06, 3.574154e-06]
GPU_NON_BLOCKING_TIMES     = [3.404281e-06, 3.402847e-06, 3.410595e-06, 3.422638e-06, 3.449654e-06, 2.881115e-06, 2.912966e-06, 2.954216e-06, 3.038802e-06, 3.241911e-06, 3.382351e-06, 3.624526e-06]
CTC_P_WISE_TIMES           = [1.265935e-05, 1.291080e-05, 1.286333e-05, 1.291271e-05, 1.295210e-05, 1.301558e-05, 1.305365e-05, 1.338007e-05, 1.381761e-05, 1.443836e-05, 1.588557e-05, 1.873525e-05]
CTC_NON_BLOCKING_TIMES     = [1.272437e-05, 1.296329e-05, 1.290464e-05, 1.296755e-05, 1.299877e-05, 1.307658e-05, 1.310716e-05, 1.345244e-05, 1.390525e-05, 1.479172e-05, 1.826904e-05, 2.056418e-05]

# Testing Size 4096 only partially completed :'(
# PMPI_Alltoall Time 7.423982e-06
# GPU-Aware Pairwise Exchange Time 4.141709e-06

# OLD TIMINGS
# gpu_alltoall timings
TEST_SIZE_OLD              = [           1,            2,            4,            8,           16,           32,           64,          128,          256,          512,         1024,         2048,         4096,         8192,        16384,        32768,        65536,       131072,       262144,       524288]
# PMPI_TIMES                = [7.371147e-06, 7.363185e-06, 7.361157e-06, 7.364657e-06, 7.362917e-06, 7.356881e-06, 7.385159e-06, 7.388837e-06, 7.389716e-06, 7.397343e-06, 7.416003e-06, 7.479695e-06, 7.621184e-06, 7.645173e-06, 7.704429e-06, 7.724955e-06, 7.887628e-06, 7.923775e-06, 8.183318e-06, 8.881558e-06]
GPU_P_WISE_TIMES_OLD       = [6.870522e-04, 6.856073e-04, 6.856778e-04, 6.845764e-04, 6.851729e-04, 6.842542e-04, 6.845944e-04, 6.854029e-04, 6.847766e-04, 6.846961e-04, 6.838248e-04, 6.857002e-04, 6.836948e-04, 6.879169e-04, 6.917843e-04, 7.003560e-04, 7.163912e-04, 7.454135e-04, 1.520770e-03, 2.946504e-03]
GPU_NON_BLOCKING_TIMES_OLD = [6.864572e-04, 6.863279e-04, 6.860292e-04, 6.857140e-04, 6.863580e-04, 6.851268e-04, 6.854083e-04, 6.860709e-04, 6.851120e-04, 6.843392e-04, 6.856143e-04, 6.860100e-04, 6.822670e-04, 6.893121e-04, 6.923034e-04, 7.009618e-04, 7.179974e-04, 7.457572e-04, 1.520328e-03, 2.960296e-03]
CTC_P_WISE_TIMES_OLD       = [6.987214e-04, 6.972971e-04, 6.979407e-04, 6.975813e-04, 6.985528e-04, 6.973423e-04, 6.979871e-04, 6.985840e-04, 6.980454e-04, 6.984976e-04, 7.011740e-04, 7.003597e-04, 7.021022e-04, 7.129453e-04, 7.231965e-04, 8.060664e-04, 8.552497e-04, 9.643857e-04, 1.862845e-03, 3.445407e-03]
CTC_NON_BLOCKING_TIMES_OLD = [6.987074e-04, 6.983300e-04, 6.982004e-04, 6.985613e-04, 6.985036e-04, 6.990171e-04, 6.991852e-04, 6.991420e-04, 6.996042e-04, 7.378021e-04, 7.571471e-04, 7.602690e-04, 7.624456e-04, 7.692210e-04, 7.809033e-04, 8.075441e-04, 8.549010e-04, 9.631673e-04, 1.864799e-03, 3.460144e-03]

# Test size for MPI without GPU-Acceleration
TEST_SIZE_MPI         = [           1,            2,            4,            8,           16,           32,           64,          128,          256,          512,         1024,         2048,         4096,         8192,        16384]
# Non variable-length, non-GPU-Accelerated times
PMPI_TIMES            = [4.258114e-05, 4.286320e-05, 4.815905e-05, 6.156236e-05, 8.125006e-05, 1.338939e-04, 2.487242e-04, 9.844402e-04, 4.678897e-04, 1.169374e-03, 1.658039e-03, 3.033246e-03, 6.050317e-03, 1.173416e-02, 2.289635e-02]
MPIX_TIMES            = [2.630234e-03, 3.538980e-04, 4.142768e-04, 6.652896e-04, 3.661942e-04, 7.952576e-04, 5.041786e-04, 8.766378e-04, 9.734534e-04, 9.066051e-04, 1.665729e-03, 3.514598e-03, 6.826788e-03, 1.310346e-02, 2.582901e-02]
# MPI (non-GPU-accelerated) with variable length message size
PMPI_V_TIMES = [1.402051e-04, 1.394434e-04, 1.477697e-04, 9.126485e-04, 2.181496e-04, 3.558985e-04, 3.291239e-04, 4.996010e-04, 5.688856e-04, 1.215114e-03, 1.668159e-03, 3.042503e-03, 6.055685e-03, 1.176972e-02, 2.301293e-02]
MPIX_V_TIMES = [1.966063e-04, 2.011106e-04, 2.140012e-04, 2.545202e-04, 3.525960e-04, 4.404482e-04, 5.929759e-04, 7.617561e-04, 1.028282e-03, 9.132279e-04, 1.661844e-03, 3.391091e-03, 6.942222e-03, 1.307528e-02, 2.577212e-02]

# DELTA Timings
TEST_SIZE_DELTA       = [           1,            2,            4,            8,           16,           32,           64,          128,          256,          512,         1024,         2048,         4096,         8192,        16384,        32768,        65536,       131072,       262144,       524288]
# PMPI_Alltoall_DELTA   = [6.967843e-06, 6.955969e-06, 6.950089e-06, 6.951983e-06, 6.942560e-06, 6.937628e-06, 6.950715e-06, 6.971834e-06, 7.043043e-06, 7.062413e-06, 7.065228e-06, 7.172110e-06, 7.139564e-06, 7.213729e-06, 7.259430e-06, 7.257276e-06, 7.383624e-06, 7.814454e-06, 8.052476e-06, 8.819650e-06]
GPU_AWARE_PAIR_DELTA  = [1.692440e-07, 1.700136e-07, 1.700103e-07, 1.708992e-07, 1.727185e-07, 1.790119e-07, 1.912952e-07, 2.092884e-07, 7.583231e-06, 7.576276e-06, 7.613759e-06, 7.652875e-06, 7.681321e-06, 7.749346e-06, 7.833737e-06, 7.836609e-06, 7.916391e-06, 8.377364e-06, 8.625037e-06, 9.194491e-06]
GPU_AWARE_NB_DELTA    = [1.865370e-07, 1.944192e-07, 1.929703e-07, 1.929050e-07, 1.970901e-07, 2.046335e-07, 2.235919e-07, 7.650981e-06, 7.657992e-06, 7.676133e-06, 8.011378e-06, 7.772269e-06, 7.800222e-06, 7.832519e-06, 7.872975e-06, 7.862562e-06, 8.017000e-06, 8.404112e-06, 8.666169e-06, 9.317228e-06]
COPY_TO_CPU_PAIR_DELTA= [1.250582e-05, 1.258676e-05, 1.255021e-05, 1.259792e-05, 1.267250e-05, 1.267269e-05, 1.279296e-05, 1.295909e-05, 1.371367e-05, 1.448124e-05, 1.532527e-05, 1.647678e-05, 1.936765e-05, 2.504420e-05, 2.606036e-05, 3.135194e-05, 4.813934e-05, 8.636736e-05, 7.418997e-03, 1.440126e-02]
COPY_TO_CPU_NB_DELTA  = [1.250392e-05, 1.253748e-05, 1.251516e-05, 1.260944e-05, 1.268359e-05, 1.269461e-05, 1.278583e-05, 1.301615e-05, 1.393210e-05, 1.459684e-05, 1.507721e-05, 1.614107e-05, 1.800486e-05, 2.183672e-05, 2.337580e-05, 3.153096e-05, 4.838520e-05, 8.609277e-05, 7.208337e-03, 1.433501e-02]




# Plot the old GPU times (h100)
def plot_gpu_alltoall_old():
    #graph
    plt.plot(TEST_SIZE_OLD, GPU_P_WISE_TIMES_OLD,       '-o',  label="GPU-Aware Pairwise Exchange",   markersize=3)
    plt.plot(TEST_SIZE_OLD, GPU_NON_BLOCKING_TIMES_OLD, '--*', label="GPU-Aware Nonblocking",         markersize=3)
    plt.plot(TEST_SIZE_OLD, CTC_P_WISE_TIMES_OLD,       '-s',  label="Copy-to-CPU Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE_OLD, CTC_NON_BLOCKING_TIMES_OLD, '--+', label="Copy-to-CPU Nonblocking",       markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()

# CPU times (h100)
def plot_cpu_alltoall_h100():
    #graph
    plt.plot(TEST_SIZE_MPI, PMPI_TIMES,            '-o',  label="MPI Alltoall",   markersize=3)
    plt.plot(TEST_SIZE_MPI, MPIX_TIMES,            '-*',  label="MPIX Alltoall",  markersize=3)
    plt.plot(TEST_SIZE_MPI, PMPI_V_TIMES, '--s', label="MPI Alltoallv",  markersize=3)
    plt.plot(TEST_SIZE_MPI, MPIX_V_TIMES, '--+', label="MPIX Alltoallv", markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()
   
# Plot the GPU times for H100s
def plot_gpu_alltoall_new_h100():
    #graph
    plt.plot(TEST_SIZE,       GPU_P_WISE_TIMES,  '-o',   label="GPU-Aware Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE, GPU_NON_BLOCKING_TIMES, '--*',         label="GPU-Aware Nonblocking", markersize=3)
    plt.plot(TEST_SIZE,       CTC_P_WISE_TIMES,  '-s', label="Copy-to-CPU Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE, CTC_NON_BLOCKING_TIMES, '--+',       label="Copy-to-CPU Nonblocking", markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()

# Plot the GPU times for DELTA
def plot_delta_minus_last_two():
    plt.plot(TEST_SIZE_DELTA[:len(TEST_SIZE_DELTA) - 2:],   GPU_AWARE_PAIR_DELTA[:len(TEST_SIZE_DELTA) - 2:],  '-o',   label="GPU-Aware Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE_DELTA[:len(TEST_SIZE_DELTA) - 2:],     GPU_AWARE_NB_DELTA[:len(TEST_SIZE_DELTA) - 2:], '--*',         label="GPU-Aware Nonblocking", markersize=3)
    plt.plot(TEST_SIZE_DELTA[:len(TEST_SIZE_DELTA) - 2:], COPY_TO_CPU_PAIR_DELTA[:len(TEST_SIZE_DELTA) - 2:],  '-s', label="Copy-to-CPU Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE_DELTA[:len(TEST_SIZE_DELTA) - 2:],   COPY_TO_CPU_NB_DELTA[:len(TEST_SIZE_DELTA) - 2:], '--+',       label="Copy-to-CPU Nonblocking", markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()

# Plot the GPU times for DELTA
def plot_delta():
    plt.plot(TEST_SIZE_DELTA,   GPU_AWARE_PAIR_DELTA,  '-o',   label="GPU-Aware Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE_DELTA,     GPU_AWARE_NB_DELTA, '--*',         label="GPU-Aware Nonblocking", markersize=3)
    plt.plot(TEST_SIZE_DELTA, COPY_TO_CPU_PAIR_DELTA,  '-s', label="Copy-to-CPU Pairwise Exchange", markersize=3)
    plt.plot(TEST_SIZE_DELTA,   COPY_TO_CPU_NB_DELTA, '--+',       label="Copy-to-CPU Nonblocking", markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()

# Plot the GPU times vs. CPU times for H100s
def plot_main_h100():
    #graph
    plt.plot(    TEST_SIZE,              GPU_P_WISE_TIMES,  '-o',   label="GPU-Aware Pairwise Exchange", markersize=3)
    plt.plot(    TEST_SIZE,        GPU_NON_BLOCKING_TIMES, '--*',         label="GPU-Aware Nonblocking", markersize=3)
    plt.plot(    TEST_SIZE,              CTC_P_WISE_TIMES,  '-s', label="Copy-to-CPU Pairwise Exchange", markersize=3)
    plt.plot(    TEST_SIZE,        CTC_NON_BLOCKING_TIMES, '--+',       label="Copy-to-CPU Nonblocking", markersize=3)
    plt.plot(    TEST_SIZE, PMPI_TIMES[0:len(TEST_SIZE):],  '-x',                  label="MPI Alltoall", markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()

# Plot the GPU times for DELTA against those for h100
def plot_delta_vs_h100():
    plt.plot(TEST_SIZE,   GPU_AWARE_PAIR_DELTA[0:len(TEST_SIZE):],  '-o',   label="GPU-Aware Pairwise Exchange(gh200)", markersize=3)
    plt.plot(TEST_SIZE,     GPU_AWARE_NB_DELTA[0:len(TEST_SIZE):], '--*',         label="GPU-Aware Nonblocking(gh200)", markersize=3)
    plt.plot(TEST_SIZE, COPY_TO_CPU_PAIR_DELTA[0:len(TEST_SIZE):],  '-s', label="Copy-to-CPU Pairwise Exchange(gh200)", markersize=3)
    plt.plot(TEST_SIZE,   COPY_TO_CPU_NB_DELTA[0:len(TEST_SIZE):], '--+',       label="Copy-to-CPU Nonblocking(gh200)", markersize=3)
    plt.plot(TEST_SIZE,                          GPU_P_WISE_TIMES,  '-o',    label="GPU-Aware Pairwise Exchange(h100)", markersize=3)
    plt.plot(TEST_SIZE,                    GPU_NON_BLOCKING_TIMES, '--*',          label="GPU-Aware Nonblocking(h100)", markersize=3)
    plt.plot(TEST_SIZE,                          CTC_P_WISE_TIMES,  '-s',  label="Copy-to-CPU Pairwise Exchange(h100)", markersize=3)
    plt.plot(TEST_SIZE,                    CTC_NON_BLOCKING_TIMES, '--+',        label="Copy-to-CPU Nonblocking(h100)", markersize=3)
    # plt.plot(TEST_SIZE,             PMPI_TIMES[0:len(TEST_SIZE):],  '-x',                  label="MPI Alltoall", markersize=3)
    plt.xlabel("n")
    plt.xscale('log', base=2) # Set x-axis to logarithmic scale
    # plt.yscale('log', base=10) # Set y-axis to logarithmic scale
    plt.ylabel("Time of Algorithm (seconds)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
#   plot_gpu_alltoall_old()
  plot_cpu_alltoall_h100()
  plot_gpu_alltoall_new_h100()
  plot_main_h100()
  plot_delta()
  plot_delta_minus_last_two()
  plot_delta_vs_h100()
