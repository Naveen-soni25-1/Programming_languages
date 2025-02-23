def show_sandwiches(ingredients):
    """display the items customer what's in sandwiches"""
    if ingredients:
        print("\nMaking a sandwiche with the following ingredients ".title())
    for items in ingredients:
        print(f"-{items}")
        
print("when done enter 'done".title())  
#creating a list before loop so we don't get undefine error 
ingredients = []
  
#Creating a loop that ask for user input
while True:
    ask = input("What ingredients do you want to add: ".title()).strip().title()
    if ask:
        if ask.lower() == 'done':
            break
        else:
            ingredients.append(ask)
            print(f"done adding!:“{ask.title()}”\n".title())
    else:
        continue     

show_sandwiches(ingredients)
         
    
    