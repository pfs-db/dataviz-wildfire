"""
Maximize Stock Trading Profit

Given the daily values of a stock, create a function called max_profit_days() that, given a list of
integers, will return the index value of the two elements that represent the day on, which one should
have bought a share and the day on which one should have sold a share based on the max profit.

A list of integers will represent the stock price at the beginning or "opening bell" of each day for a week. You are required to buy and sell only once. You also must buy a stock before selling it.
You are required to buy and sell only once. You also musst buy a stock before selling it.

For example, given the list [17, 11, 60, 25, 150, 75, 31, 120] you can assume that index 0 represents 
day 0 and index 7 represents day 7. In this case, purchasing on day 1 and selling on day 4 would yield 
the most profit. If we were to call max_profit_days([17, 11, 60, 25, 150, 75, 31, 120), the function 
would return (1,4).
This challenge and variations of it were reported to have been asked at interviews with Google. 
If you've covered the material in Pass the Technical Interview with Python or an equivalent, 
you i should be able to solve this challenge. If you have trouble, try refreshing your knowledge 
there first.
"""

import sys


def main():
    sample_list = [17, 11, 60, 25, 150, 75, 31, 120]
    max_profit_days(sample_list)


def max_profit_days(prices: list):
    """Calculating the prices for every possiblity and afterwards finding the max is would have a O(n!) time, that would be really bad"""
    if prices == []:
        return
    max_profit_days_aux(prices)


def max_profit_days_aux(prices: list, max_value=0) -> int:
    hlist = head(prices)
    tlist = tail(prices)

    # base case
    if hlist == [] or tlist == []:
        return max_value
    print(f"{hlist} {max(tlist)}")
    if max_value < max(tlist) - hlist:
        max_value = max(tlist) - hlist
    max_profit_days_aux(tlist, max_value)


def head(gen_list: list):
    if gen_list == []:
        return []
    else:
        return gen_list[0]


def tail(gen_list: list):
    if gen_list == []:
        return []
    else:
        return gen_list[1 : len(gen_list)]


def map_index(prices: list) -> dict:
    """[17, 11, 60, 25, 150, 75, 31, 120] -> {"17": 0, "11": 1, ...}"""
    if prices == []:
        sys.exit("Price list empty in the map index")
    price_dict = dict()
    for price in prices:
        price_dict[price] = prices.index(price)
    return price_dict


if __name__ == "__main__":
    main()
