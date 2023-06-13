import networkx as nx
import numpy as np
# este no sirve, eliminarlo
class GridToGraph:
    def __init__(self, namespace):
        self.A = namespace['A']
        self.D = namespace['D']
        self.G_fighter = namespace['G_fighter']
        self.G_fire = namespace['G_fire']
        self.burnt_nodes = namespace['burnt_nodes']
        self.fighter_pos = namespace['fighter_pos']
        self.node_pos = namespace['node_pos']

    def get_output(self):
        return {
            'graph_fighter': self.G_fighter,
            'graph_fire': self.G_fire,
            'burnt_nodes': self.burnt_nodes,
            'fighter_pos': self.fighter_pos,
            'node_pos': self.node_pos,
            'distance_matrix': self.D
        }

def mfp_constraints(D, B, nodes, time, burnt_nodes, A, distance, return_matrices=False):

def fixed_grid_to_graph(grid, fighter_pos=None, num_fires=1):
    """Returns a MFP instance for a given grid.

    Parameters
    ----------
    n : int
        Number of nodes.
    p : float
        Probability for edge creation.
    dim : int, optional (default 2)
        Dimension of graph.
    fighter_pos : list or None (default)
        The Firefighter initial position. If `None`, position is chosen at random in the unit cube
        of dimensions `dim`.
    num_fires : int, optional (default 1)
        Number of initial burnt nodes. `num_fires` nodes are chosen at random from `n` nodes.
    generator : None (default) or np.random._generator.Generator.
        Indicator of random number generation state.

    Returns
    -------
    A_fire : numpy array
        n x n adjacency matrix of the fire graph.
    D_fighter : numpy array
        (n+1) x (n+1) distance matrix of the firefighter graph. The last row and column corresponds
        to the firefighter.
    burnt_nodes : list
        Initial burnt nodes.
    fighter_pos : list
        Initial firefighter position.
    node_pos : list
        Positions of the nodes"""


    fighter_pos = init_fighter_pos(dim, fighter_pos, generator)

    # if seed is not None: generator = rng[1]
    burnt_nodes = init_burnt_nodes(n, num_fires, generator)

    # Fire graph
    # if seed is not None: generator = rng[2]
    G_fire = erdos_graph_forced(n, p, dim, generator)
    A_fire = adjacency_matrix(G_fire)

    # Firefighter graph
    pos = nx.get_node_attributes(G_fire, 'pos')
    pos[n] = fighter_pos
    G_fighter = complete_graph(n + 1, dim, pos)
    D_fighter = euclidean_matrix(G_fighter)

    nodes_pos = [coor for u, coor in pos.items()][:-1]
    instance = {'A': A_fire, 'D': D_fighter, 'fighter_pos': fighter_pos,
                'node_pos': nodes_pos, 'burnt_nodes': burnt_nodes, 'G_fire': G_fire,
                'G_fighter': G_fighter}
    instance = SimpleNamespace(**instance)

    return instance
