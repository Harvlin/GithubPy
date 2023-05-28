# Recipe CRUD Operations: Users should be able to perform basic CRUD (Create, Read, Update, Delete) operations on recipes. 
# They should be able to add a new recipe, view the details of a recipe, and delete recipes.
recipes = {}
def add_recipes():
      dish_name = input("Enter the name of your dish: ")
      dish_ingredient = input("Enter your ingredient in a single line(comma separated): ")
      dish_instruction = input("Enter the instruction in one single line(comma separated step by step): ")
      recipes[dish_name] = {"Ingredient: ", dish_ingredient, " Dish instruction: ", dish_instruction}
      print("Addes successfully.")
def view_recipes():
      dish_name = input("Enter the name of your dish: ")
      recipe = recipes.get(dish_name)
      if recipe:
            print("Recipes: {dish_name}")
            print("Ingredient: ", ", ".join(recipe["dish_ingredient"]))
            print("Instructions: ", ", ".join(recipe["dish_instruction"]))
      else:
            print("Recipe not found")
def del_recipes():
      dish_name = input("Enter the name of your dish: ")
      if dish_name in recipes:
            del recipes[dish_name]
            print("Deleted successfully.")
      else:
            print("Dish not found.")
      
def main():
      while True:
            user_choice = eval(input("1. Add recipes\n2. Delete recipes\n3. View_recipes\n4. Quit\nEnter your choice: "))
            if user_choice == 1:
                  add_recipes()
            elif user_choice == 2:
                  del_recipes()
            elif user_choice == 3:
                  view_recipes()
            elif user_choice == 4:
                  break
            else:
                  print("Invalid Input")
main()