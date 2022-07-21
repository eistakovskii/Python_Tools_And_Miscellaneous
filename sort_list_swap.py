def sort_swap(x, descending = False, verbose = False):

    for i in range(0,len(x)):
        s_el = x[i]
        for j in range(i, len(x)):
            if descending == False:
                if s_el > x[j]:
                    s_el = x[j]
                    x[i], x[j] = x[j], x[i]
            else:
                if s_el < x[j]:
                    s_el = x[j]
                    x[i], x[j] = x[j], x[i]

    if verbose == True:
        print(x)
        
    return x
