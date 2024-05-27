import sys
import heapq
import math

def testpath(graph):
    lg = len(graph)-1
    d = {}
    for i in range(lg):
        tmp = (graph[i][0] - graph[lg][0])*(graph[i][0] - graph[lg][0]) + (graph[i][1] - graph[lg][1]) * (graph[i][1] - graph[lg][1])
        if tmp <= 10000:
            d[i] = tmp
    if len(d) == 0:
        return False
    elif 0 in d.keys():
        return d[0]**0.5
    else:
        return True
          
def dijkstra(graph):
    lg = len(graph)-1
    done = {}
    heap = [(0,0)]
    heapq.heapify(heap)
    try:
        while done.get(lg) == None:
            cdist, cmin = heapq.heappop(heap) # distance, min node name
            if done.get(cmin) != None:
                continue
            cnode = graph.pop(cmin)
            for k, v in graph.items():
                tmp = (cnode[0] - v[0])*(cnode[0] - v[0]) + (cnode[1] - v[1]) * (cnode[1] - v[1])
                if tmp <= 10000:
                    heapq.heappush(heap, (cdist+(math.sqrt(tmp)), k))
            done[cmin] = cdist
    except IndexError:
         return '-1\n'
    return "{:.2f}\n".format(done.get(lg))

for line in sys.stdin:
        data = line.strip().split(",")
        locs = [(float(data[i]), float(data[i+1])) for i in range(1, len(data), 2)]
        test = testpath(locs)
        if test == False:
            sys.stdout.write('-1\n')
        elif test == True:
            locs = {j:locs[j] for j in range(len(locs))}
            sys.stdout.write(dijkstra(locs))
        else:
            sys.stdout.write("{:.2f}\n".format(test))
