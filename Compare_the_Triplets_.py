def compareTriplets(a, b):
    a_point = 0
    b_point = 0
    points = []
    
    for i in range (0, len(a)):
        if a[i] == b[i]:
            pass
        elif a[i] > b[i]:
            a_point += 1
        else:
            b_point += 1
            
    points.append(a_point)
    points.append(b_point)
    return points
