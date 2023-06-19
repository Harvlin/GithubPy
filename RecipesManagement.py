# Make a recipe management
# features including: Add, delete, view
recipes = {}


def add_recipe():
    name_dish = input("Enter the recipe name: ")
    ingredients_dish = input("Enter the ingredients (comma separated): ").split(",")
    instructions_dish = input("Enter the instructions (comma separated): ")
    recipes[name_dish] = {
        "Dish ingredients": ingredients_dish, "Dish instructions": instructions_dish}
    print("Recipe added successfully")


def view_recipe():
    name_dish = input("Enter the recipe name: ")
    recipe = recipes.get(name_dish)
    if recipe:
        print(f"\nRecipe: {name_dish}")
        print("Ingredients: ", ", ".join(recipe["Dish ingredients"]))
        print("Instructions: ", recipe["Dish instructions"])
    else:
        print("Dish not found")


def delete_recipe():
    name_dish = input("Enter the dish name: ")
    if name_dish in recipes:
        del recipes[name_dish]
        print("Recipe deleted successfully")
    else:
        print("Dish not found")


def main():
    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. Delete Recipe")
        print("4. Quit")
        user_input = input("Enter your choice by numbers: ")
        if user_input == "1":
            add_recipe()
        elif user_input == "2":
            view_recipe()
        elif user_input == "3":
            delete_recipe()
        elif user_input == "4":
            break
        else:
            print("Invalid choice")
            continue


main()
