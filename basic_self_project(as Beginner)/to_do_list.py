greet= "\tHello user,\n\twelcome to your to_do list"
print(greet.title())

operation="\tif you like to add something to list press[p1].\n\tto exit the list press [e1]"
print(operation.title())

my_list=[]

while True:# use to continue loop infinity
    user_input=input("\twhat do you want to add to the list:".title())
    
    if user_input.lower()=='p1':
        if my_list:#use again because of condition in condition
            for i, task in enumerate(my_list,1):
                print(f"\t{i}.{task}".title())
               #used to store task in list easily
        else:
            print("\tyour list is empty".title())
    elif user_input.lower() =='e1':
            print(f"\texiting your program,goodbye!".title())
            break #used to stop the program
           
    else:
            my_list.append(user_input)
            print(f"\n\t'{user_input.title()}' is added to your list")
            
#there is specific indentation for python code to represent each block separately so it easily to read
        