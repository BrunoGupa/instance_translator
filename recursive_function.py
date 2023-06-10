import movingfp.gen as mfp
import json
from miqcp import mfp_constraints
from verify_function import verify
from convert_to_cvs import json_to_csv
from gens_for_paper import get_seed
import numpy as np

FIREFIGHTERS = 1


def find_B_suf(nodes, burnt_nodes, A, distance, time, binary_dic, json_name_bin, cvs_name_bin,
               B, D, node_list=None, instances=None):
    # We start with B = 1
    print(
        f"-------Solving  for B = {B},  n = {nodes}, burnt = {burnt_nodes}, D = {D} --------------------------")

    objective, is_upper_bound, not_interrupted = run_and_save(nodes,
                                                               burnt_nodes,
                                                               A,
                                                               distance,
                                                               D,
                                                               B,
                                                               time,
                                                               binary_dic,
                                                               json_name_bin,
                                                               cvs_name_bin,
                                                               node_list,
                                                               instances)

    if not_interrupted:
        if not is_upper_bound:
            B += 1
            find_B_suf(nodes, burnt_nodes, A, distance, time, binary_dic,
                       json_name_bin, cvs_name_bin, B, D, node_list, instances)


def run_and_save(nodes, burnt_nodes, A, distance, D, B, time, binary_dic, json_name_bin, cvs_name_bin,
                 D_max=None, node_list=None, instances=None):
    global FIREFIGHTERS, is_upper_bound


    print("nodes=", nodes)
    print("B=", B)
    print("D=", D)

    infeasible, runtime, not_interrupted, objective, defended_seq, distances = \
        mfp_constraints(D, B, nodes, time, burnt_nodes, A, distance)
    # Verify that the process finishes with that value of B
    _, burnt, B_veri = verify(nodes, burnt_nodes, A, distance, defended_seq,
                              node_list=node_list, instances=instances)

    if objective == burnt:
        # L is an upper bound
        is_upper_bound = True
    else:
        # The process don't end and L is an lower bound
        is_upper_bound = False

    if D_max is None:
        D_max = D

    binary_dic[0].append([[nodes, burnt_nodes],
                                 [D, B, infeasible, runtime, not_interrupted, objective, defended_seq,
                                  distances],
                                 [is_upper_bound, D_max]])

    # Saving data
    with open(f"./runs_grid/jsons/{json_name_bin}", "w") as binary:
        json.dump(binary_dic, binary)
    json_to_csv(f"./runs_grid/jsons/{json_name_bin}", f"./runs_grid/csv_s/{cvs_name_bin}")

    return objective, is_upper_bound, not_interrupted
