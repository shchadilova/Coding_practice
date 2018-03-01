import sys

#!/bin/python3

import sys

def CoinChange(m, coins, _cashe={}):
    
    change = 0
    
    memo_key = str((m, coins))
    
    if memo_key in _cashe.keys():
        return _cashe[memo_key]
    
    else:
        if m == 0:
            _cashe[memo_key] = 1
            return 1
        elif m < 0:
            _cashe[memo_key] = 0
            return 0
        else:
            if len(coins) == 0:
                _cashe[memo_key] = 0
                return 0
            else:
                change = CoinChange(m - coins[-1], coins) + CoinChange(m, coins[:-1])
                _cashe[memo_key] = change
                return change  

n = int(input().strip())
for i in range(n):
    n = int(input().strip())
    coins = [int(c) for c in input().strip().split(" ")]
    m = int(input().strip())
    #print(coins)
    print(CoinChange(m, coins))