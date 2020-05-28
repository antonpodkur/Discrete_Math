n,m = map(int, input().split())

adj = [[] for i in range(n)]
used = [False for i in range(n)]

for i in range(m):
    v,w = map(int, input().split())
    v-=1
    w-=1
    adj[v].append(w)
    adj[w].append(v)

def dfs(v):
    if used[v]:
        return
    used[v]=True
    print(v+1,end=' ')
    
    for w in adj[v]:
        dfs(w)

def run():
    for v in range(n):
        dfs(v)
run()

