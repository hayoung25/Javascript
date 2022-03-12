
## A Naive recursive Python implementation of LCS problem

# X,Y are arrays and m, n is length of both arrays respectively
def lcs(X, Y, m, n):

    # Base code for recursion
    if m == 0 or n == 0:
       return 0;

    # add 1 to the max length when the end of each array is same
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);

    # if they are not the same, then find bigger number between the recursions 
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));


## Dynamic Programming implementation of LCS problem  
def lcs(X, Y):

    # Find the length of the strings
    m = len(X)
    n = len(Y)
  
    # Declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
    
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# end of function lcs
  

# Driver program to test the above function
# X = "AGGTAB"
# Y = "GXTXAYB"
# print("Length of LCS is ", lcs(X, Y))
  
