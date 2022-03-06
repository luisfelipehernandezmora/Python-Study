class Ingredient():
    """Models the food item as an ingredient"""
    def __init__(self,name, amount):
        self.name=name
        self.amount=amount
    def expire(self):
        """Expires the ingredient"""
        print(f"Oh no! these {self.name} got expired!")
        self.name="expired" +self.name +":/" #Here you change the name from tomatoes to expired tomatoes
    def __str__(self):
        return(f"{self.name}({self.amount})")
        #return(f"There are {self.amount} {self.name}")
    def __repr__(self):
        return(f"Ingredient(name={self.name},amount={self.amount})")
    def __add__(self , other):
        """Combine two ingredients"""
        new_name = self.name + other.name
        new_amount=self.amount + other.amount
        return (Ingredient(name=new_name, amount=new_amount))


papas=Ingredient("potatoes",5)

cookies=Ingredient("cookies",2)
water=Ingredient("Special water",3)

zanahorias=papas+cookies

print("",papas.name,papas.amount,"\n",cookies.name,cookies.amount,"\n",water.name,water.amount,"\n",zanahorias.name,zanahorias.amount)

print(papas)
print(zanahorias)