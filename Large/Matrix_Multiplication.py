x = [[2, -2], 
[5, 3]]

y = [[-1, 4], 
[7, -6]]

result = [[0, 0],
[0, 0]]

# iterate through rows of X
for i in range(len(x)):
    # iterate through columns of Y
    for j in range(len(y[0])):
        # iterate through rows of Y
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

for r in result:
    print(r)

#solved