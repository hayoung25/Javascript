from logging import captureWarnings


# cap => cap
# wt => weights
# val => value
# n => number of elements

def knapSack(cap, weight, val, n):
    matrix = [[0 for x in range(cap + 1)] for x in range(n + 1)]
  
    # Build table matrix[][] in bottom up manner
    for row in range(n + 1):
        for col in range(cap + 1):
            if row == 0 or col == 0:
                matrix[row][col] = 0
            elif weight[row-1] <= col:
                matrix[row][col] = max(val[row-1] + matrix[row-1][col-weight[row-1]], matrix[row-1][col])
            else:
                matrix[row][col] = matrix[row-1][col]
  
    return matrix[n][cap]
  
  
# Driver code
val = [60, 100, 120]
weight = [10, 20, 30]
cap = 50
n = len(val)
print(knapSack(cap, weight, val, n))
  