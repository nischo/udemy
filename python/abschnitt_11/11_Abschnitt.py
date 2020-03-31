myfile = open('fruits.txt', 'r')

print(myfile.read())
myfile.close()

print('##############3')

with open('fruits.txt') as myfile:
    content = myfile.read()

print(content)