#İlhan BOZCAN 160709003
#Güray COŞKUN 160709034

import math
import matplotlib.pyplot as plt
import csv


data_set = []
test_set = []


with open('train.csv',encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    for line in spamreader:
        data_set.append(line)

with open('test.csv',encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    for line in spamreader:
        test_set.append(line)

head = data_set[0]
data_set.remove(head)
test_set.remove(test_set[0])
k = int(input("Enter a neighbors number (between 1 and 999) : "))


def find_min_max(dataSet):

    min_max_final = []
    for count in range(len(head)):
        tmp = []
        min_max = []
        for data in dataSet:
            tmp.append(float(data[count]))
        tmp.sort(reverse=True)

        min_max.append(tmp[-1])
        min_max.append(tmp[0])
        min_max_final.append(min_max)

    return min_max_final


min_max_values_data = find_min_max(data_set)


min_max_values_test = find_min_max(test_set)


def normalization(dataSet,min_max_array):
    normaled = []

    for data_row in dataSet:
        tmp = []
        for index,data in enumerate(data_row):

            normal_value = ((float(data) - min_max_array[index][0]) / (min_max_array[index][1] - min_max_array[index][0]))
            tmp.append(normal_value)
        normaled.append(tmp)
    return normaled

print("Data normalizing...")
normaled_data_set =normalization(data_set,min_max_values_data)
normaled_test_set =normalization(test_set,min_max_values_test)



def euclidean_distance(dataSet,testSet):
    distance = []

    for test_row in testSet:
        tmp = []
        for data_row in dataSet:
            result = 0
            for index,data in enumerate(data_row):

                result += (float(data) - float(test_row[index]))**2

            tmp.append(math.sqrt(result))
        distance.append(tmp)
    return distance

print("Euclidean distance calculating...")
distance = euclidean_distance(normaled_data_set,normaled_test_set)




def KNN(dataSet,testSet,dist,row_index,k):
    dist_copy = dist.copy()
    neighbor = []
    for i in range(k):
        min = 99999
        min_index = 0

        for index,first in enumerate(dist_copy):
            if first < min:
                min_index = index
                min = first

        neighbor.append(dataSet[min_index])
        dist_copy[min_index] = 999999

    accuary_list = []

    for i in range(k):
        #accuary numbers array to count function
        accuary_list.append(neighbor[i][20])



    label = testSet[row_index][20]
    zero =accuary_list.count("0")
    one = accuary_list.count("1")
    two = accuary_list.count("2")
    three = accuary_list.count("3")


    #check test label

    if (zero > one) and (zero > two) and (zero > three):
        largest = 0

    elif (one > two) and (one > zero) and (one > three) :
        largest = 1

    elif (two > zero) and (two > one) and (two > three) :
        largest = 2
    elif (three > zero) and (three > one) and (three > two) :
        largest = 3

    else:
        #Short distance set label
        largest = int(neighbor[0][20])

    if label == str(largest):
        #its equal accuary+=1
        return True

    return False

k_list = []
x_axis = []
print("Calculating and ploting...")
for k_number in range(1,k+1):
    x_axis.append(k_number)
    accuary = 0
    for i in range (1000):
        if (KNN(data_set,test_set,distance[i],i,k_number)):
            accuary +=1
    k_list.append(float(accuary)/10)

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'Calibri'
f = plt.figure()
plt.xlabel("K neighbors")
plt.ylabel("Accuary (%)")
plt.plot(x_axis, k_list)
f.savefig("plot.pdf")


















