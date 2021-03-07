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

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = []


visited = set()
def lowest_cost():
    lowest = float('inf')
    lowest_node = None
    for k, v in costs.items():
        if v < lowest and k not in visited:
            lowest = v
            lowest_node = k
    return lowest_node

node = lowest_cost()

while node:
    cost = costs[node]
    for k, v in graph[node].items():
        if cost + v < costs[k]:
            costs[k] = cost + v
            parents[k] = node
    visited.add(node)
    node = lowest_cost()

print(costs)
print(parents)





'''
Python 语法方面的问题：
无穷大的表示法 float("inf")
dict1.keys() 不是 dick1.keys  要加括号，是个函数
while 的使用方法
数字转化为 字符串 str(n) 而不是 n.str()
'''