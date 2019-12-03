-Knapsack algorithm is an algorithm based on getting the most optimum efficiency from existing data (weight,values of items).

-How to run?

-STEP 1 : Users determine size of populations and maximum number of generetion.

-STEP 2 :Parent Selection ( 1 = Roulette-Wheel, 2 = K-Tournament Selection). Roulette-Wheel selection uses probabilities of chromosome about fitness value.In K-Tournament Selection, k is the number of selecting random chromose.
-After random selecting,Tournament Selection selects the chromosome that have highest fitness value.

-STEP 3 :Crossover(n-point). User determine n value.Two chromosomes swap genes each other.First gene's index is n.

-STEP 4 :Mutation(Bit-flip mutation). User determine mutation probability. I stored a random value,if mutation probability higher than the random value,population will be mutate.

-STEP 5 :Survival Selection( 1 = Age-Based, 2 = Fitness-Based). In age-based,the oldest 2 chromosomes removed from population and add two chromosomes which created after crossover.
-In Fittness-Based,Two chromosomes which has the lowest fitness values,removed from population and add two chromosomes which crated after crossover.

-STEP 6 :Elitism is  current fittest member of the population is always propagated to the next generation.Users say "yes" or "no".

-STEP 7 :Next population will be created.At the begin of program,Users could be determine number of generetion.