menu = {
    'Pizza':250,
    'Burger':100,
    'Salad':120,
    'Coffee':80,
    'FrenchFries':90
}

print("*-WELCOME TO KITKAT RESTAURANT-*")
print("1.Pizza-250rs\n2.Burger-100rs\n3.Salad-120rs\n4.Coffee-80rs\n5.FrenchFries-90rs")
item1 = input("Enter the item you want :")
totalBill = 0
quantity = 0

if item1 in menu:   
    
    quantity = int(input("Enter the quantity :"))
    print(f"Your selected item {item1} is added to order!")
    totalBill += quantity * menu[item1]
else:
    print(f"The selected item {item1} is not avaliable yet!!")

item2 = input("Do you want to add something else (Y/N)? :").upper()
if item2=="Y":
    another_order = input("Enter the second order name :")
    if another_order in menu:
        
        quantity1 = int(input("Enter the quantity :"))
        print(f"Your selected item {another_order} is added to order!")
        
        totalBill += quantity1 * menu[another_order]
    else:
        print(f"The selected item {item2} is not avaliable yet!!")

print(f"TOTAL BILL : {totalBill}")
print("---THANK YOU, VISIT AGAIN!---")

