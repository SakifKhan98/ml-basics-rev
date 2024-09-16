#Example of a basic python file
# print("Basic Functionalities")

# # variables
# test_value = 25
# print(test_value)

# #snake_case Every Character is lower Case

# #input
# user_input = input('Please input something: ')
# print('Hello', user_input, 'Good Morning')


# # Containers
# Tuple=(1,2,3,4,5, 'lisa', 'john') #immutable
# List = [1,2,3,4,5, 'lisa', 'john'] #mutable
# Set = {1,2,3,4,5, 'lisa', 'john'} #unique values
# Dictionary = {'name':'john', 'age':25}

# # Slicing can be confusing

# Looooooop
number_one = 36
number_two = 5
# if number_one > number_two:
#   print('Number One is greater than Number Two')
# elif number_one < number_two:
#   print('Number One is Smaller than Number Two')
# else:
#   print('Number One is equal to Number Two')

# While Loop
# while number_one > number_two:
#   print('Number One is greater than', number_two)
#   number_two += 1
# print("LOOP ENDED")

# For Loop
# test_list = [1,2,3,4,5,6,7,8,9,10]
# for i in test_list:
#   print(i)
#   if i == 5:
#     print("Item is", i)

# # Functions

# def printer(value):
#   print('Hello World', value)

# printer('John')

# Range function
# info = f'Number One is {number_one} and Number Two is {number_two}'
# print(info)

# simple_list = [i for i in range(0,11,1)]
# print(simple_list)

# double_value = lambda x: x*2
# print(double_value(5))

# Classes
class Mage:
  def __init__(self, health, mana):
    self.health = health
    self.mana = mana
    print('Class has been initialized')
    print(f'Health: {self.health} Mana: {self.mana}')
    
  def __len__(self):
    return self.mana
    
mage = Mage(100, 200)
print(len(mage))