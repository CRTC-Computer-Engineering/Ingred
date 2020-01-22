'''
program Ask User for food and give their user nutritional information based on 
the recipe's ingredients
'''
#declare globals
flour = 0
yeast = 0
egg = 0
baking_powder = 0
butter = 0
water = 0
milk = 0
sugar = 0
brown_sugar = 0
salt = 0
baking_soda = 0

ingredients_Dict = {"calories":0, "fat":0, "cholesterol":0, "sodium":0, 
"carbohydrates":0, "potassium":0, "protein":0}
ingredientsList = ["Flour","Yeast","Egg","Baking_Powder","Butter","Water"]
ingredientsList2 = ["Milk","Sugar","Brown_Sugar","Salt","Baking_Soda"]
user_uses = int(input("How many ingredients are you using from the list?: "))
# ask uses for loop to repeat how much ingredance user chose op use 
print ("Note: You must capitalize")
for i in range(user_uses):
    user_ingredients = input("What ingredients do you want to use: ")
    if user_ingredients == "Flour":
        #print ("Serving size - One cup of all Purpose white flour")
        #global flour
        flour = float(input("How many cups of flour are there?: "))
        calories = (455 * flour)
        fat = (1.2 * flour)
        cholesterol = (0 * flour)
        sodium = (.003 * flour)
        carbohydrates = (95.4 * flour)
        potassium = (.134 * flour)
        protein = (12.9 * flour)
    elif user_ingredients == "Yeast":
        #print ("Serving Size - 1/4 of a cup")
        #global yeast
        yeast = float(input("How many cups of yeast are there?: "))
        calories = (60 *(yeast / 4))
        fat =  (.5 *(yeast / 4))
        cholesterol = (0 *(yeast / 4))
        protein = (8 *(yeast / 4))
        sodium = (.025 *(yeast / 4))
        potassium = (.020 *(yeast / 4))
        carbohydrates = (5 *(yeast / 4))
    elif user_ingredients == "Egg":
        #print ("Serving Size - One Large Egg")
        #global egg
        egg = float(input("How many eggs are there?: "))
        egg = egg / 4
        calories = (70 * egg)
        fat = (5 * (egg / 4))
        cholesterol = (.195 * egg)
        protein = (6 * egg)
        potassium = (.063 * egg)
        sodium = (.065 * egg)
        carbohydrates = (1 * egg)
        egg = egg * 4
    elif user_ingredients == "Baking Powder":
        #print ("Serving Size - 1/4 tsp")
        #global baking_powder
        baking_powder = float(input("How many teaspoons of baking milk powder are there?: "))
        calories = (0 * (baking_powder / 4))
        fat = (0 * (baking_powder / 4))
        cholesterol = (0 * (baking_powder / 4))
        protein = (0 * (baking_powder / 4))
        potassium = (.001 * (baking_powder / 4))
        sodium = (.110 * (baking_powder / 4))
        carbohydrates = (0 * (baking_powder / 4))
    elif user_ingredients == "Butter":
        #print ("Serving Size - 1 Tbsp")
        #global butter
        butter = float(input("How many tablespoons of butter are there?: "))
        calories = (100 * (butter / 16))
        fat = (11 * (butter / 16))
        cholesterol = (.030 * (butter / 16))
        protein = (0 * (butter / 16))
        potassium = (.003 * (butter / 16))
        sodium = (.120 * (butter / 16))
        carbohydrates = (0 * (butter / 16))
    elif user_ingredients == "Water":
        #print ("Serving Size - 1 cup in 8 fluid ounces")
        #global water
        water = float(input("How many cups of water are there?: "))
        calories = 0
        fat = 0
        cholesterol = 0
        protein = 0
        potassium = 0
        sodium = 0
        carbohydrates = 0
    elif user_ingredients == "Milk":
        #print ("Serving Size - 1 cup")
        #global milk
        milk = float(input("How many cups of milk are there?: "))
        calories = (100 * milk)
        fat = (0 * milk)
        cholesterol = (.005 * milk)
        protein = (10 * milk)
        potassium = (.366 * milk)
        sodium = (.150 * milk)
        carbohydrates = (15 * milk)
    elif user_ingredients == "Sugar":
        #print ("Serving Size - 1 tsp")
        #global sugar
        sugar = float(input("How many cups of sugar are there?: "))
        calories = (16 * (sugar * 48))
        fat = (0 * (sugar * 48))
        cholesterol = (0 * (sugar * 48))
        protein = (0 * (sugar * 48))
        potassium = (.133 * (sugar * 48))
        sodium = (0 * (sugar * 48))
        carbohydrates = (4.2 * (sugar * 48))
    elif user_ingredients == "Brown Sugar":
        #print ("Serving Size - 1 tsp unpacked")
        #global brown_sugar
        brown_sugar = float(input("How many cups of brown sugar are there?: "))
        calories = (11 * (brown_sugar * 48))
        fat = (0 * (brown_sugar * 48))
        cholesterol = (0 * (brown_sugar * 48))
        protein = (0 * (brown_sugar * 48))
        potassium = (.040 * (brown_sugar * 48))
        sodium = (.001 * (brown_sugar * 48))
        carbohydrates = (2.9 * (brown_sugar * 48))
    elif user_ingredients == "Salt":
        #print ("Serving Size - 1 tbsp")
        #global salt
        salt = float(input("How many tablespoons of salt are there?: "))
        calories = (0 * salt)
        fat = (0 * salt)
        cholesterol = (0 * salt)
        protein = (0 * salt)
        potassium = (6.976 * salt)
        sodium = (.001 * salt)
        carbohydrates = (0 * salt)
    elif user_ingredients == "Baking Soda":
        #print ("Serving Size - 1 tsp")
        #global baking_soda
        baking_soda = float(input("How many teaspoons of baking soda are there?: "))
        calories = (0 * baking_soda)
        fat = (0 * baking_soda)
        cholesterol = (0 * baking_soda)
        protein = (0 * baking_soda)
        potassium = (0 * baking_soda)
        sodium = (1.259 * baking_soda)
        carbohydrates = (0 * baking_soda)
    else:
        print ("You might have typed the Ingredients wrong. Please check again")
    #Adds the nuterance number for ingred to dict 
    ingredients_Dict["calories"] = ingredients_Dict["calories"] + calories
    ingredients_Dict["fat"] = ingredients_Dict["fat"] + fat
    ingredients_Dict["cholesterol"] = ingredients_Dict["cholesterol"] + cholesterol
    ingredients_Dict["sodium"] = ingredients_Dict["sodium"] + sodium
    ingredients_Dict["carbohydrates"] = ingredients_Dict["carbohydrates"] + carbohydrates
    ingredients_Dict["potassium"] = ingredients_Dict["potassium"] + potassium
    ingredients_Dict["protein"] = ingredients_Dict["protein"] + protein
