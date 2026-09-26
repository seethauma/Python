print("hello")

#L=>E=>G=>B
#Local ->Enclosing->Global->Built-in
def order():
    food = "Briyani"
    print("my order is:", food)
order()

#print(food)

def cart():
    discount =10 # Enclosing
    def checkout():
        print("applying discount:",discount)
    checkout()
    print(discount)
cart()

user_id="seethapalani"

def homepage():
    print("Welcome:",user_id)
def profile():
    print(user_id,"Profile")

homepage()
profile()

delivery_partner="Swiggy" #Global

def restaurant():
    item="Gobi Manchurian" # Enclosing

    def order_quantity():
        quantity=2 # local
        print(f"food order {quantity} {item} using {delivery_partner}")
    order_quantity()
restaurant()

print("Good service:",delivery_partner)

homepage()

print(__file__) # Built-in