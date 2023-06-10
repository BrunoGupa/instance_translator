import numpy as np
from decimal import Decimal


# Suppose anchor point is not in any tree
def distance_matrix(grid, anchor_point, t_move, t_shoot, t_any, round_float=3):
    t_move = Decimal(t_move)
    t_shoot = Decimal(t_shoot)
    t_any = Decimal(t_any)

    distances_array = []
    row, col = anchor_point

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                distances = []
                for k in range(grid.shape[0]):
                    for l in range(grid.shape[1]):
                        if grid[k, l] == 1:
                            d = Decimal(max(abs(i-k), abs(j-l)))
                            d = d * (t_any + t_move)
                            if d > 0:
                                d += t_shoot
                            d = round(float(d), round_float)
                            distances.append(d)

                d = Decimal(max(abs(i - row), abs(j - col)))
                d = d * (t_any + t_move) + t_shoot
                d = round(float(d), round_float)
                distances.append(d)

                distances_array.append(distances)

    distances = []
    for k in range(grid.shape[0]):
        for l in range(grid.shape[1]):
            if grid[k, l] == 1:
                d = Decimal(max(abs(row - k), abs(col - l)))
                d = d * (t_any + t_move) + t_shoot #Keep + shoot time for symmetry (but should not be added)
                d = round(float(d), round_float)
                distances.append(d)

    row, col = anchor_point
    d = Decimal(max(abs(row - row), abs(col - col)))
    d = round(float(d), round_float)
    distances.append(d)

    distances_array.append(distances)

    print("Grid:")
    print(grid)
    print("Distances:")
    print(distances_array)
    return np.array(distances_array)







# import numpy as np
# from decimal import Decimal
#
# SQUARE_SHAPE = 20
# T_MOVE = 0.025
# T_SHOOT = 0.05
# T_ANY = 0.025
#
# anchor_point = [9, 9]
# init_fire = []
#
#
# print("anchor_point", anchor_point)
#
#
# # Suppose anchor point is not in any tree
# def distance_matrix(grid, anchor_point, t_move, t_shoot, t_any, round_float=3):
#     # t_any: time added at any step
#     # t_move: time added when the bulldozer moves to its neighborhood (not its same position)
#     # t_shoot: time to added to cut a tree.
#     t_move = Decimal(t_move)
#     t_shoot = Decimal(t_shoot)
#     t_any = Decimal(t_any)
#
#     # initialize the distances array with zeros
#     distances_array = []
#     row, col = anchor_point
#
#     # iterate over all values in the grid that are equal to 3
#     for i in range(grid.shape[0]):
#         for j in range(grid.shape[1]):
#             if grid[i, j] == 3:
#                 distances = []
#                 # calculate the distance from value to all other 3s in the grid
#                 for k in range(grid.shape[0]):
#                     for l in range(grid.shape[1]):
#                         if grid[k, l] == 3:
#                             d = Decimal(max(abs(i-k), abs(j-l)))
#                             d = d * (t_any + t_move)
#                             # -------------------------------
#                             # We do strong assumptions: As the MFP constrains need d(x,x) = 0,
#                             # We need that the anchor point don't be a tree. With this:
#                             # * The optimum never digs its own place, then
#                             # * we can substitute d(x,x) = t_any + t_shoot by d'(x,x) = 0
#                             # -------------------------------
#                             if d > 0:
#                                 d += t_shoot
#                             d = round(float(d), round_float)
#                             #print(f"from {i,j} to {k,l} distance {d}")
#                             distances.append(d)
#                 # Calculate the distance to the anchor point
#                 d = Decimal(max(abs(i - row), abs(j - col)))
#                 d = d * (t_any + t_move)
#                 d = round(float(d), round_float)
#                 # From tree to anchor point we have not to add t_shoot because anchor point is not a tree
#                 distances.append(d)
#
#                 distances_array.append(distances)
#     # Add the anchor point
#     distances = []
#     # calculate the distance from anchor point to all other trees in the grid
#     for k in range(grid.shape[0]):
#         for l in range(grid.shape[1]):
#             if grid[k, l] == 3:
#                 d = Decimal(max(abs(row - k), abs(col - l)))
#                 # If the bulldozer moves to the anchor point to a tree, it shoots
#                 d = d * (t_any + t_move) + t_shoot
#                 d = round(float(d), round_float)
#                 distances.append(d)
#     # Calculate the distance to the anchor point to itself
#     row, col = anchor_point
#     d = Decimal(max(abs(row - row), abs(col - col)))
#     d = round(float(d), round_float)
#     distances.append(d)
#
#     distances_array.append(distances)
#
#     # print the grid and distances
#     print("Grid:")
#     print(grid)
#     print("Distances:")
#     print(distances_array)
#
# #anchor_point = [1, 2]
# #distance_matrix(grid, anchor_point, 0,0,1)
# #distance_matrix(grid,anchor_point,T_MOVE,T_SHOOT,T_ANY)
# grid = [[0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
#         [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
#         [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
#         [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
#         [0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#         [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
#         [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]
#
#
# distance_matrix(grid, (9,9), T_MOVE, T_SHOOT, T_ANY)
