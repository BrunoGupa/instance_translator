import networkx as nx
import movingfp.gen as mfp
import copy
from gens_for_paper import get_seed
import numpy as np


def get_path(path):
    solution = []
    # Append the first defended node
    solution.append(path[0][0])
    for item in path:
        if solution[-1] != item[0]:
            solution.append(item[0])
    return solution


def verify(n, burnt_nodes, A, distance, path, node_list=None, instances=None):


    solution = get_path(path)

    burned = burnt_nodes
    G = nx.Graph()

    for i in range(n + 1):
        G.add_node(i)

    for i in range(n):
        for j in range(n):
            if A[i][j] == 1:
                G.add_edge(i, j)

    nx.draw(G)
    mov = distance.tolist()


    ordered_list = []
    for i in range(len(mov)):
        for j in range(len(mov[i])):
            if mov[i][j] != 0:
                ordered_list.append(mov[i][j])
    ordered_list.sort()

    sum_less_than_one = True
    sumation = 0
    i = 0
    while sum_less_than_one:
        sumation = sumation + ordered_list[i]
        i += 1
        if sumation < 1:
            sum_less_than_one = True
        else:
            sum_less_than_one = False

    # D = i-1 # rondas de defensa

    process_finished = False
    first_time_here = True

    i = 1
    while not process_finished:
        # for i in range(1,B+1):
        # print("-----------------------------")
        # print("burn round: " + str(i))
        defended = []
        sumation = 0
        j = -1
        while sumation <= i and j + 2 < len(solution):
            j += 1
            sumation += mov[solution[j]][solution[j + 1]]
        if sumation > i:
            sumation -= mov[solution[j]][solution[j + 1]]
        else:
            j += 1
        if sumation < i - 1:
            # it means that there was a hole burning round without defending a node
            new_defended = False
        else:
            new_defended = True
        # print("a: " + str(sumation))
        for k in range(j + 1):
            defended.append(solution[k])
        # print("defended")
        # print(defended)

        for v in range(n):
            for d in defended:
                if (v, d) in G.edges():
                    G.remove_edge(v, d)
        new_burned = copy.deepcopy(burned)
        for v in range(n):
            for b in burned:
                if (v, b) in G.edges():
                    new_burned.add(v)
        if len(new_burned) == len(burned):
            if first_time_here:
                first_time_here = False
                B_veri = i - 1
            if not new_defended:
                # The process is finished
                process_finished = True

        burned = copy.deepcopy(new_burned)
        # print("burned")
        # print(burned)
        # print("burned_size: ", len(burned))
        i += 1

    return defended, len(burned), B_veri

