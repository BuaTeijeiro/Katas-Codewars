def make_readable(seconds):
    minutes = seconds // 60
    clock_seconds = str(seconds % 60)
    hours = minutes // 60
    clock_minutes = str(minutes % 60)
    clock_hours = str(hours)
    clock = [clock_hours,clock_minutes,clock_seconds]
    for i in range(len(clock)):
        if len(clock[i]) == 1:
            clock[i] = '0' + clock[i]
        else:
            continue
    return ":".join(clock)
