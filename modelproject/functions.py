# Find kth highest bid

def k_highest_bid(k, all_valuations):
    return round(sorted(all_valuations, reverse = True)[k-1], 3)

# Bidders payoff from participating in auction
#Only if you have the highest valuation and thereby the highest bid you will win the auction and get a positive payoff

def bidders_payoff(optimal_bid, highest_bid, k_highest_bid):
    if optimal_bid == highest_bid:
        return round((valuation - k_highest_bid), 3)
    else: 
        return 0
    
# Optimal bidding strategies

def opt_bid_2_price(valuation):
    return round(valuation, 3)


def opt_bid_k_price(k, a, n, valuation):
    return round(a + ((n-1-k+1)/n+1-1)*(valuation-a), 3)

#Expected revenue (ex ante)
#Given the revenue equivalence theorem the expected revenue is the same for all auction formats

def expected_revenue_uniform(a, b, n):
    return round(a+((n-1)/(n+1))*(b-a), 3)

# Actual revenue (ex post)

def actual_revenue_uniform(sellers_valuation, highest_bid):
    return round(sellers_valuation - highest_bid, 3)