import sys
import queue as Q
from queue import PriorityQueue

graph_txt = open("graph.txt", "r")
graph = {}
adjacents = {}
def fill_edge(row):
    key_indis = 3
    value_indis = 5
    edge = {}
    adjacent = []
    while value_indis < len(row) :
        if int(row[value_indis]) != 0:
            edge[row[key_indis]]= int(row[value_indis])
        key_indis += 5
        value_indis +=5
    add_edge(row[0], edge)
    for key, value in edge.items():
        if value != 0:
            adjacent.append(key)
    add_adjacent(row[0], adjacent)

def add_edge(i,edge):
    graph[i] = edge

def add_adjacent(i,adjacent):
    adjacents[i] = adjacent
for row in graph_txt:
    fill_edge(list(row))


def bfs(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

def DFS(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if (vertex == goal):
                return path
            visited.add(vertex)
            for neighbor in sorted(graph[vertex], reverse=True):
                stack.append((neighbor[0], path + [neighbor[0]]))

def ucs(graph, start, goal):

    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if goal in node[1]:
            # print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            return node[1]
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))

start = input("Please enter the start state : ").capitalize()
if start  not in graph:
    print("There is no "+start+" !")
else:
    goal = input("Please enter the goal state : ").capitalize()

    if  goal not in graph:
        print("There is no "+goal+" !")
    elif goal ==start:
        print("You're already at "+goal)
    else:

        bfs_list = bfs(adjacents,start,goal)
        strBfs = ''.join(str(str1) for str1 in bfs_list)
        print("BFS : ", end="")
        print(*strBfs, sep=" - ")

        dfs_list = DFS(adjacents, start,goal)
        strDfs = ''.join((str2) for str2 in dfs_list)
        print("DFS : ", end="")
        print(*strDfs, sep=" - ")

        ucse=ucs(graph, start, goal)
        print("UCS :", (" - ").join(ucse))

