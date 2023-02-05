import random

dificulty = input("Escolha a dificuldade de jogo: facil ou dificil\n")

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
        "Kingdom of Merland": {"Principality of Sicocoria": -2, "Kingdom of Tentes": 4},
        "Principality of Sicocoria": {"Kingdom of Merland": -2, "Principality of Montia": -6},
        "Principality of Montia": {"Principality of Sicocoria": -6, "Kingdom of Tentes": 2},
        "Kingdom of Tentes": {"Principality of Montya": 8, "Kingdom of Merland": 4, "Gey": 8, "Republic of Nyirkhad": -7},
        "Gey": {"Kingdom of Tentes": 8, "Republic of Nyirkhad": 5},
        "Republic of Nyirkhad": {"Gey": 5, "Kingdom of Tentes": -7}
}

def find_path_with_fixed_cost(graph, start, end, path=None, cost=0):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [(path, cost)]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_cost = cost + graph[start][node]
            new_paths = find_path_with_fixed_cost(graph, node, end, path, new_cost)
            for new_path, new_cost in new_paths:
                paths.append((new_path, new_cost))
    print(paths)
    return paths

nodes = list(graph.keys())
start = random.choice(nodes)
end = random.choice(nodes)

results = find_path_with_fixed_cost(graph, start, end)

print("Cidade inicial:", start)
print("Cidade de destino:", end)

cost_map = {}
for node1 in graph:
    for node2 in graph[node1]:
        cost_map[f"{node1} to {node2}"] = graph[node1][node2]

for cost in cost_map:
    print("O custo de", cost, "e igual a:", cost_map[cost])

selected_path = None
while not selected_path:
    min_cost = min(cost for _, cost in results)
    user_choice = input("Digite o custo do menor caminho possível: ")
    try:
        choice = int(user_choice)
        if choice == min_cost:
            for path, cost in results:
                if cost == choice:
                    selected_path = (path, cost)
                    break
        else:
            print("Este não é o caminho mais curto, tente novamente")
    except ValueError:
        print("Entrada inválida, digite um número!")

print("Parabens, voce acerto, o caminho correto e ", selected_path[0], "com custo de: ", selected_path[1])