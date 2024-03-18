num_trucks, length, weight_limit = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * length
time_passed = 0
for truck in trucks:
    while True:
        bridge.pop(0)
        time_passed += 1

        if sum(bridge) + truck > weight_limit:
            bridge.append(0)
        else:
            bridge.append(truck)
            break

time_passed += length
print(time_passed)
