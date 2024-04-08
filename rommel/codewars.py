def flick_switch(lst):
    switch = True
    uitkomst = []
    for iets in lst:
        if iets == 'flick':
            switch = False
        uitkomst.append(switch)
    return uitkomst