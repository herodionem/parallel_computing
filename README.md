Single Instruction, Multiple Data (SIMD):
* SIMD computer consists of 'n' identical processors, each with dedicated memory
* Each processor executes the same instruction on different parts of the data
* "Data level parallelism"
* Easy to set up GPU processing with Python

Multiple Instruction, Multiple Data (MIMD):
* Usually operate asynchronously
* 'n' controllers, 'n' processors, Shared memory network and data streams
* see `./mimd_memory_architecture.png`
* Shared vs Distributed memory
    * Shared: memory index 'i' is the same for each processor
        * see `./shared_memory_architecture.png`
        * Memory management:
            * Memory consistency between processors' managed by updating processors' cache
                * "Cache Coherency"
            * Must controll access of each processor to the shared memory (i.e. only single processor at a time should have access to memory resource)
            * Memory location must not be changed
            * Sharing data is fast

        * Memory access:

            * Uniform memory access (UMA)
                * Not very scalable
                * "symmetric multi-processor"
                * Programmer responsible for management of synchronization

            * Non-Uniform memory access (NUMA)
                * Divides memory area into high-speed access assigned to each processor in a common area for the data exchange with slower access
                * "Distributed shared memory"
                * Scalable but complex

            * No remote memory access (NORMA)
                * Memory is physically distributed among processors/local memory
                * messaging protocol for coherency

            * Cache only memory access (COMA)
                * Derived from analysis of NUMA --> they kept local copies of data in cache which were also stored in main memory.
                * COMA removes duplicates and keeps only cache memories

    * Distributed: 'i' is a local address
        * Concurrency between processors' memory stores managed via messaging
        * see `./distributed_memory_architecture.png`
