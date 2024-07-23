def stable_stock_matching(buyers_preferences, stocks_preferences):
    free_buyers = list(buyers_preferences.keys())
    matched_buyers = {}
    buyer_current_proposals = {buyer: 0 for buyer in free_buyers}

    while free_buyers:
        buyer = free_buyers.pop(0)
        buyer_prefs = buyers_preferences[buyer]
        stock = buyer_prefs[buyer_current_proposals[buyer]]
        buyer_current_proposals[buyer] += 1

        if stock not in matched_buyers.values():
            matched_buyers[buyer] = stock
        else:
            current_buyer = next(b for b, s in matched_buyers.items() if s == stock)
            stock_prefs = stocks_preferences[stock]
            if stock_prefs.index(buyer) < stock_prefs.index(current_buyer):
                del matched_buyers[current_buyer]
                matched_buyers[buyer] = stock
                free_buyers.append(current_buyer)
            else:
                free_buyers.append(buyer)

    return matched_buyers

# Example usage
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
