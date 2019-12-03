import random
import matplotlib.pyplot as plt

from pip._vendor.msgpack.fallback import xrange

fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')

c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)
upper_limit = 1;
lower_limit = 0;
popSize = int(input('Size of population : '))
genNumber = int(input('Max number of generation : '))

global nextGeneretion
population = []
for i in range(popSize):
    temp = []
    for j in range(len(w)):
        temp.append(random.randint(0, 1))
    population.append(temp)

print('evaluating fitnesses')
age = []
for i in range(len(population)):
    age.insert(i, 0)
print(age)


def calculate_weight(population):
    total_fit = 0
    fitness_weight = []
    value = []
    weight = []
    for i, chrom in enumerate(population):
        ft = 0
        wt = 0
        for j, gene in enumerate(chrom):
            ft += gene * v[j]
            wt += gene * w[j]
            if wt > c:
                ft = 0
        value.append(ft)
        weight.append(wt)
        total_fit = total_fit + ft
        print(i + 1, chrom, ft, wt)
    fitness_weight.append(value)
    fitness_weight.append(weight)
    return fitness_weight


def FitnessCalculate(population):
    fitness = []
    popNew = calculate_weight(population)
    weight = popNew[1]
    value = popNew[0]

    for index, i in enumerate(weight):
        if (i > c):
            fitness_value = 0
            fitness.append(fitness_value)
        else:
            fitness_value = value[index]
            fitness.append(fitness_value)

    return fitness


fitness_weight = calculate_weight(population)
print(fitness_weight)
print('\nParent Selection\n---------------------------')
parentSelection = int(input('Which one? '))
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')


def get_probability_list():
    for f in fitness_weight:
        fitness = fitness_weight[0]
    total_fit = float(sum(fitness))
    relative_fitness = [f / total_fit for f in fitness]
    probabilities = [sum(relative_fitness[:i + 1])
                     for i in range(len(relative_fitness))]
    return probabilities


probablities = get_probability_list()
parent = []


def roulette_wheel_pop(population, probabilities, number):
    choosen = []
    for n in xrange(number):
        r = random.random()
        for (i, individual) in enumerate(population):
            if r <= probabilities[i]:
                choosen.append(list(individual))
                break
    print(choosen)
    return choosen


if parentSelection == 1:
    parent = roulette_wheel_pop(population, probablities, 2)
    first_child = []
    second_child = []
    for x in parent[0]:
        first_child.append(x)
    for y in parent[1]:
        second_child.append(y)


def tournamentSelection():
    choosen = []
    first = []
    fitness_values = []

    for x in fitness_weight[0]:
        fitness_values.append(x)

    for h in xrange(2):
        k = int(input("What will be size of tournament?"))
        for x in xrange(k):
            a = random.randint(0, len(fitness_values) - 1)
            first.append(fitness_values[a])
        max = 0
        for k in xrange(len(first)):
            if first[k] > max:
                max = first[k]

        for (i, individual) in enumerate(fitness_values):
            if fitness_values[i] == max:
                choosen.append(population[i])
                fitness_values.remove(individual)
                first.clear()
    print(choosen)

    return choosen


if parentSelection == 2:
    parent = tournamentSelection()
    first_child = []
    second_child = []
    for x in parent[0]:
        first_child.append(x)
    for y in parent[1]:
        second_child.append(y)


def nPointCrossover(n, parent):
    for index, value in enumerate(age):
        age[index] = value + 1
    part1 = []
    part2 = []
    for x in parent[0]:
        part1.append(x)
    for y in parent[1]:
        part2.append(y)

    for i in range(n, len(part1)):
        part1[i], part2[i] = part2[i], part1[i]
    print("first" + str(part1))
    print("second" + str(part2))

    return part1, part2


print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))
nPointCrossover(n, parent)


