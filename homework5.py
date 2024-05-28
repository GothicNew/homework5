#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
immutable_var = (5, 1, 10.6, 12, True, 'Watch', 2)
print(immutable_var)

#Попытайтесь изменить элементы кортежа immutable_var
#immutable_var.append(35)
#Получаем ошибку, так как тип данных кортеж является неизменяемым

mutable_list = [5, 1, 10.6, 12, True, 'Watch', 2]
mutable_list.insert(-1,'Dogs')
print(mutable_list)

