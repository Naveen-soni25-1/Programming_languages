my_foods = ['pizza', 'burger', 'pasta']
friend_foods = my_foods[:] # passing a copy of the list.

my_foods.append('ice cream')
friend_foods.append('salad')

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)
