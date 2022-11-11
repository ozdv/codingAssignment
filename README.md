# Prime Number Generation Benchmark

This code will take in a positive integer n as an input and generate a list of prime numbers less than or equal to n.
It will then output the the execution time it takes to generate the lists using two methods of generation: The typical Brute force method, and the more efficient, Sieve of Eratosthenes method.

## Running the Code

Simply clone the repo, navigate to the directory in a terminal, and run `python3 main.py`. You will then be prompted to enter an integer value, so enter any integer greater than 1 and hit `enter`.

To run the unit tests, simply run `python3 -m unittest test_main.py`

### Is there any measurable difference between the two algorithms for small values of N?

For small integer values, the difference is in miliseconds. However as you get into the hundreds of thousands or millions, the difference is exponential.

### Approximately at what value of N, if any, does the performance gap become significant?

For instance at 100,000 the execution time on my machine is aprox 0.03 seconds for Sieve, while 0.16 seconds for brute force. Although both are under a second, sieve is over 4x faster. While for a max of 1,000,000 it is over 10x faster!

The time complexity of Sieve of Eratosthenes is O(n log log n) which is much more efficient for larger value n's than my brute force algorithm of O(n^2)

### Do you think it was a good idea to benchmark the two algorithms in parallel? Why or why not?

With multithreading, we can give each function control over the interpreter at any point in time due to GIL. Although the threads are not truly running simultaneously, they are taking turns running to achieve concurrency. As a result, I think it is not ideal in this case as it can hinder one another's performance. Multiprocessing would be a more ideal approach as you can give each algorithm it's own CPU core.

### In general, does it always make sense to use the algorithms with the best Big O performance in our code?

For the most part yes. It is all dependent on the use case, for instance searching a database, sorting data, etc. are all very intensive processes which can be drastically increased by having more efficient algorithms. Sure, if the data being worked with only has 10 rows then the difference is negligible, but as data scales up, so to will the runtime of each operation.

### Describe some scenarios where it could make sense to choose a slower algorithm.

If the value of N is known, then you can evaluate the worst-case time complexity. For instance, insertion sort is faster than quick sort for inputs less than around 9000 due to the recursive approach.
