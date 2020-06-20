prices, te, oop = [5, 11, 3, 50, 60, 90], [1, 25, 12, 36, 14, 40] , [1, 100, 101, 200, 201, 300, 301, 400, 401, 500]
k = 2
# def transactionInDays(prices, k):
#     profits = [[0 for x in prices] for y in range(k + 1)]
#     for i in range(1, k + 1):
#         maxSoFar = float("-inf")
#         for j in range( len(prices)):
#             maxSoFar = max(maxSoFar, profits[i - 1][j - 1] - prices[j - 1])
#             #print('MAXSOFAR:', maxSoFar, 'profits[i - 1][j - 1] - prices[j - 1]:', profits[i - 1][j - 1], '-', prices[j - 1])
#             profits[i][j] = max(profits[i][j - 1], maxSoFar + prices[j])
#             print(profits[i][j - 1], maxSoFar, "+", prices[j] )
#     print(prices)
#     for i in range(k + 1):        
#         print(profits[i])

def transactionInDays(prices, k):
    if not len(prices):
        return 0
    evenProfits = [0 for x in prices]
    oddProfits = [0 for x in prices]
    for i in range(1, k + 1):
        maxSoFar = float("-inf")
        if i % 2 == 1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits
        for j in range(1, len(prices)):
            maxSoFar = max(maxSoFar, previousProfits[j -1] - prices[j - 1])
            currentProfits[j] = max(currentProfits[j -1], maxSoFar + prices[j])
    print(evenProfits if k % 2 == 0 else oddProfits)

transactionInDays(oop, 5)