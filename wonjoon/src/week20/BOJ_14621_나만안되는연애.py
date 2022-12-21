import sys

input = sys.stdin.readline
N, M = map(int, input().split())

gender = list(map(str, input().split()))
check = [0] * N

parent = [0] * (N + 1)  # 정점 초기화
edges = []

# 부모 테이블에서 부모 자기 자신으로 초기화
for i in range(1, N + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()  # 비용순으로 오름차순 정렬


# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    if parent[x] == x:
        return x

    parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾기 (간선 연결)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


res = 0
for edge in edges:
    cost, a, b = edge

    # 성별이 같으면 패스
    if gender[a - 1] == gender[b - 1]:
        continue

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
        check[a - 1] += 1
        check[b - 1] += 1

for t in check:
    if t == 0:
        res = -1
        break

print(res)
