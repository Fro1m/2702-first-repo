# Assignments 7,8,9,10:
my_file = open("words.txt", 'w')
my_file.write('Daniel')
my_file.close()

my_file = open("words.txt", 'r')
print(my_file.read())

my_file = open("words.txt", 'a', encoding='utf-8')
my_file.write('בדיקה')
my_file.close()

