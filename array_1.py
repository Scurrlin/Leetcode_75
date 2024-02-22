# Two Sum

def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    for i, num in enumerate(nums):
        if target - num in nums_dict:
            return [nums_dict[target - num], i]
        nums_dict[num] = i

# Best Time to Buy and Sell Stock
        
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

