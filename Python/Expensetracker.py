food = {
    "Apple":"50p", 
    "Banana":"70p", 
    "Mango":"1.50p", 
    "Grapes":"30p", 
    "Pear":"90p", 
    "Melon":"1.00p"

} 

Transport = {
    "Bus":"£2.00p", 
    "Car":"£5.00", 
    "Train":"£15.00", 
    "Tram":"£7.50", 
    "Scooter":"0", 
    "Bike":"0"

} 

Entertainment = {
    "Cinema":"£12.00p", 
    "Museams":"70p", 
    "Park":"£1.50p", 
    "Sports":"30p", 
    "TV":"90p", 
    "Games":"£1.00p"

} 



print("Hi and Welcome to expense tracker, this will help you track your daily expenses ")

y = int(input("Enter your expense amount : "))

print(f"£{y} is your expense amount ")


x = input("what is your expense category? :  (Food, Transport, Entertainment) ")


if x == ("Food") or x == ("food"):
    foods = list(food.keys())
    print(foods)
    y=input("Choose a fruit ")
    print(f"It costs {food[y]}")


if x == ("Transport") or x == ("transport"):
    transport = list(Transport.keys())
    print(transport)
    y=input("Choose a Transport ")
    print(f"It costs {Transport[y]}")


if x == ("Entertainment") or x == ("entertainment"):
    Entertainments = list(Entertainment.keys())
    print(Entertainments)
    v=input("Choose an Entertainment ")
    print(f"It costs {Entertainment[v]}")