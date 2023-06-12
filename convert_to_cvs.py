import json
import pandas as pd


def json_to_csv(json_name, cvs_name):
    with open(json_name, 'r') as a_file:
        moving = a_file.read()
        moving = json.loads(moving)


    num_nodes = []
    burnt_nodes = []
    instance = []


    D = []
    B = []
    infeasible = []
    runtime = []
    not_interrupted = []
    objective = []
    defended_seq = []
    distances = []

    algorithm = []

    is_upper_bound = []
    D_max = []

    for key in moving.keys():
        for n in range(len(moving[key])):
            algorithm.append("moving")

            x = moving[key][n][0][0]
            num_nodes.append(x)

            x = moving[key][n][0][1]
            burnt_nodes.append(x)

            x = moving[key][n][0][2]
            instance.append(x)

            x = moving[key][n][1][0]
            D.append(x)


            x = moving[key][n][1][1]
            B.append(x)

            x = moving[key][n][1][2]
            infeasible.append(x)

            x = moving[key][n][1][3]
            runtime.append(x)

            x = moving[key][n][1][4]
            not_interrupted.append(x)

            x = moving[key][n][1][5]
            objective.append(x)

            x = moving[key][n][1][6]
            defended_seq.append(x)

            x = moving[key][n][1][7]
            distances.append(x)

            x = moving[key][n][2][0]
            is_upper_bound.append(x)

            x = moving[key][n][2][1]
            D_max.append(x)


    results = {}

    results["num_nodes"] = num_nodes
    results["burnt_nodes"] = burnt_nodes
    results["instance"] = instance

    results["D"] = D
    results["B"] = B

    results["algorithm"] = algorithm

    results["infeasible"] = infeasible
    results["runtime"] = runtime
    results["not_interrupted"] = not_interrupted
    results["objective"] = objective
    results["is_upper_bound"] = is_upper_bound
    results["D_max"] = D_max
    results["defended_seq"] = defended_seq
    results["distances"] = distances


    df = pd.DataFrame(results)
    df.to_csv(cvs_name)
