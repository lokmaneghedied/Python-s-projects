def add_time(start, duration, day=False):
    time1 = start.split()
    start_time = time1[0]
    form = time1[1]
    time2 = duration.split()
    duration_time = time2[0]
    x = start_time.split(':')
    y = duration_time.split(':')
    mn = int(x[1]) + int(y[1])
    h = int(x[0]) + int(y[0])
    n = 0
    while h >= 12 :
        if form == 'AM':
            form = 'PM'
            h -= 12
        else :
            form = 'AM'
            n += 1
            h -= 12
        continue
    if mn >= 60 :
        h = h + 1
        mn = int(x[1]) + int(y[1]) - 60
        if form == 'PM' and h >= 12:
            form = 'AM'
            n += 1
        elif form == 'AM' and h >= 12:
                form = 'PM'
    else :
        mn = int(x[1]) + int(y[1])
    if mn < 10:
        mn = f'0{mn}'
    if day:
        week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
        new_day = f', {week[(week.index(day.capitalize()) + n) % 7]}' 
        if n == 1:
            return f'{h}:{mn} {form}{new_day} (next day)'
        elif n == 0 :
            return f'{h}:{mn} {form}{new_day}'
        else:
            return f'{h}:{mn} {form}{new_day} ({n} days later)'
    else :
        if n == 0 :
            return f'{h}:{mn} {form}'
        if n == 1 :
            return f'{h}:{mn} {form} (next day)'
        else:
             return f'{h}:{mn} {form} ({n} days later)'



print(add_time("3:30 PM", "2:12"))
#expected = "5:42 PM"

#actual = add_time("11:55 AM", "3:12")
#expected = "3:07 PM"

#actual = add_time("2:59 AM", "24:00")
#expected = "2:59 AM (next day)"

#actual = add_time("8:16 PM", "466:02")
#expected = "6:18 AM (20 days later)"