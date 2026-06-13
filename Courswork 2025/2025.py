

import csv
def readFile():
    orders = []
    class Order:
        def __init__(self, orderNum, date, email, type, cost,rating):
            self.orderNum = orderNum
            self.date = date
            self.email = email
            self.type = type
            self.cost = float(cost)
            self.rating = int(rating)
        
    with open('Courswork 2025/Software/orders.txt', 'r') as file:
        reader  = csv.reader(file)
        for row in reader:
            newOrder = Order(row[0], row[1], row[2], row[3], row[4], row[5])
            orders.append(newOrder)
    return orders

def findPositionOfWinner(orders):
    position = -1
    index = 0
    month = input("enter first 3 letters of month")
    while position == -1 and index < len(orders):
        if orders[index].date[0:3] and orders[index].rating ==5:
            position = index
        index+=1
    return position

def writeWinnerToFile(orders, position):
    if position >= 0:
        with open('winningCustomer.txt', 'w') as file:
            file.write(str(orders[position].orderNum )+ "," +str(orders[position].email) +"," + str(orders[position].cost) )
    else:
        file.write("no winner")



def countType(orders, type):
    count = 0
    for index in range(len(orders)):
        if orders[index].type == type:
            count+=1
    print(count)





#main
 

orders = readFile()
position = findPositionOfWinner(orders)
writeWinnerToFile(orders, position)
delivery = countType(orders, 'Delivery')
collection = countType(orders, 'Collection')