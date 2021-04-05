'''
There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.

Examples
mango(3, 3) ==> 6    # 2 mangoes for 3 = 6; +1 mango for free
mango(9, 5) ==> 30   # 6 mangoes for 5 = 30; +3 mangoes for free
'''

def mango(quantity, price):
    remainder = quantity % 3        # Calculate the remainder i.e carry over mangos after triple offer
    offer_mango = (quantity - remainder) * 2/3 * price        # Workout the cost of the mangos that apply to the offer
    total_cost = offer_mango + (remainder * price)      # Total cost is given by the cost with the offer counted 
                                                        # and the basic price applied to any mangos that do not fit 
                                                        # into the 3 for 2
    
    return total_cost
  
'''
Note more consise solution...
'''

def mango(quantity, price):
    return (quantity - quantity // 3) * price   # You get quantity // 3 mangoes for free!
