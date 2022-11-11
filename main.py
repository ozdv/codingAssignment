# Please complete this assignment by Friday, November 11 11:59 MDT.
# If you have any further questions do not hesitate to contact me.

# Benchmarking Prime Number Generators

# You are building a software application that requires you to generate a list of all prime numbers
# less than or equal to a max value (N).

# You do some google searching and find two algorithms for generating primes:
    # Sieve of Eratosthenes https://www.baeldung.com/cs/prime-number-algorithms#sieve-of-eratosthenes
    # Brute force method (Iterate over all numbers in range N and test if each is prime)

# Write a small program to benchmark the performance (execution time) of the two different algorithms to
# help you decide which to use in your application.

# Your program should accept the max value, N, as a command line argument,
# and run benchmark tests for each algorithm in parallel.
# For example, if your program is written in Java the Sieve of Eratosthenes testing should run in one thread,
# and the Brute Force testing should run concurrently in a separate thread.
# Finally, your program should report the results of the benchmarking to the screen and exit.
# At a minimum the measured execution time of each algorithm should be printed.

# Follow-up Questions:
    # Is there any measurable difference between the two algorithms for small values of N?
    # Approximately at what value of N, if any, does the performance gap become significant?
    # Do you think it was a good idea to benchmark the two algorithms in parallel? Why or why not?
    # In general, does it always make sense to use the algorithms with the best Big O performance in our code?
    # Describe some scenarios where it could make sense to choose a slower algorithm.

# We are looking for you to:
    # Use unit tests to show the correctness of your implementation
    # Add any applicable documentation
    # Note any assumptions that you make
    # Include instructions on how to run your program
    # Use git for version control

# Please craft a solution that:
    # Is written in Java or Python
    # You would consider to be representative of your level of professionalism
    # Does not copy code directly from the internet. Everyone has a unique coding style and we want to see yours.
    # Please submit a git repo with your solution & answers to the follow-up questions. Gitlab/Github is fine.

############################################################################################################################
