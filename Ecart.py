def calculate_shipping_fee(units, units_per_package=10, package_fee=5):
    num_packages = units // units_per_package
    if units % units_per_package != 0:
        num_packages += 1
    shipping_fee = num_packages * package_fee
    return shipping_fee


def flat_10_Discount(total_price):
    flat_10_discount = total_price-10
    return flat_10_discount
            
        
def bulk_5_Discount(orders):
    discounted_total = 0

    for order in orders:
        product = order['product']
        quantity = order['quantity']
        price = order['price']
        
        if quantity >= 10:
            discount = 0.1
            discounted_price = price - (price*discount)
            discounted_total += discounted_price
        else:
            discounted_total += price

    return discounted_total


def tiered_50_Discount(orders):
    discounted_total = 0
    
    for order in orders:
        product = order['product']
        quantity = order['quantity']
        price = order['price']

        if quantity >= 15:
            discount = 0.5
            discounted_price = price - (price*discount)
            discounted_total += discounted_price
        else: 
            discounted_total += price

    return discounted_total

    
def discount(total_price, orders):
    discountDict = {}

    if total_price >= 200:  
        discountDict['flat_10_discount'] = flat_10_Discount(total_price)
    
    if above_10:
        discountDict['bulk_5_discount'] = bulk_5_Discount(orders)

    if above_15 and total_quantity >= 30: 
        discountDict['tiered_50_discount'] = tiered_50_Discount(orders)   

    if discountDict:
        return (min(discountDict.items(), key=lambda x: x[1]))
    

if __name__ == "__main__":

    price = 0
    total_price = 0
    total_quantity = 0
    above_15 = False
    above_10 = False
    shoppingDict = {"A":20,"B":40,"C":50}
    orders = []
    giftWrap_Fee = 0

    for k,v in shoppingDict.items():print(f'{k}: Price {v}')
    while True:
        choice = input('\nChoose an item: A, B, C\n').upper()
        if choice not in shoppingDict:
            print('Invalid Product')
        else:
            quantity=int(input("Enter quantity:"))
            if input("Do you want product as a gift? y/n:").lower() == 'y':
                giftWrap_Fee += quantity * 1.00
            if quantity >= 15: above_15 = True
            if quantity >= 10: above_10 = True
            total_quantity += quantity
            price = quantity*shoppingDict.get(choice)
            orders.append({'product': choice,'quantity':quantity,'price':price})
            try:total_price += quantity*shoppingDict.get(choice)

            except KeyError:print('Error')
            if input('Would you like to go pick another order? y/n:').lower() == 'n':
                print()
                print('\t\t\t-------Order Details----------')
                print()
                print(orders)
                print()
                print(f'Subtotal: ${total_price}')
                break

    
    #Discount
    if discount(total_price,orders):
        discountName, discountAmount = discount(total_price,orders)
        print()
        print(f'Discount Name:{discountName}')
        print(f'Discount Amount:${discountAmount}')
        total_price = discountAmount
        
    #Shipping
    units_per_pack=10
    package_fee=5
    shipping_Fee = calculate_shipping_fee(total_quantity, units_per_pack, package_fee)
    print()
    print(f'shipping Fee: ${shipping_Fee}')

    #Gift
    if giftWrap_Fee:
        print()
        print(f'Gift wrap fee: ${giftWrap_Fee}')

    #Total cost
    total = total_price + giftWrap_Fee + shipping_Fee
    print()
    print(f'Total: ${total}')