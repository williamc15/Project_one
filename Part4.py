"""
Analysis of Algorithm (AoA) for the Stable Matching Problem:

Time Complexity:
O(n^2), where n is the number of buyers/stocks.

Explanation:
1. In the worst case, each buyer might have to propose to every stock once.
2. There are n buyers, and each might make up to n proposals.
3. This leads to a worst-case time complexity of O(n^2).

Space Complexity:
O(n^2)

Explanation:
1. buyers_preferences and stocks_preferences: O(n^2) - Each of n buyers/stocks has a list of n preferences.
2. free_buyers: O(n) - In the worst case, it could contain all n buyers.
3. matched_stocks: O(n) - It will contain n key-value pairs at the end.
4. stocks_rank: O(n^2) - For each of n stocks, we store a dictionary with n buyer rankings.

Optimality:
This solution is optimal in terms of time complexity for the following reasons:

1. The Gale-Shapley algorithm (which this solution implements) is proven to always find a stable matching in O(n^2) time.
2. It's impossible to find a stable matching in less than O(n^2) time in the worst case, because:
   a. There are n^2 preferences in total that need to be considered.
   b. In the worst case, we might need to look at all preferences to ensure stability.

While the space complexity is also O(n^2), it's mainly due to storing the input preferences. 
The algorithm itself doesn't add significant extra space beyond what's needed to store the input.

Potential improvements:
1. Space optimization: We could potentially reduce space by not creating the stocks_rank dictionary 
   and instead searching the stocks_preferences list each time. However, this would increase the 
   time complexity to O(n^3).
2. For very large datasets, there are more complex algorithms that can achieve slightly better 
   average-case time complexity, but they still have a worst-case time complexity of O(n^2).

In conclusion, this solution is optimal for the general case of the stable matching problem, 
achieving the best possible worst-case time complexity while maintaining a space complexity 
that's on par with the input size.
"""


def stable_matching(buyers_preferences, stocks_preferences):
    # Initialize all buyers and stocks as free
    free_buyers = list(buyers_preferences.keys())
    matched_stocks = {}
    
    # Create a reverse preference list for stocks
    stocks_rank = {stock: {buyer: rank for rank, buyer in enumerate(buyers)}
                   for stock, buyers in stocks_preferences.items()}
    
    while free_buyers:
        buyer = free_buyers.pop(0)
        for stock in buyers_preferences[buyer]:
            if stock not in matched_stocks:
                matched_stocks[stock] = buyer
                break
            else:
                current_buyer = matched_stocks[stock]
                if stocks_rank[stock][buyer] < stocks_rank[stock][current_buyer]:
                    free_buyers.append(current_buyer)
                    matched_stocks[stock] = buyer
                    break
        else:
            free_buyers.append(buyer)
    
    return {v: k for k, v in matched_stocks.items()}

# Example usage:
buyers_preferences = {
    'Buyer1': ['StockA', 'StockB', 'StockC'],
    'Buyer2': ['StockB', 'StockA', 'StockC'],
    'Buyer3': ['StockA', 'StockB', 'StockC']
}

stocks_preferences = {
    'StockA': ['Buyer1', 'Buyer2', 'Buyer3'],
    'StockB': ['Buyer2', 'Buyer1', 'Buyer3'],
    'StockC': ['Buyer1', 'Buyer2', 'Buyer3']
}

result = stable_matching(buyers_preferences, stocks_preferences)
print(result)