print("Это первая строка")
print("Это вторая строка")
print("Это третья строка")

x=10
if x<10:
    print("Число x меньше десяти")
elif x==10:
    print("Число x равно 10")
elif x>10:
    print("Число x больше 10")

y=25

if y<=10:
    print("Число y меньше или равно 10")
elif y>10 and y<=25:
    print("Число y больше 10, но меньше или равно 25")
elif y>25:
    print("Число y больше 25")

x1 = 50
x2 = 20
print("Остаток от деления равен:", x1%x2)

y1 = 40
y2 = 7
print("Частное равно: ",y1/y2)

age = 10
if age<18:
    print("Подрости немного")
elif age>18:
    print("Добро пожаловать")

in_age = input ("Укажите возраст: ")
int_age = int(in_age)
if int_age > 18:
    print ("Пожалуйста, заходите!")
else:
    print ("Тебе ещё надо подрости малыш")
