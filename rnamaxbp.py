# The implementation of RNA maximum base pair matching algorithm in python version - 3.9


r = "CUUGAAC"

ww = [('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G'), ('G', 'U'), ('U', 'G')]
dictionary1 = {}
dictionary2 = {}
for i in range(0, len(r)):
    for j in range(i, len(r)):
        for x in ww:
            if (r[i], r[j]) == x:
                dictionary1[r[i], r[j]] = 1
            else:
                dictionary2[r[i], r[j]] = 0

dictionary2.update(dictionary1)

print("value for ww base pairs", dictionary2)

m = {}

for i in range(len(r)):
    for j in range(i, i + 3):
        if j <= len(r):
            m[i, j] = 0

print(m)
x = []
for h in range(4, len(r)):
    for i in range(1, len(r) - h):
        j = i + h

        case1 = m[i, j-1 ]
        case2 = (1 + m[i + 1, j - 1]) * dictionary2[r[i], r[j]]

        x.append(max(case1, case2))

print(x)



