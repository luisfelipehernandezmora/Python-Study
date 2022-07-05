from unicodedata import name
import unittest
import Access_the_recipes

class Test_that_recipes_access_correctly(unittest.TestCase):

    def Test_the_correct_recipe_is_open(self):
        self.assertEqual((Access_the_recipes.look_recipe('Rich Chocolate Cake with Ganache Glaze')),('Rich Chocolate Cake ...ache Glaze', 'by cookingsheri','INGREDIENTS\nCake\n* 1 cup freshly brewed hot coffee\n\n1/2 cup Unsweetened natural cocoa powder\n3/4 cup packed light brown sugar\n1/2 cup full fat sour cream \n2 teaspoons vanilla extract\n8 tablespoons (1 stick) unsalted butter, at room temperature\n1 1/4 cups granulated sugar\n2 eggs\n1 1/4 cups all-purpose flour\n3/4 teaspoon baking soda\n1 teaspoon table salt\n\nChocolate Ganache\n* 8 ounces of semi sweet chocolate chips \n\nHalf cup of heavy cream \n\nPREPARATION\n1. Preheat the oven to 350°F. Prepare a 10-inch round cake pan by greasing it with cooking spray and then lining the bottom with parchment paper.\n2. To make cake, pour the hot coffee into a medium bowl and stir in the cocoa powder until it dissolves. Stir in the brown sugar, followed by the sour cream and the vanilla. Stir thoroughly.\n3. Using a mixer, beat the butter and granulated sugar on medium speed until light-yellow and fluffy,Add the eggs and mix for 2 minutes.\n4. In a medium bowl, whisk together the flour, baking soda, and salt. On low speed, mix in a third of the flour mixture and half of the coffee mixture. Add another third of the flour mixture and all the remaining coffee mixture. Using a rubber spatula, fold in the remaining flour mixture until all of the ingredients are fully incorporated. Pour the batter into the prepared cake pan.\n5. Bake for 25 minutes. Rotate the pan in the oven and bake for 25 more minutes. Remove from oven and let cook for at least 20 mins. Then turn the cake out onto a clean plate, remove the parchment, and turn the cake back over onto a wire rack. Let the cake cool completely.\n6. Place the  chocolate chips into a bowl and set aside.\n7.Heat the heavy cream in a quart-sized,\nmicrowavable container and microwave for 3 to 4 minutes on high, or heat on stovetop medium heat until it just begins to simmer. Pour the cream over the chocolate chocolate chips and let stand for 2 minutes. Mix until smooth and pour over cooled cake. Let ganache set for at least 15 mins. Slice and serve!\nIf you’d like to watch me make this cake, you can check it out here!\n'))



if __name__=="__main__":
    unittest.main()



