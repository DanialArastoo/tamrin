product_list = []

while True:
    
    print("1)Add product")
    print("2)Print All product")
    print("3)Find product By name")
    print("4)print sum all")     
    print("0)Exit")

    option = int(input("Enter Option : "))


    if option == 1:
        print("ADD")
        name  = input("Enter product name : ")
        name.lower()
        price = int(input("Enter price : "))

        for p in product_list:
            if p[0] == name:
                print("Duplicate product !!!")
                break
        else:
            product = [name , price]
            product_list.append(product)
            print("\nproduct Saved")

    elif option == 2:
        print("PRINT ALL\n")
        for p in product_list:
            print("name    :", p[0])
            print("product :", p[1])
            print("-" * 50)

    elif option == 3:
        print("FIND BY name\n")
        name = input("Enter product name to Search : ")
        for p in product_list:
            if p[0] == name:
                print("name   :", p[0])
                print("price  :", p[1])
                print("-" * 50)

    elif option == 4:
        print("print sum all\n")
        sm=0
        for p in product_list:
            sm=sm+(p[1])
        print("until now your product price is : ")
        print("sum:",sm)

    elif option == 0:
        if (input("Are you sure (y/n) ?") == "y"):
            print("EXIT")
            break
    else:
        print("INVALID")

    input("\npress enter to continue")
