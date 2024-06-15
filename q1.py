prices=[]
#i want 5 prices in array
days=['monday','tuesday','wednesday','thirsday','friday','saturday']
for i in range(len(days)):
    n=int(input('enter the number'))
    prices.append(n)
print(prices)
#buy
#chooes the days too bus a stock
buy=0
for i in days:
    if i=='monday':
        buy=prices[1]
#chooes the day for sell the stock
sell=0
for i in days:
    if i=='saturday':
        sell=prices[5]
profit=buy-sell
print(profit,'you are gain the this profit from this trade')




