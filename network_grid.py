import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def adjency(grid):

    # Identify the positions of 1s and label them
    labels = {}
    counter = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                labels[(i, j)] = counter
                counter += 1

    # Create the networkx graph
    G = nx.Graph()

    # Add nodes
    for position, label in labels.items():
        G.add_node(label, pos=position)

    # Add the isolated node 'a' at (9,9)
    G.add_node('a', pos=(9, 9))

    # Add edges
    for position, label in labels.items():
        i, j = position
        # Check for adjacency (including diagonals) and add edges accordingly
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:  # skip self
                    continue
                if (i+di, j+dj) in labels:  # neighbor exists
                    G.add_edge(label, labels[(i+di, j+dj)])

    # Draw the graph
    pos = nx.get_node_attributes(G, 'pos')
    transformed_pos = {node: (y, -x) for node, (x, y) in pos.items()}  # rotate 90 degrees clockwise and reflect

    nx.draw(G, transformed_pos, with_labels=True)
    plt.show()

    # Find the label of each node
    # Copy grid
    labeled_grid = np.empty_like(grid, dtype=object)

    #Label '1's and '0's
    counter = 1
    for i in range(labeled_grid.shape[0]):
       for j in range(labeled_grid.shape[1]):
           if grid[i][j] == 1:
               labeled_grid[i, j] = counter
               counter += 1
           else:
               labeled_grid[i, j] = grid[i][j]

    #Add the new label 'a' to the labeled grid
    labeled_grid[9][9] = 'a'

    # Print labeled grid
    print(labeled_grid)


    # Get adjacency matrix
    A = nx.adjacency_matrix(G).toarray()

    # Reorder rows and columns to match the desired order
    #desired_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a']
    desired_order = [str(i) for i in range(1, 40)]
    #print(desired_order)

    node_order = list(map(str, G.nodes()))
    reorder_indices = [node_order.index(node) for node in desired_order]

    A_reordered = A[reorder_indices][:, reorder_indices]

    return A_reordered






# import networkx as nx
# import matplotlib.pyplot as plt
# import numpy as np
#
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
# # Identify the positions of 1s and label them
# labels = {}
# counter = 1
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == 1:
#             labels[(i, j)] = counter
#             counter += 1
#
# # Create the networkx graph
# G = nx.Graph()
#
# # Add nodes
# for position, label in labels.items():
#     G.add_node(label, pos=position)
#
# # Add edges
# for position, label in labels.items():
#     i, j = position
#     # Check for adjacency (including diagonals) and add edges accordingly
#     for di in [-1, 0, 1]:
#         for dj in [-1, 0, 1]:
#             if di == 0 and dj == 0:  # skip self
#                 continue
#             if (i+di, j+dj) in labels:  # neighbor exists
#                 G.add_edge(label, labels[(i+di, j+dj)])
#
# # # Draw the graph
# # pos = nx.get_node_attributes(G, 'pos')
# # nx.draw(G, pos, with_labels=True)
# # plt.gca().invert_yaxis()  # to match the grid's visual representation
# # plt.show()
#
# # Draw the graph
# pos = nx.get_node_attributes(G, 'pos')
# transformed_pos = {node: (y, -x) for node, (x, y) in pos.items()}  # rotate 90 degrees clockwise and reflect
#
# nx.draw(G, transformed_pos, with_labels=True)
# plt.show()
#
#
#
# # Find the label of each node
# # Copy grid
# labeled_grid = np.array(grid)
#
# # Label '1's
# counter = 1
# for i in range(labeled_grid.shape[0]):
#     for j in range(labeled_grid.shape[1]):
#         if labeled_grid[i, j] == 1:
#             labeled_grid[i, j] = counter
#             counter += 1
#
# # Print labeled grid
# print(labeled_grid)
#

# anchor point?
