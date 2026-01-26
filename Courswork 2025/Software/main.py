import csv

def readFile():
    Orders = []
    class order:
        def __init__(self, orderNum, date, email, option, cost, rating):
          self.orderNum = orderNum
          self.date =date
          self.email =email
          self.option =option
          self.cost=cost
          self.rating = rating

    with open('Courswork 2025/Software/orders.txt', 'r') as file:
       reader = csv.reader(file)
       for row in reader:
          NewOrder = order(row[0], row[1], row[2], row[3], row[4], row[5])
          Orders.append(NewOrder)
    return Orders



def identify_winner():
    position = -1
    index = 0
    month = input("enter a month")
    while position == -1 and index < len(Orders):
      if (month[0:4] == Orders[index].date) and (Orders[index].rating) == 5:
         position = index
      else:
         index = index + 1

    print(position)

#main
Orders = readFile()
identify_winner()
