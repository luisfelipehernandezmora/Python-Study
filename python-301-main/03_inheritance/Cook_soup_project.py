from Ingredients import *

print(f"Hello! Welcome to this python cooking project! \n")
lista=[]
weigth=0
# while True:
#     ing=input(f"Which are the ingredients? (When finished type 'Done') ")
#     if ing=="Done":
#         print(f"Ok, let's cook it!")
#         break
#     quant=int(input(f"How many grams of {ing} you will add? "))
#     is_spice=input(f"Is this a Spice (type 'Yes'), or not? ")
#     if is_spice=="Yes":
#         taste=input(f"Which is the taste of the spice? ")
#         ing=Spice(ing,quant,taste)
#     else:
#         ing=Ingredient(ing,quant)
#     lista.append(ing)
# print(f"Ok, you are done with the ingredients, you have: {lista}")


tomato=Ingredient("Tomatoes", 200)
potato=Ingredient("potatoes", 200)
water=Ingredient("water", 600)
tofu=Ingredient("tofu", 250)


lista=[tomato,potato,water,tofu]
for elem in lista:
    unit=elem.amount
    weigth+=unit
portions=int(weigth/225) #225 grams or 8 oz. is the average soup portion size 
print(f"So you have food for {portions} people")
