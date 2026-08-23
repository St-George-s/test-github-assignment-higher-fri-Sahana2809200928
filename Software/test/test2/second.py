import csv

class Order:
    def __init__(self, customerName, productPrchased, amountSpent, id,category ):
        self.customerName = customerName
        selfproductPrchased= productPrchased
        self.amountSpent= amountSpent
        self.id = self.category = category

def readOrdersfromCSV():
    Orders = []
    with open('Software/test/test2/orders (1).csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newOrder = Order(row[0], row[1], row[2], row[3], row[4])
            Orders.append(newOrder)
    return Orders

def findMaxOrderWithTV():
    maxOrder = Orders[0]
    for order in Orders:
        if "TV" in Orders[order].productPurchased and Order(order).amountSpent > maxOrder:
            maxOrder = Orders[order]
    print(maxOrder)

def everyFifthCustomerDiscount():
    with open('discounts.txt', 'w') as file:
        chars = ord.customerName[:3]
        for ord in Orders:
            if ord.id % 5 == 0:

                file.write(ord.id + '-' + chars + "-"+ "DISCOUNT CODE ASSIGNED")
            else:
                file.write(ord.id + '-' + chars + "-"+ "DISCOUNT CODE NOT ASSIGNED")
                

#main
Orders = readOrdersfromCSV()
maxOrder= findMaxOrderWithTV()








    
    
