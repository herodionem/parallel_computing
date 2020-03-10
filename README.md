Single Instruction, Multiple Data (SIMD):
* SIMD computer consists of 'n' identical processors, each with dedicated memory
* Each processor executes the same instruction on different parts of the data
* "Data level parallelism"
* Easy to set up GPU processing with Python

Multiple Instruction, Multiple Data (MIMD):
* Usually operate asynchronously
* 'n' controllers, 'n' processors, Shared memory network and data streams
* see `static/mimd_memory_architecture.png`
* Shared vs Distributed memory
    * Shared: memory index 'i' is the same for each processor
        * see `static/shared_memory_architecture.png`
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
        * "Multi-computer"
        * Concurrency between processors' memory stores managed via messaging
        * see `static/distributed_memory_architecture.png`
        * Pros:
            * No conflicts at communication bus or switch
            * No limit to number of processors
            * No cache coherency issues (since each processor is in charge of it's own data store)
        * Cons:
            * Communication between processors requires message protocol, which
                * takes time
                * interrupts processor getting request message to deal with request
                * responsible for subdivision of data in local memories to optimize performance (huge logistical problem)

Massive Parallel Processing (MPP):
* Clusters
    * fail-over
    * load balancing
    * high-performance computing
* Shared memory model
* Miltithread model
* Distributed memory model
* Message passing model
* Parallel model

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Parallel Design:
* Task decomposition
    * Domain decomposition -> segments of data
    * Functional decomposition -> broken down into tasks
* Task assignment
    * task distribution
    * workload distribution
    * maximizing idempotence (limiting communication between tasks/processes)
* Agglomeration
    * combine smaller tasks with larger ones
    * limiting communication (comm costs - fixed and variable)
    * if tasks are too small, fixed costs could overwhelm available resources
* Mapping
    * specify optimum location for execution
    * <minimize execution time>
    * Balancing need for tasks to communicate (locality) with the ability of tasks/processes to be run concurrently
