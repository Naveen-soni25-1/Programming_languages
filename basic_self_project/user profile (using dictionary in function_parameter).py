def build_profile(first,last,**user_info):
    """building a user profile"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    print("\nprofile contains the following items: ".title())
    for user,value in user_info.items():
        print(f"{user}:{value}".title())
        
#creating a loop asking for user input       
while True:
    user_details = {}
    
    f_name = input("\nfirst name: ".title())
    l_name = input("last name: ".title())
    users = input("information name: ".title())
    
    user_1 = input(f"{users}: ".title())
    user_details[users] = user_1
    ask = input("want to continue(yes/no): ".title())
    if ask.lower() == 'no':
        break        
build_profile(f_name,l_name,**user_details)