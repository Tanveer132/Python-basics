#-/-/-/-/-/-/-/-/-/-/-/-/-GROCCERY SHOP-/-/-/-/-/-/-/-/-/-/-/-/-

#menu available in the shop
shop=[["oil",160],["milk",97],["sugar",40]]

# empty bag 
bag=[]
# bill 
bill=[]
status="Y"
ch=0
while ch<=5:
    print("----choose below option----")
    # ask the user to select the operation
    choice=int(input("1. shop display.\n 2. buy product. \n 3. remove product. \n 4. Display bag. \n 5. Total bill.\n ==>"))

    #to display the shop 
    if choice== 1:
        print("---SHOP DISPLAY---")
        print(shop)
        break

    #to add product to bag
    elif choice== 2:

        print(shop)
        product=input("Enter the name of the product you want to buy:")
        flag=1
        for i in range(len(shop)):
            if shop[i][0]==product:
                pos=i
                flag=1
                break
        if flag==1:
            bag.append(shop[pos][0])
            bill.append(shop[pos][1])
            shop.remove([product,shop[pos][1]])
            print("---SHOP DISPLAY---")
            print(shop)

        else:
            print("not found")

    #to remove the product
    elif choice== 3:
        product=input("Enter the name of the product you want to return:")
        flag=0
        pos=0
        for i in range(len(bag)):
            
            if bag[i]==product:
                pos=i
                flag=1
                break
        if flag==1:
            rem_product=bag.remove(pos)
            rem_price=bill.remove(pos)
            shop.append([rem_product,rem_price])
            print("---SHOP DISPLAY---")
            print(shop)
        else:
            print("ohh...Bag is already empty...")

    #to display bag 
    elif choice== 4:
        if len(bag)!=0:
            print(bag)
        else:
            print("ohh...Bag is already empty...")

    #to display the total bill
    elif choice== 5:
        sum=0
        for i in bill:
            sum=sum+i
        print(bill)
    continue

