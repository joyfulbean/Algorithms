# https://leetcode.com/problems/network-delay-time/

#첫번째 source의 거리는 0으로 만든다. 
#source를 전부 넣은 priority q를 하나 생성
#그래프레서 v를 하나씩 꺼내서, 반복
#만약 v가 source애 없다면,dist[v]를 무한대로 바꾸기. prev[v]를 undefined 로 바꾼다. 
#그리고 q에 넣는다. 거리와 v를. 
#q가 다 빌때까지 반복
#q에서 가장 낮은걸 꺼내서 u에 넣는다. 
#u의 모든 neighbor방문하면서, u,v의 거리와 u를 더해서 alt에 넣고
#distv가 alter보다 크면, 즉 alt가 더 작으면, 
#dist[v]에 alter를 넣고, prev[v]에 u를 넣는다
#그리고 q의 우선순위를 감소시킨다. 

