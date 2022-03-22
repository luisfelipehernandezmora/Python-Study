import webbrowser

class Apartment:
    def __init__(self, l, w, h):
        self.length = l
        self.height= h
        self.width = w
        self.square_area = l * w * h


class Ingredient:
    """Models the food item as an ingredient"""
    def __init__(self,name, amount):
        self.name=name
        self.amount=amount
        self.expired = False
        # self.amount=int(input(f"Type the amount of {self.name}"))
         

    def expire(self):
        """Expires the ingredient"""
        print(f"Oh no! these {self.name} got expired!")
        # self.name="expired " +self.name +" :/" #Here you change the name from tomatoes to expired tomatoes
        self.expired = True
    
    def __str__(self):
        return(f"{self.name}, amount: {self.amount}, expired: {self.expired}")
            
    # def __repr__(self):
    #     return(f"Ingredient(name={self.name},amount={self.amount})")
    
    def __add__(self , other):
        """Combine two ingredients"""
        if self.name!=other.name:
            new_name = f"{self.name} and {other.name}"
        else:
            new_name=self.name
        new_amount=self.amount + other.amount

        return (Ingredient(name=new_name, amount=new_amount))

    def get_info(self):
        """Make a wikipedia search for this ingredient and open the page"""
        url=f"https://en.wikipedia.org/wiki/{self.name}"
        webbrowser.open(url, new=0, autoraise=True)

class Spice(Ingredient):
    """Model a spice to flavor the food!"""
    
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste=taste

    # overloading the super class method
    def expire(self):
        """ spices don't expire"""
        print("spices don't expire")
        return False
        
        # if self.name=="salt":
        #     print(f"Nonono, salt don't expire")
        #     return(None)
        # elif self.name !="salt":
        #     print(f"Your {self.name} is expired, probably still good to use")
        #     self.name="old"+self.name

banana=Ingredient("Bananas",5)
print(banana)
banana.expire()

# a = 0
# b = 10
# c = 'Luis'


# def do_something(b):
    
#     print (a)
#     Local
#     Enclosed
#     Global
#     Builtin