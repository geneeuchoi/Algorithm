from collections import deque

def solution(bridge_length, weight, truck_weights):

    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    
    answer = 0
    current_weight = 0
    
    while bridge:
        answer += 1
        out = bridge.popleft()
        current_weight -= out
         
        if truck: 
            if current_weight + truck[0] <= weight: 
                current_truck = truck.popleft()
                bridge.append(current_truck)
                current_weight += current_truck 
            else:
                bridge.append(0)
    
            
    return answer