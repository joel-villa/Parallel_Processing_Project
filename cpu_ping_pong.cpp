#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

int main(int argc, char* argv[])
{
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Status status;

    // Determine partner process
    int proc = rank + 1;
    if (rank % 2 == 1)
        proc = rank - 1;

    int msg_type = 0;

    // Loop over message sizes (2^i doubles)
    for (int i = 0; i <= 18; i++)
    {
        int n = 1 << i;     // number of doubles in this test
        double *size = (double*)malloc(n * sizeof(double));
        double *size_recv = (double*)malloc(n * sizeof(double));

        // initialize values
        for (int k = 0; k < n; k++)
            size[k] = (double)k;

        int num_iters = 1000;   // number of ping pongs
        clock_t start, end;

        // finis allocating before timing
        MPI_Barrier(MPI_COMM_WORLD);

        if (msg_type == 0)
        {
            if (rank % 2 == 0)   // even ranks send first
            {
                start = clock();
                for (int j = 0; j < num_iters; j++)
                {
                    MPI_Send(size, n, MPI_DOUBLE, proc, 1234, MPI_COMM_WORLD);
                    MPI_Recv(size_recv, n, MPI_DOUBLE, proc, 2341, MPI_COMM_WORLD, &status);
                }
                end = clock();

                double total_time = ((double)(end - start)) / CLOCKS_PER_SEC;
                double time_per_msg = total_time / (2.0 * num_iters);

                printf("Rank %d  2^%d doubles (%d bytes):  %.6e sec/message\n",
                       rank, i, (int)(n * sizeof(double)), time_per_msg);
            }
            else    // odd ranks receive first
            {
                for (int j = 0; j < num_iters; j++)
                {
                    MPI_Recv(size_recv, n, MPI_DOUBLE, proc, 1234, MPI_COMM_WORLD, &status);
                    MPI_Send(size, n, MPI_DOUBLE, proc, 2341, MPI_COMM_WORLD);
                }
            }
        }

        free(size);
        free(size_recv);
    }

    MPI_Finalize();
    return 0;
}
