item_price = 500.73
print('Item Price Is: $', item_price)

purchase_price = int(input('Enter purchase price: '))

if purchase_price == item_price:
    print('Thanks for your patronage')

elif purchase_price < item_price:
   change = item_price - purchase_price
   print(f'Your change is: {change:.2f} cents')