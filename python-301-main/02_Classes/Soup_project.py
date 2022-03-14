from Ingredients import Ingredient

zuchini=Ingredient("Zuchini",5)
pumpkin=Ingredient("Pumpkins",4)
bread=Ingredient("Ciabata bread",2)
milk=Ingredient("Skim milk",2)

items=[zuchini,pumpkin,bread,milk]

for i in items:
    i.get_info()



