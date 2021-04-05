# dynamic dictionary problem no.1

#create an empty dictionary
shop={}

#n=> Product=3
n=int(input("Enter the number of products do you want to add :"))

# product name - input
# product price - input
for i in range(n):
    name=input("Enter the name of the product :")
    price=int(input("Enter the price of the product :"))
    shop[name]=price
print(shop)