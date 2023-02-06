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
            "Kingdom of Merland": {"Principality of Sicocoria": (-9, -3), "Principality of Montia": (-6, 43), "Douchientian Theocracy": (8, -37), "Grand Duchy of Lignia": (-3, 40), "Republic of Nyirkhad": (28, 4)},
            "Principality of Sicocoria": {"Kingdom of Merland": (-9, 1), "Principality of Montia": (17, 43), "Douchientian Theocracy": (7, -37)},
            "Principality of Montia": {"Principality of Sicocoria": (17, -3), "Kingdom of Tentes": (-4, 30), "Kingdom of Merland": (-6, 1), "Grand Duchy of Lignia": (20, 40), "Kingdom of Guileria": (-25, 12)},
            "Kingdom of Tentes": {"Principality of Montia": (-4, 43), "Gey": (45, -25), "Republic of Nyirkhad": (35, 4)},
            "Gey": {"Kingdom of Tentes": (45, 30), "Republic of Nyirkhad": (-3, 4), "Douchientian Theocracy": (37, -37)},
            "Republic of Nyirkhad": {"Gey": (-3, -25), "Kingdom of Tentes": (35, 30), "Kingdom of Givrairatil": (-33, -24), "Kingdom of Merland": (28, 1)},
            "Bishopric of Silgulia": {"Lharanha": (-5, -2), "United Provinces of Rouertia": (12, 31), "Douchientian Theocracy": (-2, -37)},
            "United Provinces of Rouertia": { "Bishopric of Silgulia": (12, 37), "Kingdom of Givrairatil": (-5, -24), "Douchientian Theocracy": (25, -37), "Kingdom of Guileria": (2, 12)},
            "Kingdom of Givrairatil": {"United Provinces of Rouertia": (-5, 31), "Kingdom of Guileria": (4, 12), "Republic of Nyirkhad": (-33, 4)},
            "Lharanha": {"Bishopric of Silgulia": (-5, 37), "Douchientian Theocracy": (11, -37)},
            "Douchientian Theocracy": {"Principality of Sicocoria": (7, -3), "United Provinces of Rouertia": (25, 31), "Bishopric of Silgulia": (-2, 37), "Lharanha": (11, -2), "Kingdom of Guileria": (15, 12), "Grand Duchy of Lignia": (10, 40), "Gey": (37, -25), "Kingdom of Merland": (8, 1)},
            "Grand Duchy of Lignia":  {"Douchientian Theocracy": (10, -37), "Kingdom of Merland": (-3, 1), "Principality of Montia": (20, 43)},
            "Kingdom of Guileria": {"Kingdom of Givrairatil": (4, -24), "Douchientian Theocracy": (15, -37), "Principality of Montia": (-25, 43)}
        }
    elif dificulty == "facil":
        graph = {
            "Kingdom of Merland": {"Principality of Sicocoria": (8, 6), "Kingdom of Tentes": (8, 12), "Republic of Nyirkhad": (-1, 7)},
            "Principality of Sicocoria": {"Kingdom of Merland": (8, -2), "Principality of Montia": (9, 5), "Gey": (-11, -13)},
            "Principality of Montia": {"Principality of Sicocoria": (9, 6), "Kingdom of Tentes": (-7, 12), "Republic of Nyirkhad": (10, 7)},
            "Kingdom of Tentes": {"Principality of Montia": (-7, 5), "Kingdom of Merland": (8, -2), "Gey": (15, -13)},
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