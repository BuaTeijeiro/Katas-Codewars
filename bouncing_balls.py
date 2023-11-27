def bouncing_ball(h, bounce, window):
    if h <= 0:
        return -1
    elif bounce <= 0 or bounce >= 1:
        return -1
    elif window >= h or window <= 0:
        return -1
    
    
    times = 1
    height = h * bounce
    while height > window:
        height = bounce * height
        times += 2
    
    return times