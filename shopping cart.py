products={
    1:{'name':"bananna","price":30},
    2:{'name':"Apple","price":150},
    3:{'name':"milk","price":60},
    4:{'name':"ots","price":100},
    5:{'name':"chicken","price":250},
}
cart={}
def show_products():
    print("Avilable products:")
    for pid,details in products.items():
        print("{}----{}------{}".format(pid,details['name'],details['price']))
def view_cart():
    print("=====my cart=====")
    if not cart:
        print("cart is empty:")
    else:
        total=0
        for pid,item in cart.items():
            name=item['name']
            price=item['price']
            qty=item['quantity']
            sub_total=qty*price
            total=total+sub_total
            print("{} {} x {} -{}/-".format(pid,name,qty,sub_total))
        print("total {}/-".format(total))
def add_to_cart():
    show_products()
    try:
        pid=int(input("enter product id to add:"))
        if pid in products:
            qty=int(input("enter quanty:"))
            if pid in cart:
                cart[pid]['quantity']+=qty
            else:
                cart[pid]={
                    'name':products[pid]['name'],
                    'price':products[pid]['price'],
                    'quantity':qty
                }
            print("{} X {} added into cart".format(qty,products[pid]['name']))
        else:
            print('inavalid product id')
    except ValueError:
        print("invalid input")
def remove_from_cart():
    view_cart()
    if not cart:
        return
    try:
        pid = int(input("enter product id to remove:"))
        if pid in cart:
            qty = int(input("enter quanty:"))
            current_qty=cart[pid]['quantity']
            if qty== current_qty:
                del cart[pid]
                print("item deleted form cart\n")
            elif qty < current_qty:
                cart[pid]['quantity']-=qty
                print("cart updated succesfully\n")
            else:
                print("you only have{}".format(current_qty))
        else:
            print("item not in cart")
    except ValueError:
        print("inavalid input:")
def checkout():
    view_cart()
    if cart:
        confim=input("process to check (y/n):")
        if confim == 'y':
            print("thank you for shopping\n")
        else:
            print("check out cancelled\n")
def menu():
    while True:
        print("\n============= shooping cart=============")
        print("1.views products")
        print("2.Add to cart")
        print("3.Remove from cart")
        print("4.view cart")
        print("5.checkout")
        print("6.exit")
        choice=input("enter your choice:")
        if choice=='1':
            show_products()
        elif choice=='2':
            add_to_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            view_cart()
        elif choice == '5':
            checkout()
        elif choice == '6':
            print("exiting.GOOD BYE!")
        else:
            print("invalid choice please try again")
menu()