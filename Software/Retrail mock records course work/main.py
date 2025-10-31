import csv

class Order(): #coontains 3 entities
   def __init__( self, ID, name, product, spent, Category): # initilize the class
      self.ID = ID
      self.name = name
      self.product = product
      self.spent = spent
      self.Category = Category

def readOrders():
    orders = []
    with open("Retail Company Data analysis/ordersExtended.csv", "r") as file:
       reader = csv.reader(file) # splits each row into an array
       next(reader)
       for row in reader:
            neworder= Order(row[0], row[1], row[2], float(row[3]), row[4]) # add new row, with entities, and create an isntance of it
            orders.append(neworder)  # add to array, each isntacne is cotnained with the array
    return orders

def findMaxorder(orders): # pass int eh arraay of isntances
    maxOrder = orders[0] # first isntance is max order 
    for ord in orders[1:]:
            if "TV" in ord.product and ord.spent > maxOrder.spent: # starts from first position instead of position 0 or else it woudl compare psition 0 with its self        if "TV" in ord.product and ord.spent > maxOrder.spent: # meets 2 conditions. 1. TV is in word 2.spent is greater than current vartiabel set to max
                maxOrder = ord
    
    print(maxOrder.spent)

#main
def discountCode(): # in the subprogramme def discountcode()
    orders = readOrders() #add all the orderes to an array
    findMaxorder(orders)
    with open("Retail Company Data analysis/newtextfile.txt", "w") as file:  #open new textfile in write mode to append the discount or no discount
        for ord in orders: 
            chars = ord.product[:3] #first 3 characters
            if int(ord.ID) % 5 == 0:# if there is no remainder then divisble by 5
                file.write(str(ord.ID) +  " " +chars + " Discount" )#add the ID OF USER, FIRST 3 CHARS, htey have a discount
            else:
                file.write(str(ord.ID) +  " " +chars + " No Discount" )
            file.write("\n") # move to next line


            
