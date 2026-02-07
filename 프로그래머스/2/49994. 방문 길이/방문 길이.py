def solution(dirs):
    
    x, y = 0, 0
    paths = set()
    answer = 0
    
    for dir in dirs:
        tmp_x, tmp_y = x, y
        
        if dir == "U": tmp_y = y + 1
        elif dir == "D": tmp_y = y -1
        elif dir == "R": tmp_x = x + 1
        else: tmp_x = x - 1
        
        if -5 <= tmp_x <= 5 and -5 <= tmp_y <= 5:
            path = tuple(sorted([(x, y), (tmp_x, tmp_y)]))
            paths.add(path)
            x, y = tmp_x, tmp_y
        
    return len(paths)