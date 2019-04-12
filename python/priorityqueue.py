
import heapq

pq = []

heapq.heappush(pq, (-4, 4))
heapq.heappush(pq, (-1, 1))
heapq.heappush(pq, (-3, 3))
heapq.heappush(pq, (-2, 2))

print pq[0]
print heapq.heappop(pq)

print pq[0]
print heapq.heappop(pq)