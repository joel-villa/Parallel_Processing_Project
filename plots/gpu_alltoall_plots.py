# gpu_alltoall timings
TEST_SIZE                 = [           1,            2,            4,            8,           16,           32,           64,          128,          256,          512,         1024,         2048,         4096,         8192,        16384,        32768,        65536,       131072,       262144,       524288]
PMPI_TIMES                = [7.371147e-06, 7.363185e-06, 7.361157e-06, 7.364657e-06, 7.362917e-06, 7.356881e-06, 7.385159e-06, 7.388837e-06, 7.389716e-06, 7.397343e-06, 7.416003e-06, 7.479695e-06, 7.621184e-06, 7.645173e-06, 7.704429e-06, 7.724955e-06, 7.887628e-06, 7.923775e-06, 8.183318e-06, 8.881558e-06]
GPU_P_WISE_TIMES          = [6.870522e-04, 6.856073e-04, 6.856778e-04, 6.845764e-04, 6.851729e-04, 6.842542e-04, 6.845944e-04, 6.854029e-04, 6.847766e-04, 6.846961e-04, 6.838248e-04, 6.857002e-04, 6.836948e-04, 6.879169e-04, 6.917843e-04, 7.003560e-04, 7.163912e-04, 7.454135e-04, 1.520770e-03, 2.946504e-03]
GPU_NON_BLOCKING_TIMES    = [6.864572e-04, 6.863279e-04, 6.860292e-04, 6.857140e-04, 6.863580e-04, 6.851268e-04, 6.854083e-04, 6.860709e-04, 6.851120e-04, 6.843392e-04, 6.856143e-04, 6.860100e-04, 6.822670e-04, 6.893121e-04, 6.923034e-04, 7.009618e-04, 7.179974e-04, 7.457572e-04, 1.520328e-03, 2.960296e-03]
CTC_P_WISE_TIMES          = [6.987214e-04, 6.972971e-04, 6.979407e-04, 6.975813e-04, 6.985528e-04, 6.973423e-04, 6.979871e-04, 6.985840e-04, 6.980454e-04, 6.984976e-04, 7.011740e-04, 7.003597e-04, 7.021022e-04, 7.129453e-04, 7.231965e-04, 8.060664e-04, 8.552497e-04, 9.643857e-04, 1.862845e-03, 3.445407e-03]
CTC_NON_BLOCKING_TIMES    = [6.987074e-04, 6.983300e-04, 6.982004e-04, 6.985613e-04, 6.985036e-04, 6.990171e-04, 6.991852e-04, 6.991420e-04, 6.996042e-04, 7.378021e-04, 7.571471e-04, 7.602690e-04, 7.624456e-04, 7.692210e-04, 7.809033e-04, 8.075441e-04, 8.549010e-04, 9.631673e-04, 1.864799e-03, 3.460144e-03]

To request GPUs, add --gpus-per-node X or --gpus X, where X is the desired number of GPUs.
Job 112586 running on easley[027-028]
Testing Size 1
PMPI_Alltoallv Time 1.402051e-04
MPIX_Alltoallv Time 1.966063e-04
Testing Size 2
PMPI_Alltoallv Time 1.394434e-04
MPIX_Alltoallv Time 2.011106e-04
Testing Size 4
PMPI_Alltoallv Time 1.477697e-04
MPIX_Alltoallv Time 2.140012e-04
Testing Size 8
PMPI_Alltoallv Time 9.126485e-04
MPIX_Alltoallv Time 2.545202e-04
Testing Size 16
PMPI_Alltoallv Time 2.181496e-04
MPIX_Alltoallv Time 3.525960e-04
Testing Size 32
PMPI_Alltoallv Time 3.558985e-04
MPIX_Alltoallv Time 4.404482e-04
Testing Size 64
PMPI_Alltoallv Time 3.291239e-04
MPIX_Alltoallv Time 5.929759e-04
Testing Size 128
PMPI_Alltoallv Time 4.996010e-04
MPIX_Alltoallv Time 7.617561e-04
Testing Size 256
PMPI_Alltoallv Time 5.688856e-04
MPIX_Alltoallv Time 1.028282e-03
Testing Size 512
PMPI_Alltoallv Time 1.215114e-03
MPIX_Alltoallv Time 9.132279e-04
Testing Size 1024
PMPI_Alltoallv Time 1.668159e-03
MPIX_Alltoallv Time 1.661844e-03
Testing Size 2048
PMPI_Alltoallv Time 3.042503e-03
MPIX_Alltoallv Time 3.391091e-03
Testing Size 4096
PMPI_Alltoallv Time 6.055685e-03
MPIX_Alltoallv Time 6.942222e-03
Testing Size 8192
PMPI_Alltoallv Time 1.176972e-02
MPIX_Alltoallv Time 1.307528e-02
Testing Size 16384
PMPI_Alltoallv Time 2.301293e-02
MPIX_Alltoallv Time 2.577212e-02