print (" ")
#prints all the ingred and it's value
print ("Total Calories: "+str(ingredients_Dict["calories"]))
print ("Total Fat: "+str(ingredients_Dict["fat"])+" g")
print ("Total Cholesterol: "+str(ingredients_Dict["cholesterol"])+" g")
print ("Total Sodium: "+str(ingredients_Dict["sodium"])+" g")
print ("Total Carbohydrates: "+str(ingredients_Dict["carbohydrates"])+" g")
print ("Total Potassium: "+str(ingredients_Dict["potassium"])+" g")
print ("Total Protein: "+str(ingredients_Dict["protein"])+" g")


#basic ingredients
print ("NOTE : This program will only list the most common ingredients")
print ("If there is an ingredient you do not use, enter '0'")
print (" ")
#get values


#baking_powder = float(input("How many teaspoons of baking powder are there?: "))    #COME BACK TO THIS

#rounding units
salt = float(round(salt, 3))
baking_soda = float(round(baking_soda, 3))
baking_powder = float(round(baking_powder, 3))

#define ingredient_cups
new_ingredients_cups = 0

#list manipulation
ingredients_list_numbers = []

#add only needed ingredients
if flour > 0:
    ingredients_list_numbers.append(flour)
if yeast > 0:
    ingredients_list_numbers.append(yeast)
if egg > 0:
    ingredients_list_numbers.append(egg)
if baking_powder > 0:
    ingredients_list_numbers.append(baking_powder)
if butter > 0:
    ingredients_list_numbers.append(butter)
if water > 0:
    ingredients_list_numbers.append(water)
if milk > 0:
    ingredients_list_numbers.append(milk)
if sugar > 0:
    ingredients_list_numbers.append(sugar)
if brown_sugar > 0:
    ingredients_list_numbers.append(brown_sugar)
if salt > 0:
    ingredients_list_numbers.append(salt)
if baking_soda > 0:
    ingredients_list_numbers.append(baking_soda)
if new_ingredients_cups > 0:
    ingredients_list_numbers.append(new_ingredients_cups)

#UI enhancements:
print (" ")
print("Note that any ingredients not specifically mentioned are negated")
print("Your ingredients from least use to most used are:")

#dictionary &replace numbers with words
recipe_dict = {"Flour":flour, "Yeast":yeast, "Egg":egg, "Baking Powder":baking_powder, "Butter":butter, "Water":water, "Milk":milk, "Sugar":sugar, "Brown Sugar":brown_sugar, "Salt":salt}

# Create a list of tuples sorted by index    
recipe_dict = sorted(recipe_dict.items() ,  key=lambda x: x[1])

# Iterate over the sorted sequence
for elem in recipe_dict :
    print(elem[0] , ":" , elem[1])

ingredients_list_numbers.sort()
ingredients_list_numbers.reverse()
str(ingredients_list_numbers)
