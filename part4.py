def stable_stock_matching(buyers_preferences, stocks_preferences):
    # Initialize all buyers and stocks as free
    free_buyers = list(buyers_preferences.keys())
    matched_buyers = {}
    
    # Create a reverse preference list for stocks
    stocks_rank = {stock: {buyer: rank for rank, buyer in enumerate(buyers)}
                   for stock, buyers in stocks_preferences.items()}
    
    while free_buyers:
        buyer = free_buyers.pop(0)
        for stock in buyers_preferences[buyer]:
            if stock not in matched_buyers.values():
                matched_buyers[buyer] = stock
                break
            else:
                current_buyer = [b for b, s in matched_buyers.items() if s == stock][0]
                if stocks_rank[stock][buyer] < stocks_rank[stock][current_buyer]:
                    free_buyers.append(current_buyer)
                    matched_buyers[buyer] = stock
                    del matched_buyers[current_buyer]
                    break
        else:
            free_buyers.append(buyer)
    
    return matched_buyers

# Example usage
if __name__ == "__main__":
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

    result = stable_stock_matching(buyers_preferences, stocks_preferences)
    print(result)
