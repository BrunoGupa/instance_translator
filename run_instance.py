from recursive_function import find_B_suf
from get_D_value import start_recursion
from network_grid import adjency
from bulldozer_to_MFP import distance_matrix
import numpy as np

instance_name = "ahuev"

nodes = 40 # including the anchor point
n_list = [39]

move_values = {
    0: {"T_MOVE": 0.025, "T_SHOOT": 0.1, "T_ANY": 0.025},
    1: {"T_MOVE": 0.05, "T_SHOOT": 0.3, "T_ANY": 0.05},
    2: {"T_MOVE": 0.1, "T_SHOOT": 0.5, "T_ANY": 0.05},
    3: {"T_MOVE": 0.5, "T_SHOOT": 0.5, "T_ANY": 0.05},
}

anchor_point = [9, 9]
burnt_nodes = [21] # list of nodes where the fire starts

SQUARE_SHAPE = 10
T_MOVE = 0.025
T_SHOOT = 0.1
T_ANY = 0.025
POS_BULL = [SQUARE_SHAPE-1, SQUARE_SHAPE-1]
BULL_POS = f'{SQUARE_SHAPE-1}.{SQUARE_SHAPE-1}'
POS_FIRE = (5, 0)

parameters = {
    'nrows': SQUARE_SHAPE,
    'ncols': SQUARE_SHAPE,
    'pos_bull': POS_BULL,
    'pos_fire': POS_FIRE,
    't_move': T_MOVE,
    't_shoot': T_SHOOT,
    't_any': T_ANY,
}


grid = [[0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]


A = adjency(grid)
# Convert the grid to numpy array
grid = np.array(grid)

for i in range(4):
    instance_name = f"ahuev_{i}"
    T_MOVE = move_values[i]["T_MOVE"]
    T_SHOOT = move_values[i]["T_SHOOT"]
    T_ANY = move_values[i]["T_ANY"]
    distance = distance_matrix(grid, anchor_point, T_MOVE, T_SHOOT, T_ANY)

    print("distance form 0:5", distance[34,39])


    # Print adjacency matrix
    print("Adjacency Matrix:")
    i = 1
    for row in A:
        print(i, row)
        i += 1





    fighter_pos = anchor_point

    threshold_time = None
    FIREFIGHTERS = 1 # Num. of total firefighters. Must be 1 as default.

    B_base = 1  # The recursion starts from this value of B until solve the instance
    instances = 1 # num. of total instances with the same global seed  for each number of nodes

    json_name = f'instance_{nodes}_{instance_name}.json'
    cvs_name = f"verify_{nodes}_{instance_name}.csv"

    binary_dic = {}
    for i in range(instances):
        binary_dic[i] = []

    # D defending rounds
    # B burning rounds
    # nodes vertices of the graph

    D, _ = start_recursion(nodes,
                           burnt_nodes,
                           distance,
                           instances=instances,
                           node_list=n_list)

    print("n=", nodes, "burnt_nodes=", burnt_nodes, "D", D)

    # We solve finding the minimum B for which the process finishes
    find_B_suf(nodes, burnt_nodes, A, distance, threshold_time, binary_dic,
               json_name, cvs_name, B_base, D, node_list=n_list, instances=instances)
