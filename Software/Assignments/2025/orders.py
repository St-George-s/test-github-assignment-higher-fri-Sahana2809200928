import csv

class orders():
    def __init__(self,orderNum,date,email,option,cost,rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost
        self.rating = rating
    

def readOrders():
    Orders = []
    with open('Software/Assignments/2025/orders.txt', 'r') as file:
        reader= csv.reader(file)
        for row in reader:
            newOrder = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            Orders.append(newOrder)
    return(Orders)

def first_5_star_order_position():
    position = -1
    index = 0
    month= input("enter a chosen month")
    while position == -1 and index < len(Orders):
        if Orders[index].month == "month" and  Orders[index].rating == 5:
            position = index
        else:
            index =+ 1
    return position

def write_winner_details_to_file():
    with open ('winners.py', 'w') as file:
        if position >= 0:
            file.append(position)
        else:
            file.write("none")
        



#main
Orders = readOrders()

position = first_5_star_order_position()

write_winner_details_to_file()

