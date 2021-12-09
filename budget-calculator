
#Budget Calculator
#Using the names dictionary and order_list shown below, write a program that fits the following conditions:
# - It should produce an order by adding items to receipt from order_list sequentially.
# - It should Print "Current Total: £x" with each iteration
# - If the order value exceeds the budget value, it should stop adding items and print "Budget Exceeded!".
# - If not, each time it adds items, it should:
# - Print "Adding *full name of item* (quantity)".
# - Subtract the price from budget.
# - Add the price to running_total.
# - It should print out running_total, order and budget formatted into print statements (done for you).
# order_list = [("tom", 0.87, 4),
# ("sug", 1.09, 3),
# ("ws", 0.29, 4),
# ("juc", 1.89, 1),
# ("fo", 1.29, 2)]
# names = {"tom":"Tomatoes",
# "sug":"Sugar",
# "ws":"Washing Sponges",
# "juc":"Juice",
# "fo":"Foil"}
# budget = 10.00
# running_total = 0
# receipt = []


# %%
#Solution to activity

order_list = [("tom", 0.87,2),
("sug", 1.09, 2),
("ws", 0.29, 1),
("juc", 1.89, 0),
("fo", 1.29, 2)]

names = {"tom":"Tomatoes",
"sug":"Sugar",
"ws":"Washing Sponges",
"juc":"Juice",
"fo":"Foil"}

#Unpacks the tuple to assign parameters
budget, running_total, receipt = 10.00 , 0 , []

#
for item in order_list:
    if running_total <= budget:
        if(item[2] > 0):
            print(f'Adding {names[item[0]]} ({item[2]})\n')
            price = item[2] * item[1]
            budget = budget - price
            running_total = running_total + price
            item_cost = (item[0], item[2], price)
            receipt.append(item_cost)
            print('Current Total: £{} \n '.format(running_total))
            print('Budget: £{} \n '.format(budget))
            

        else:
            print('Sorry! Budget exceeded')
            break

print('--------------------------------------------------------')
print('Receipt')
print('--------------------------------------------------------')

count = 1

#print reciept
for i in receipt:
        # print(f'{count}) {names[i[0]]} {i[1]} ')
        print('{}| {n} | {q} | £{p:.2f} '.format(count, n = names[i[0]], q =  i[1], p =  i[2]))
        count += 1

