import random

def find_path_with_fixed_cost_and_value(graph, start, end, path=None, cost=0, value=0):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [(path, cost, value)]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_cost, new_value = graph[start][node]
            new_paths = find_path_with_fixed_cost_and_value(graph, node, end, path, cost + new_cost, value + new_value)
            for new_path, new_cost, new_value in new_paths:
                paths.append((new_path, new_cost, new_value))
    return paths

def graph(dificulty):

    if dificulty == "dificil":
        graph = {
            "Kingdom of Merland": {"Principality of Sicocoria": -2, "Kingdom of Tentes": 4, "Douchientian Theocracy": 11},
            "Principality of Sicocoria": {"Kingdom of Merland": -2, "Principality of Montia": -6},
            "Principality of Montia": {"Principality of Sicocoria": -6, "Kingdom of Tentes": 2},
            "Kingdom of Tentes": {"Principality of Montya": 8, "Kingdom of Merland": 4, "Gey": 8, "Republic of Nyirkhad": -7, "Grand Duchy of Lignia": -5},
            "Gey": {"Kingdom of Tentes": 8, "Republic of Nyirkhad": 5},
            "Republic of Nyirkhad": {"Gey": 5, "Kingdom of Tentes": -7, "Kingdom of Guileria": 8, "Grand Duchy of Lignia": -9},
            "Bishopric of Silgulia": {"Lharanha": 10, "United Provinces of Rouertia": -15, "Kingdom of Givrairatil": -7},
            "United Provinces of Rouertia": {"Lharanha": 5, "Bishopric of Silgulia": -15, "Kingdom of Givairatil": 11, "Douchientian Theocracy": -7},
            "Kingdom of Givrairatil": {"Bishopric of Silgulia": -7, "United Provinces of Rouertia": 11, "Lharanha": -2, "Douchientian Theocracy": 8},
            "Lharanha": {"Bishopric of Silgulia": 10, "Kingdom of Givrairatil": -2, "United Provinces of Rouertia": 5, "Douchientian Theocracy": -5},
            "Douchientian Theocracy": {"Kingdom of Merland": 11, "United Provinces of Rouertia": -7, "Kingdom of Givrairatil": 8, "Lharanha": -5}
        }
    elif dificulty == "facil":
        graph = {
            "Kingdom of Merland": {"Principality of Sicocoria": (8, 6), "Kingdom of Tentes": (8, 12), "Republic of Nyirkhad": (-1, 7)},
            "Principality of Sicocoria": {"Kingdom of Merland": (8, -2), "Principality of Montia": (9, 5), "Gey": (-11, -13)},
            "Principality of Montia": {"Principality of Sicocoria": (9, 6), "Kingdom of Tentes": (-7, 12), "Republic of Nyirkhad": (10, 7)},
            "Kingdom of Tentes": {"Principality of Montya": (-7, 5), "Kingdom of Merland": (8, -2), "Gey": (15, -13)},
            "Gey": {"Kingdom of Tentes": (15, 12), "Republic of Nyirkhad": (4, 7), "Principality of Sicocoria": (-11, 6)},
            "Republic of Nyirkhad": {"Gey": (4, -13), "Kingdom of Merland": (-1, -2), "Principality of Montia": (10, 5)}
        }

    nodes = list(graph.keys())
    start = random.choice(nodes)
    end = random.choice(nodes)

    while end == start:
        end = random.choice(nodes)

    results = find_path_with_fixed_cost_and_value(graph, start, end)

    max_value = max(value for _, _, value in results)

    bag = max(value for _, _, value in results)
    selected_path2 = [path for path, _, value in results if value == bag]

    selected_path = [path for path, _, value in results if value == max_value]

    cost_map = {}
    for node1 in graph:
        for node2 in graph[node1]:
            cost_map[f"{node1} to {node2}"] = graph[node1][node2]

    min_cost = min(cost for _, cost, _ in results)

    for min_cost in results:
        selected_path = (min_cost)

    print(selected_path[1], bag)

    return{
            "cidade inicial": start,
            "cidade de destino": end,
            "caminho mais rentavel": selected_path2,
            "caminho menor energia": selected_path[0],
            "custo menor energia": selected_path[1],
            "custo mais rentavel": bag
        }