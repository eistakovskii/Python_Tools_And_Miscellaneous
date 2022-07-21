x = [2,4,6,3,7,9,5]

for i in range(0,len(x)):
    s_el = x[i]
    for j in range(i, len(x)):
        if s_el > x[j]:
            s_el = x[j]
            x[i], x[j] = x[j], x[i]

print(x)
