# coding=utf-8
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = float('inf')

visited = set()

def findlowestcost():

    lowestcost = float('inf')
    node = None
    for k, v in costs.items():
        if k not in visited and v < lowestcost:
            lowestcost = k
            node = k
    return node

node = findlowestcost()

while node:
    cost = costs[node]
    for k, v in graph[node].items():

        if cost + v < costs[k]:
            costs[k] = cost + v
    visited.add(node)

    node = findlowestcost()

print costs