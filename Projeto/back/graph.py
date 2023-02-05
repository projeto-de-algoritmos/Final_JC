import random

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
    return paths

graph = {
    "Kingdom of Merland": {"Principality of Sicocoria": -2, "Kingdom of Tentes": 4},
    "Principality of Sicocoria": {"Kingdom of Merland": -2, "Principality of Montia": -6},
    "Principality of Montia": {"Principality of Sicocoria": -6, "Kingdom of Tentes": 2},
    "Kingdom of Tentes": {"Principality of Montya": 8, "Kingdom of Merland": 4, "Gey": 8, "Republic of Nyirkhad": -7},
    "Gey": {"Kingdom of Tentes": 8, "Republic of Nyirkhad": 5},
    "Republic of Nyirkhad": {"Gey": 5, "Kingdom of Tentes": -7}
}

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
    print("O custo de", cost, "é igual a:", cost_map[cost])

selected_path = None
while not selected_path:
    user_choice = input("Digite o custo do menor caminho possivel: ")
    try:
        choice = int(user_choice)
        for path, cost in results:
            if cost == choice:
                selected_path = (path, cost)
        if not selected_path:
            print("Este não é o caminho mais curto, tente novamente")
    except ValueError:
        print("Entrada invalida, digite um numero!")

print("Parabéns, você acertou, o caminho correto é ", selected_path[0], "com custo de: ", selected_path[1])