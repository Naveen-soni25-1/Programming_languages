# An Empty  dictionary for people
favorite_language = {}

# Greetings to people 
print("welcome to poll")
print("to see the poll result,enter [show]".title())

while True: # An loop till break
    name = input("\nwhat is your name: ".title()).strip()
    
    if name.lower() == 'show': # To see reault
        print("\nHere's poll result:".title())
        for i ,key in enumerate(favorite_language,start =1): # to print poll in formate
            print(f"{i}.{key}:{favorite_language[key]}")
        break
           
    elif name in favorite_language.keys():
        add = input("do you want to add more(yes/no): ".title()).strip()
        if add == 'yes':
            inp = input("enter then :-".title()).strip()
            favorite_language[name].append(inp)
            continue 
        elif add == 'no': 
            continue
          
    else:
        ask = input("what is your favourite language: ".title()).strip()
        favorite_language[name] = [ask]