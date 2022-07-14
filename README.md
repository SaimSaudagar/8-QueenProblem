# 8-QueenProblem
Python Code For 8-Queen Problem Using Genetic Algorithm

This is the code for 8-Queen problem in which I have used genetic algorithm.

Firstly, I have generated 4 initial populations as arrays in which the ith element is the number of the row where a queen is placed and where i is the column.
I have generated unique numbers in every column to optimize it as to eliminate 2 queens in 1 row.

Then I calculated their fitness as in how many queens are not attacked by other queens and then chose the best 2 from them and applied one point crossover between them.
Then I applied swap mutation on the best from the 6 currently in hand populations and the fitness is calculated of the one generated from the mutation.

As now there are 7, so from the I took out 2 best populations from them as per their fitness.

And finally, I applied one point crossover and mutation repeatedly until solution is found.

NOTE: Every time when there are non-unique numbers in the array I made them unique to make it more optimized.

Output Sample:
First population [[2, 7, 6, 8, 1, 5, 4, 3], [6, 5, 7, 8, 2, 1, 4, 3], [2, 5, 6, 8, 3, 1, 4, 7], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [3, 0, 5, 4]

*************************************
After crossover of the best in the population [[2, 5, 6, 8, 4, 3, 1, 7], [1, 6, 4, 3, 5, 2, 8, 7]]
Their fitness [3, 0]

After mutation of the best in the population [4, 8, 6, 5, 3, 1, 2, 7]
Its fitness 3

After selection of the best in the population [[4, 8, 6, 5, 3, 1, 2, 7], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[4, 8, 6, 5, 2, 1, 3, 7], [1, 6, 4, 3, 5, 8, 2, 7]]
Their fitness [1, 3]

After mutation of the best in the population [4, 8, 1, 5, 3, 2, 6, 7]
Its fitness 3

After selection of the best in the population [[4, 8, 1, 5, 3, 2, 6, 7], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[4, 8, 1, 5, 2, 3, 6, 7], [1, 6, 4, 3, 8, 2, 5, 7]]
Their fitness [3, 3]

After mutation of the best in the population [4, 8, 2, 5, 6, 1, 3, 7]
Its fitness 1

After selection of the best in the population [[4, 8, 2, 5, 6, 1, 3, 7], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[4, 8, 2, 5, 6, 3, 1, 7], [1, 6, 4, 3, 5, 2, 8, 7]]
Their fitness [2, 0]

After mutation of the best in the population [1, 8, 2, 6, 5, 4, 3, 7]
Its fitness 0

After selection of the best in the population [[1, 8, 2, 6, 5, 4, 3, 7], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[1, 8, 2, 6, 4, 3, 5, 7], [1, 6, 4, 3, 5, 2, 8, 7]]
Their fitness [2, 0]

After mutation of the best in the population [1, 8, 6, 4, 5, 2, 3, 7]
Its fitness 2

After selection of the best in the population [[1, 8, 6, 4, 5, 2, 3, 7], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[1, 8, 6, 4, 2, 3, 5, 7], [1, 6, 4, 3, 5, 2, 8, 7]]
Their fitness [3, 0]

After mutation of the best in the population [5, 8, 6, 1, 4, 2, 3, 7]
Its fitness 2

After selection of the best in the population [[5, 8, 6, 1, 4, 2, 3, 7], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[5, 8, 6, 1, 2, 3, 4, 7], [1, 6, 4, 3, 8, 2, 5, 7]]
Their fitness [3, 3]

After mutation of the best in the population [5, 8, 1, 6, 4, 7, 3, 2]
Its fitness 4

After selection of the best in the population [[5, 8, 1, 6, 4, 7, 3, 2], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[5, 8, 1, 6, 2, 3, 4, 7], [1, 6, 4, 3, 5, 7, 8, 2]]
Their fitness [3, 1]

After mutation of the best in the population [1, 8, 6, 5, 4, 7, 3, 2]
Its fitness 1

After selection of the best in the population [[1, 8, 6, 5, 4, 7, 3, 2], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[1, 8, 6, 5, 2, 4, 3, 7], [1, 6, 4, 3, 8, 7, 5, 2]]
Their fitness [3, 4]

After mutation of the best in the population [1, 2, 6, 4, 5, 7, 3, 8]
Its fitness 2

After selection of the best in the population [[1, 2, 6, 4, 5, 7, 3, 8], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[1, 2, 6, 4, 3, 8, 5, 7], [1, 6, 4, 3, 5, 7, 2, 8]]
Their fitness [3, 2]

After mutation of the best in the population [5, 6, 2, 4, 1, 7, 3, 8]
Its fitness 2

After selection of the best in the population [[5, 6, 2, 4, 1, 7, 3, 8], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[5, 6, 2, 4, 3, 8, 1, 7], [1, 6, 4, 3, 2, 7, 5, 8]]
Their fitness [1, 2]

After mutation of the best in the population [5, 6, 3, 7, 1, 4, 2, 8]
Its fitness 3

After selection of the best in the population [[5, 6, 3, 7, 1, 4, 2, 8], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[5, 6, 3, 7, 2, 8, 4, 1], [1, 6, 4, 3, 5, 7, 2, 8]]
Their fitness [2, 2]

After mutation of the best in the population [5, 6, 7, 2, 1, 4, 3, 8]
Its fitness 1

After selection of the best in the population [[5, 6, 7, 2, 1, 4, 3, 8], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[5, 6, 7, 2, 1, 8, 3, 4], [1, 6, 4, 3, 5, 7, 2, 8]]
Their fitness [1, 2]

After mutation of the best in the population [2, 5, 7, 6, 1, 4, 3, 8]
Its fitness 3

After selection of the best in the population [[2, 5, 7, 6, 1, 4, 3, 8], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[2, 5, 7, 6, 1, 8, 3, 4], [1, 6, 4, 3, 5, 2, 7, 8]]
Their fitness [2, 0]

After mutation of the best in the population [2, 5, 7, 1, 6, 3, 4, 8]
Its fitness 3

After selection of the best in the population [[2, 5, 7, 1, 6, 3, 4, 8], [1, 6, 4, 3, 2, 8, 5, 7]]
Their fitness [5, 4]
*************************************

*************************************
After crossover of the best in the population [[2, 5, 7, 1, 6, 8, 4, 3], [1, 6, 4, 3, 5, 7, 2, 8]]
Their fitness [3, 2]

After mutation of the best in the population [3, 5, 7, 1, 6, 4, 2, 8]
Its fitness 6

After selection of the best in the population [[3, 5, 7, 1, 6, 4, 2, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 5]
*************************************

*************************************
After crossover of the best in the population [[3, 5, 7, 1, 6, 4, 2, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]

After mutation of the best in the population [5, 3, 7, 1, 8, 4, 2, 6]
Its fitness 2

After selection of the best in the population [[5, 3, 7, 1, 8, 4, 2, 6], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 3, 7, 1, 6, 4, 2, 8], [3, 5, 7, 1, 8, 4, 2, 6]]
Their fitness [2, 3]

After mutation of the best in the population [5, 1, 7, 6, 8, 4, 2, 3]
Its fitness 2

After selection of the best in the population [[5, 1, 7, 6, 8, 4, 2, 3], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 1, 7, 6, 3, 4, 2, 8], [3, 5, 7, 1, 8, 4, 2, 6]]
Their fitness [3, 3]

After mutation of the best in the population [5, 2, 7, 6, 3, 4, 1, 8]
Its fitness 0

After selection of the best in the population [[5, 2, 7, 6, 3, 4, 1, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 2, 7, 6, 1, 4, 3, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [0, 6]

After mutation of the best in the population [5, 7, 1, 6, 3, 4, 2, 8]
Its fitness 2

After selection of the best in the population [[5, 7, 1, 6, 3, 4, 2, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 7, 1, 6, 3, 4, 2, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [2, 6]

After mutation of the best in the population [5, 4, 1, 7, 3, 6, 2, 8]
Its fitness 2

After selection of the best in the population [[5, 4, 1, 7, 3, 6, 2, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 4, 1, 7, 6, 3, 2, 8], [3, 5, 7, 1, 4, 6, 2, 8]]
Their fitness [2, 4]

After mutation of the best in the population [1, 4, 8, 7, 3, 6, 2, 5]
Its fitness 4

After selection of the best in the population [[1, 4, 8, 7, 3, 6, 2, 5], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[1, 4, 8, 7, 6, 5, 2, 3], [3, 5, 7, 1, 4, 6, 2, 8]]
Their fitness [2, 4]

After mutation of the best in the population [6, 8, 4, 7, 3, 1, 2, 5]
Its fitness 4

After selection of the best in the population [[6, 8, 4, 7, 3, 1, 2, 5], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[6, 8, 4, 7, 3, 1, 2, 5], [3, 5, 7, 1, 4, 6, 2, 8]]
Their fitness [4, 4]

After mutation of the best in the population [6, 3, 4, 5, 8, 1, 2, 7]
Its fitness 2

After selection of the best in the population [[6, 3, 4, 5, 8, 1, 2, 7], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[6, 3, 4, 5, 1, 7, 2, 8], [3, 5, 7, 1, 8, 6, 2, 4]]
Their fitness [2, 4]

After mutation of the best in the population [6, 3, 2, 5, 1, 8, 4, 7]
Its fitness 4

After selection of the best in the population [[6, 3, 2, 5, 1, 8, 4, 7], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[6, 3, 2, 5, 1, 4, 7, 8], [3, 5, 7, 1, 6, 8, 4, 2]]
Their fitness [3, 1]

After mutation of the best in the population [6, 1, 2, 5, 4, 8, 3, 7]
Its fitness 3

After selection of the best in the population [[6, 1, 2, 5, 4, 8, 3, 7], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[6, 1, 2, 5, 3, 4, 7, 8], [3, 5, 7, 1, 4, 8, 2, 6]]
Their fitness [2, 3]

After mutation of the best in the population [4, 1, 2, 3, 6, 8, 5, 7]
Its fitness 3

After selection of the best in the population [[4, 1, 2, 3, 6, 8, 5, 7], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[4, 1, 2, 3, 6, 7, 5, 8], [3, 5, 7, 1, 6, 8, 2, 4]]
Their fitness [2, 6]

After mutation of the best in the population [4, 5, 3, 2, 6, 8, 1, 7]
Its fitness 4

After selection of the best in the population [[4, 5, 3, 2, 6, 8, 1, 7], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[4, 5, 3, 2, 6, 7, 1, 8], [3, 5, 7, 1, 6, 8, 4, 2]]
Their fitness [1, 1]

After mutation of the best in the population [4, 5, 7, 2, 6, 8, 3, 1]
Its fitness 4

After selection of the best in the population [[4, 5, 7, 2, 6, 8, 3, 1], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[4, 5, 7, 2, 6, 3, 1, 8], [3, 5, 7, 1, 6, 8, 4, 2]]
Their fitness [6, 1]

After mutation of the best in the population [4, 5, 3, 2, 6, 8, 1, 7]
Its fitness 4

After selection of the best in the population [[4, 5, 3, 2, 6, 8, 1, 7], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[4, 5, 3, 2, 6, 1, 7, 8], [3, 5, 7, 1, 6, 8, 2, 4]]
Their fitness [1, 6]

After mutation of the best in the population [4, 5, 3, 6, 8, 2, 1, 7]
Its fitness 3

After selection of the best in the population [[4, 5, 3, 6, 8, 2, 1, 7], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[4, 5, 3, 6, 7, 1, 2, 8], [3, 5, 7, 1, 8, 2, 4, 6]]
Their fitness [0, 4]

After mutation of the best in the population [5, 7, 3, 6, 8, 2, 1, 4]
Its fitness 3

After selection of the best in the population [[5, 7, 3, 6, 8, 2, 1, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 7, 3, 6, 1, 4, 2, 8], [3, 5, 7, 1, 8, 2, 6, 4]]
Their fitness [0, 3]

After mutation of the best in the population [5, 7, 1, 6, 8, 3, 2, 4]
Its fitness 5

After selection of the best in the population [[5, 7, 1, 6, 8, 3, 2, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 7, 1, 6, 3, 4, 2, 8], [3, 5, 7, 1, 8, 6, 2, 4]]
Their fitness [2, 4]

After mutation of the best in the population [5, 7, 1, 3, 6, 8, 2, 4]
Its fitness 6

After selection of the best in the population [[5, 7, 1, 3, 6, 8, 2, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[5, 7, 1, 3, 6, 4, 2, 8], [3, 5, 7, 1, 6, 8, 2, 4]]
Their fitness [4, 6]

After mutation of the best in the population [8, 7, 1, 3, 6, 4, 2, 5]
Its fitness 3

After selection of the best in the population [[8, 7, 1, 3, 6, 4, 2, 5], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 7, 1, 3, 6, 4, 2, 5], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [3, 6]

After mutation of the best in the population [8, 7, 1, 3, 6, 4, 2, 5]
Its fitness 3

After selection of the best in the population [[8, 7, 1, 3, 6, 4, 2, 5], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 7, 1, 3, 6, 4, 2, 5], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [3, 6]

After mutation of the best in the population [1, 7, 5, 3, 6, 4, 2, 8]
Its fitness 4

After selection of the best in the population [[1, 7, 5, 3, 6, 4, 2, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[1, 7, 5, 3, 6, 4, 2, 8], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [4, 6]

After mutation of the best in the population [8, 7, 3, 5, 6, 4, 2, 1]
Its fitness 2

After selection of the best in the population [[8, 7, 3, 5, 6, 4, 2, 1], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 7, 3, 5, 6, 4, 2, 1], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [2, 6]

After mutation of the best in the population [8, 7, 2, 5, 1, 4, 3, 6]
Its fitness 1

After selection of the best in the population [[8, 7, 2, 5, 1, 4, 3, 6], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 7, 2, 5, 6, 4, 1, 3], [3, 5, 7, 1, 8, 4, 2, 6]]
Their fitness [3, 3]

After mutation of the best in the population [8, 1, 2, 3, 7, 4, 5, 6]
Its fitness 1

After selection of the best in the population [[8, 1, 2, 3, 7, 4, 5, 6], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 1, 2, 3, 6, 4, 5, 7], [3, 5, 7, 1, 8, 4, 2, 6]]
Their fitness [2, 3]

After mutation of the best in the population [7, 4, 2, 3, 8, 1, 5, 6]
Its fitness 3

After selection of the best in the population [[7, 4, 2, 3, 8, 1, 5, 6], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[7, 4, 2, 3, 6, 5, 1, 8], [3, 5, 7, 1, 8, 4, 2, 6]]
Their fitness [2, 3]

After mutation of the best in the population [7, 4, 3, 2, 8, 5, 1, 6]
Its fitness 2

After selection of the best in the population [[7, 4, 3, 2, 8, 5, 1, 6], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[7, 4, 3, 2, 6, 5, 1, 8], [3, 5, 7, 1, 8, 2, 4, 6]]
Their fitness [0, 4]

After mutation of the best in the population [7, 5, 3, 2, 8, 6, 1, 4]
Its fitness 0

After selection of the best in the population [[7, 5, 3, 2, 8, 6, 1, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[7, 5, 3, 2, 6, 4, 1, 8], [3, 5, 7, 1, 8, 6, 2, 4]]
Their fitness [2, 4]

After mutation of the best in the population [7, 2, 6, 5, 8, 3, 1, 4]
Its fitness 2

After selection of the best in the population [[7, 2, 6, 5, 8, 3, 1, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[7, 2, 6, 5, 3, 4, 1, 8], [3, 5, 7, 1, 8, 6, 2, 4]]
Their fitness [0, 4]

After mutation of the best in the population [7, 1, 6, 5, 2, 3, 8, 4]
Its fitness 3

After selection of the best in the population [[7, 1, 6, 5, 2, 3, 8, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[7, 1, 6, 5, 3, 4, 2, 8], [3, 5, 7, 1, 2, 6, 8, 4]]
Their fitness [2, 3]

After mutation of the best in the population [8, 1, 6, 3, 2, 5, 7, 4]
Its fitness 2

After selection of the best in the population [[8, 1, 6, 3, 2, 5, 7, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 1, 6, 3, 5, 4, 2, 7], [3, 5, 7, 1, 2, 8, 6, 4]]
Their fitness [0, 3]

After mutation of the best in the population [8, 1, 6, 3, 2, 5, 7, 4]
Its fitness 2

After selection of the best in the population [[8, 1, 6, 3, 2, 5, 7, 4], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 1, 6, 3, 7, 4, 2, 5], [3, 5, 7, 1, 2, 6, 8, 4]]
Their fitness [3, 3]

After mutation of the best in the population [8, 1, 2, 3, 4, 5, 7, 6]
Its fitness 0

After selection of the best in the population [[8, 1, 2, 3, 4, 5, 7, 6], [3, 5, 7, 1, 6, 4, 2, 8]]
Their fitness [6, 6]
*************************************

*************************************
After crossover of the best in the population [[8, 1, 2, 3, 6, 4, 7, 5], [3, 5, 7, 1, 4, 2, 8, 6]]
Their fitness [5, 8]

The solution to the 8 queen problem is [3, 5, 7, 1, 4, 2, 8, 6]
[[0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0.]]
Solution found after 48 iterations
