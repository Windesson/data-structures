class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        max_coin_values = amount + 1

        def dp(amount):
            nonlocal coins, memo, max_coin_values
            if amount == 0:
                return 0
            
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            
            min_no_coins = max_coin_values
            for coin in coins:
                if amount - coin < 0:
                    continue
                min_no_coins = min(min_no_coins, 1 + dp(amount - coin))
            
            memo[amount] = min_no_coins
            return min_no_coins
        
        res = dp(amount) 
        return res if res < max_coin_values else -1 
        