# Returns the count of ways we can sum S[0...m-1] coins to get sum n
def countRecursive(S, m, n ):

    # If n is 0 then there is 1 solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no solution exists
    if (n < 0):
        return 0;

    # If there are no coins and n is greater than 0, then no solution exist
    if (m <=0 and n >= 1):
        return 0

    # count is sum of solutions (i) including S[m-1] (ii) excluding S[m-1]
    return countRecursive( S, m - 1, n ) + countRecursive( S, m, n-S[m-1] );

# Dynamic Programming Python implementation of Coin Change problem
def countTabulation1(S, m, n):
    # We need n+1 rows as the table is constructed in bottom up manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):

            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m-1]

# Dynamic Programming Python implementation of Coin Change problem
def countMemoization(S, m, n):

    # table[i] will be storing the number of solutions for value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0) Initialize all table values as 0
    table = [0 for k in range(n+1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]

    return table[n]