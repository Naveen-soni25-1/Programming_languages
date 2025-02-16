def print_message(unsend,sended):
     """Print unsend message and move it
     to sended list"""
     print("enter 'done' when finish:".title())
     
     while True:#take user input 
         user = input("\nenter message: ".title())
         if user.lower() == 'done':
             break
         else:
              unsend.append(user)
              
         #display user input and move it to sended  list
         current_message= unsend.pop()
         print(f"sending message:-“{current_message}”".title())
         sended.append(current_message)    
         
 # show sended message        
def show_message(sended):
    if unsend:
        print("\nfollowing message has been sended:")
        for message in sended:
            print(message)

unsend = []
sended = []
print_message(unsend,sended)
show_message(sended)