def mutation(population, mutProb):
    mutationPoint = random.randrange(0, 15)
    randMutation = random.randrange(0, len(population))
    selectedChrom = population[randMutation]
    a = random.random()
    if mutProb > a:
        if selectedChrom[mutationPoint] == 1:
            selectedChrom[mutationPoint] = 0
        else:
            selectedChrom[mutationPoint] = 1
    for i in xrange(len(population)):
        population[randMutation] = selectedChrom

    print(population[randMutation])

    return population


print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))
mutation(population, mutProb)
print('\nSurvival Selection\n---------------------------')


def fitnessSelection(generetion):
    for index, value in enumerate(age):
        age[index] = value + 1
    fitness_values = []
    for x in fitness_weight[0]:
        fitness_values.append(x)
    secondmin = fitness_values[0]
    min = fitness_values[0]

    for i in xrange(len(fitness_values)):
        if fitness_values[i] < min:
            secondmin = min
            min = fitness_values[i]
        elif secondmin == min:
            secondmin = fitness_values[i]
        elif secondmin > fitness_values[i]:
            secondmin = fitness_values[i]
    for (i, individual) in enumerate(fitness_values):
        if fitness_values[i] == min:
            generetion[i] = first_child
        elif fitness_values[i] == secondmin:
            generetion[i] = second_child
    print(min )
    print(secondmin)
    print(generetion)
    return generetion


def age_based_selection(pop, parent):
    # if there ara chromosomes which has the same age,we delete randomly.
    for index, value in enumerate(age):
        age[index] = value + 1
    a = random.randint(0, len(pop))
    for i in range(2):
        max_index = 0
        max = 0
        for index, first in enumerate(age):
            if first > max:
                max_index = index
                max = first

        pop[max_index] = parent[i]
        age[max_index] = 0

    return pop


print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
if survivalSelection == 1:
    age_based_selection(population, parent)
if survivalSelection == 2:
    fitnessSelection(population)

elitism = bool(input('Elitism? (Y or N) '))


def elitism_cal(pop, nextPop):
    k_chrom_value_pop = FitnessCalculate(pop)
    k_chrom_value_nextPop = FitnessCalculate(nextPop)

    # Worst value next pop
    min_index = 0
    min = 99999
    for index, first in enumerate(k_chrom_value_nextPop):
        if first < min:
            min_index = index
            min = first

    # Best value pop
    max_index = 0
    max = 0
    for index, first in enumerate(k_chrom_value_pop):
        if first > max:
            max_index = index
            max = first

    nextPop[min_index] = pop[max_index]
    age[max_index] = 0

    return nextPop


print('\n----------------------------------------------------------')
print('initalizing population')

##################################################################


plot_value_list = []
plot_generation_list = []
while (x < genNumber):
    pop_copy = population.copy()
    if parentSelection == 2:
        parent = tournamentSelection()
    else:
        parent = roulette_wheel_pop(population, probablities, 2)

    crossover_parent = nPointCrossover(n, parent)
    population = mutation(population, mutProb)
    if survivalSelection == 2:
        population = fitnessSelection(population)
    else:
        population = age_based_selection(population, crossover_parent)

    if elitism == "Y":
        population = elitism_cal(pop_copy, population)
    x += 1
    plot_generation_list += [x]

    values = FitnessCalculate(population)
    max_index = 0
    max = 0
    for index, first in enumerate(values):
        if first > max:
            max_index = index
            max = first

    value = str(max)
    plot_value_list += [value]

weight = calculate_weight(population)
values = FitnessCalculate(population)
max_index = 0
max = 0
for index, first in enumerate(values):
    if first > max:
        max_index = index
        max = first
chromosome = str(population[max_index])
value = str(max)
weight = str(weight[1][max_index])

fout.write('chromosome:' + chromosome + '\n')
fout.write('weight:' + weight + '\n')
fout.write('value:' + value)
fout.close()
plt.xlabel("Generation")
plt.ylabel("Best Value")
plt.title("Knapsack Problem")

# Convert integer to sort by value in y-axis
plot_value_list = [int(i) for i in plot_value_list]
plt.plot(plot_generation_list, plot_value_list)

plt.show()