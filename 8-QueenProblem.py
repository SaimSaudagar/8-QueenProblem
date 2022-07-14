import sys
from random import random
import numpy as np

def fitness(par = []):
    board = np.zeros((8, 8))
    fit = 0

    for i in range(8):
        board[par[i] - 1][i] = 1

    for i in range(8):
        found1 = True
        value = par[i] - 1

        for j in range(i + 1, 8):
            if(value + 1 == 8):
                found1 = True
                break
            else:
                if(board[value + 1][j] == 1):
                    found1 = False
                    break
            value += 1

        found2 = True
        value = par[i] - 1

        for j in range(i - 1, -1, -1):
            if(value - 1 == -1):
                found2 = True
                break
            else:
                if(board[value - 1][j] == 1):
                    found2 = False
                    break
            value -= 1

        found3 = True
        value = par[i] - 1

        for j in range(i + 1, 8):
            if(value - 1 == -1):
                found3 = True
                break
            else:
                if(board[value - 1][j] == 1):
                    found3 = False
                    break
            value -= 1

        found4 = True
        value = par[i] - 1

        for j in range(i - 1, -1, -1):
            if(value + 1 == 8):
                found4 = True
                break
            else:
                if(board[value + 1][j] == 1):
                    found4 = False
                    break
            value += 1

        if found1 == True & found2 == True & found3 == True & found4 == True:
            fit += 1

    return fit

def crossover(par1 = [], par2 = []):
    child1 = par1[0:4] + par2[4:]
    for i in range(8):
        for j in range(i + 1, 8):
            if child1[i] == child1[j]:
                while child1[i] == child1[j]:
                    ran = int(random() * 8) + 1
                    if ((ran not in child1) & (ran != child1[i])):
                        child1[j] = ran

    child2 = par2[0:4] + par1[4:]
    for i in range(8):
        for j in range(i + 1, 8):
            if child2[i] == child2[j]:
                while child2[i] == child2[j]:
                    ran = int(random() * 8) + 1
                    if ((ran not in child2) & (ran != child2[i])):
                        child2[j] = ran
    lst = [child1, child2]

    return lst

def mutation(par = []):
    out = par

    for i in range(2):
        ran = 0
        ran2 = 0
        while(ran == ran2):
            ran = int(random() * 8)
            ran2 = int(random() * 8)

        temp = out[ran]
        out[ran] = out[ran2]
        out[ran2] = temp

    return out


population = []

for j in range(4):
    par = []
    for i in range(1000):
        value = int(random() * 8) + 1
        if value not in par:
            par.append(value)
        if(len(par) == 8):
            break
    population.append(par)

fit = []

for i in range(4):
    fit.append(fitness(population[i]))

    if fit[i] == 8:
        board = np.zeros((8, 8))
        par = population[fit.index(max(fit))]

        for i in range(8):
            board[par[i] - 1][i] = 1

        print("Solution to the 8 queen problem is " + str(population[i]))
        print(board)
        print("Solution found in the first population")
        sys.exit(0)

print("First population " + str(population))
print("Their fitness " + str(fit))
print()

#     print(population[i])
#     print(fit[i])
#     print()
#
# print(population)
# print(fit)
# print()

index = fit.index(max(fit))
tempfit = fit.pop(index)
temppopulation = population.pop(index)

index = fit.index(max(fit))
tempfit2 = fit.pop(index)
temppopulation2 = population.pop(index)

population = [temppopulation, temppopulation2]
fit = [tempfit, tempfit2]

if max(fit) == 8:
    board = np.zeros((8, 8))
    par = population[fit.index(max(fit))]

    for i in range(8):
        board[par[i] - 1][i] = 1

    print("The solution to the 8 queen problem is " + str(population[fit.index(max(fit))]))
    print(board)
    print("Solution found in the first population")
    sys.exit(0)

count = 0

while True:
    CO = crossover(temppopulation, temppopulation2)
    fitco = [fitness(CO[0]), fitness(CO[1])]

    print("*************************************")
    print("After crossover of the best in the population " + str(CO))
    print("Their fitness " + str(fitco))
    print()

    population.append(CO[0])
    population.append(CO[1])
    fit.append(fitco[0])
    fit.append(fitco[1])

    # print(population)
    # print(fit)
    # print("====================")

    index = fit.index(max(fit))
    tempfit = fit.pop(index)
    temppopulation = population.pop(index)

    index = fit.index(max(fit))
    tempfit2 = fit.pop(index)
    temppopulation2 = population.pop(index)

    population = [temppopulation, temppopulation2]
    fit = [tempfit, tempfit2]

    if max(fit) == 8:
        board = np.zeros((8, 8))
        par = population[fit.index(max(fit))]

        for i in range(8):
            board[par[i] - 1][i] = 1

        print("The solution to the 8 queen problem is " + str(population[fit.index(max(fit))]))
        print(board)
        count = count + 1
        print("Solution found after " + str(count) + " iterations")
        sys.exit(0)

    # print(str(CO) + " Crossover")
    # print()
    #
    # print(population)
    # print(fit)
    # print()

    # print(population[fit.index(max(fit))])
    mut = mutation(population[fit.index(max(fit))])
    # print(str(mut) + " Mutation")
    #
    # print(population)
    # print(fit)
    # print()

    population.append(mut)
    fit.append(fitness(mut))

    print("After mutation of the best in the population " + str(mut))
    print("Its fitness " + str(fitness(mut)))
    print()
    # print(population)
    # print(fit)
    # print()

    if max(fit) == 8:
        board = np.zeros((8, 8))
        par = population[fit.index(max(fit))]

        for i in range(8):
            board[par[i] - 1][i] = 1

        print("The solution to the 8 queen problem is " + str(population[fit.index(max(fit))]))
        print(board)
        count += 1
        print("Solution found after " + str(count) + " iterations")
        sys.exit(0)

    index = fit.index(max(fit))
    tempfit = fit.pop(index)
    temppopulation = population.pop(index)

    index = fit.index(max(fit))
    tempfit2 = fit.pop(index)
    temppopulation2 = population.pop(index)

    population = [temppopulation, temppopulation2]
    fit = [tempfit, tempfit2]

    print("After selection of the best in the population " + str(population))
    print("Their fitness " + str(fit))
    print("*************************************")
    print()

    if max(fit) == 8:
        board = np.zeros((8, 8))
        par = population[fit.index(max(fit))]

        for i in range(8):
            board[par[i] - 1][i] = 1

        print("The solution to the 8 queen problem is " + str(population[fit.index(max(fit))]))
        print(board)
        count += 1
        print("Solution found after " + str(count) + " iterations")
        sys.exit(0)

    count = count + 1
    # print()
    # print(population)
    # print(fit)