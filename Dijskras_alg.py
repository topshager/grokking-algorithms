gragh  = {}


#store all neighbours of node


gragh["you"] = ["alice","bob","clair"]

gragh["start"] = {}
gragh["start"]["a"] = 6
gragh["start"] ["b"] = 2

#getting the values from the hash table
print(gragh["start"].keys())

#weight of edges

print(gragh["start"]["a"])

#adding all nodes

gragh["a"] = {}
gragh["a"]["fin"] = 1
#modeling each nodes neighbours
gragh["b"] = {}
gragh["b"]["a"] = 3
gragh["b"]["fin"] = 5

gragh["fin"] = {}

#repressinting unkown value to get to fin

infinity  = float["inf"]
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#hash  table for parant table:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#array to keep track of checked nodes

processed = ()

#algorithm

node  = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = gragh[node]
    for n in neighbors.key():
        new_cost = cost + neighbors[n]
        if costs[n] >  new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

#adding the finiding lowest cost function Dijskra

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_code_node = None
    for node in costs:
        cost = costs[node]
        if cost > lowest_cost and node not in processed:
            lowest_cost =  costs
            lowest_code_node = node
        return lowest_code_node
