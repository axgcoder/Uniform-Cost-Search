import heapq
import sys
from collections import defaultdict

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self._index = 0

    def put(self,(d, pri)):
        heapq.heappush(self.heap,(d,pri))

    def get(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)

    def empty(self):
		return len(self.heap) == 0

#to calculate ucs
def search(graph, start, end):
    if start not in graph:
        print(start + ' not found in graph !')
        return
    if end not in graph:
        print(str(end) + ' not found in graph !')

    queue = PriorityQueue()
    queue.put((0, [start]))
    fringe = set()
    while not queue.empty():
        cost,node = queue.get()

        current = node[len(node) - 1]
        if current not in fringe:
            fringe.add(current)
            if current == end:
              node.append(cost)
              return node

            for neighbor in graph[current]:
             if neighbor not in fringe:
              temp = list(node[:])
              temp.append(neighbor)
              total = cost + graph[current][neighbor]
              queue.put((total, temp))

# to read file
def read_file(filename):
    graph = defaultdict(dict)
    f = open(filename, 'r')
    for line in f:
        try:
            city1,city2,distance = line.lower().split()
            distance = int(distance)
        except ValueError:
             return dict(graph)
        graph[city1][city2] = distance
        graph[city2][city1] = distance
    f.close()
    return dict(graph)

# to display routes
def display(graph,route):
    distance = route[-1]
    print ('distance: %s km' % (distance))
    print ('route: ')
    for i in range(len(route[:-1])):
       try:
         distance=graph[route[i]][route[i + 1]]
         print ('%s to %s, %s km' % (route[i], route[i + 1], distance))
       except:
           pass

def main():
    filename = sys.argv[1]
    start = str(sys.argv[2]).lower()
    dest = str(sys.argv[3]).lower()
    graph = read_file(filename)
    print(graph)
    route=search(graph, start, dest)
    if route:
        display(graph, route)
    else:
        print('distance: infinity')
        print ('route:')
        print (route)

if __name__ == "__main__":
    main()
