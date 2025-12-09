import math
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n

    def find(self, A):
        if self.parent[A] == A:
            return A
        self.parent[A] = self.find(self.parent[A])
        return self.parent[A]

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return False
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True

    def getThreeLargestCircuits(self):
        sorted_size = sorted(self.size, reverse=True)
        return (sorted_size[0], sorted_size[1], sorted_size[2])

# with open("sample-input", 'r') as f:
with open("actual-input", 'r') as f:
    lines = f.readlines()

arr = []

for line in lines:
    x, y, z = line.strip().split(',')
    new_tuple = (int(x), int(y), int(z)) 
    arr.append(new_tuple)

def distance(p1, p2, i, j):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt(((x1 - x2) ** 2) + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    return (distance, i, j)

min_heap = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        p1, p2 = arr[i], arr[j]
        heapq.heappush(min_heap, distance(p1, p2, i, j))

uf = UnionFind(len(arr))

count_components = len(arr)

while min_heap:
# for i in range(0, 10):
    (distance, p1, p2) = heapq.heappop(min_heap)
    combined = uf.union(p1, p2)
    if combined:
        count_components -= 1
    if count_components == 1:
        print("combined all components")
        print(arr[p1][0] * arr[p2][0])
        break
print(count_components)
# s1, s2, s3 = uf.getThreeLargestCircuits()
# print(s1 * s2 * s3)
