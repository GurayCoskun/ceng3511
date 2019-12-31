#İlhan BOZCAN 160709003
#Güray COŞKUN 160709034


import csv
import random
import math
import matplotlib.pyplot as plt

income = []
spend = []
k = int(input("Select k point (Between 1 and 10)  "))
with open('data.csv',encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    data = []
    for row in spamreader:
         data.append(row)
         income.append((row[0]))
         spend.append((row[1]))


del income[0]
del spend[0]
del data[0]

income = [int(i) for i in income]
spend = [int(i) for i in spend]

def select_k_point(x_axis,y_axis,k):
    x_axis =x_axis.copy()
    y_axis = y_axis.copy()
    x_axis.sort()
    y_axis.sort()

    points = []
    for i in range(k):
        tmp = []
        x = random.randrange(x_axis[0], x_axis[-1])
        y = random.randrange(y_axis[0], y_axis[-1])
        tmp.append(x)
        tmp.append(y)
        points.append(tmp)

    return points





points = select_k_point(income,spend,k)

point_x_axis = []
point_y_axis = []
for x in points:
    point_x_axis.append(x[0])
    point_y_axis.append(x[1])



def k_means_clustering(point_coordinate,data_coordinate,k):
    datas = [[ "" for y in range((k))]
         for x in range((k))]

    #Clear data
    for i in range(k):
        datas[i].clear()

    for coordinate in data_coordinate:

        tmp = []
        for point in point_coordinate:

            distance = (((point[0]) - (int(coordinate[0])))**2) + (((point[1]) - (int(coordinate[1])))**2)
            distance = math.sqrt(distance)
            tmp.append(distance)
            min = 99999
            min_index = 0
        #Check for minumum distance
        for index, first in enumerate(tmp):
            if first < min:
                min_index = index
                min = first

        #Check for point
        for i in range(k):
            if min_index == i:
                datas[i].append(coordinate)

    return datas


result = k_means_clustering(points, data, k)

color = ["ro","bo","go","mo","ko","co","r^","m^","g^","b^"]
x_axis = []
y_axis = []
end = k-1
for data_row in result:

    for data in data_row:
        x_axis.append(int(data[0]))
        y_axis.append(int(data[1]))

    index = random.randint(0,end)
    plt.plot(x_axis, y_axis, color[index])
    del color[index]

    x_axis.clear()
    y_axis.clear()
    end = end - 1

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'Calibri'

plt.plot(point_x_axis,point_y_axis,"y*",label="Points")
plt.xlabel("income")
plt.ylabel("spend")
plt.title("K-means clustering")
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("plot.pdf")









