cnt=0

def dfs(firstnode):
    visited[firstnode]=1
    global cnt
    cnt+=1
    for nextnode in graph[firstnode]:
        #if visited[nextnode]==0 and graph[firstnode]==True:
        if visited[nextnode]==0:                                # 변경 -> 굳이 확인 안해도 for문에서 확인됨
            dfs(nextnode)


#n = map(int, input())
#m = map(int, input())
n = int(input())            # 변경    map이라는 함수에 대한 참조값이므로 밑에서 n+1을 하지 못함 따라서 변경
m = int(input())            # 변경
graph=[[] for _ in range(n+1)]
#visited=[0]*n
visited=[0]*(n+1)           # 변경    총 n+1개이기 때문
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)      # 추가    단방향이 아닌 양방향이므로 추가

dfs(1)

print(cnt-1)

