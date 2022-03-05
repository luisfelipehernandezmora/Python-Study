class Ingredient():
    """Models the food item as an ingredient"""
    def __init__(self,name, amount):
        self.name=name
        self.amount=amount
    def expire(self):
        """Expires the ingredient"""
        print(f"Oh no! these {self.name} got expired!")
        self.name="expired" +self.name +":/" #Here you change the name from tomatoes to expired tomatoes
i=Ingredient()

print(i.name)