def maxProfit( prices):
       
        maxProfit=0
        minPrice=float("inf")
        for price in prices:
            minPrice=min(minPrice,price)
            maxProfit=max(maxProfit,price-minPrice)
                
        return maxProfit
    
    
print(maxProfit([2,8,1,3,5]))