def solution(routes):
    answer = 0
    # 정렬을 합니다. 기준점은 차량이 진입하는 순간입니다.
    routes.sort()
    print(routes)
     # 처음 차가 나가는 거리를 임시변수에 넣어줍니다.
    car_out = routes[0][1]
    camera = 1
    
    for route in routes:
        # 다음차가 현재차가 나간후에 들어온다면 카메라를 추가해야합니다.
        if route[0] > car_out:
            camera += 1
            car_out = route[1]    
         # 현재 차보다 뒤차가 먼저나가면, 즉 뒤차가 범위 안에 있으면
        if route[1] <= car_out:
            car_out = route[1]    
        
    return camera

# def solution(routes):
#     routes = sorted(routes, key=lambda x: x[1])
#     last_camera = -30000

#     answer = 0

#     for route in routes:
#         if last_camera < route[0]:
#             answer += 1
#             last_camera = route[1]

#     return answer