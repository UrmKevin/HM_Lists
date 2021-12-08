valik=''
word='Programm'
word_l=list(word) # превращает переменную в список
print(word,word_l)
while True:
	valik = int(input('\nChoose:\n1. len(S)\n2. S.isdigit()\n3. S.isalpha()\n4. S.islower()\n5. S.isupper()\n6. S.upper()\n7. S.lower()\n8. S.capitalize()\n9. S.istitle()\n10. S.isspace()\n'))
	if valik == 1:
		print('In list ',len(word_l),' symbols') #Длина строки
	elif valik == 2:
		if word.isdigit()==True: #Состоит ли строка из цифр
			print('This list has at least one number')
		else:
			print('There is no numbers in this list')
	elif valik == 3:
		if word.isalpha()==True: #Состоит ли строка из букв
			print('This list has at least one letter')
		else:
			print('There is no letters in this list')
	elif valik == 4:
		if word.islower()==True: #Состоит ли строка из символов в нижнем регистре
			print('This list has at least one letter with lower register')
		else:
			print('There is no letters with lower register in this list')
	elif valik == 5:
		if word.isupper()==True: #Состоит ли строка из символов в верхнем регистре 
			print('This list has at least one letter with upper register')
		else:
			print('There is no letters with upper register in this list')
	elif valik == 6:
		print(word.upper()) #Преобразование строки к верхнему регистру
	elif valik == 7:
		print(word.lower()) #Преобразование строки к нижнему регистру
	elif valik == 8:
		print(word.capitalize()) #Переводит первый символ строки в верхний регистр, а все остальные в нижний
	elif valik == 9:
		if word.istitle()==True: #Начинаются ли слова в строке с заглавной буквы
			print('This list has capital letter')
		else:
			print("There is no capital letters in this list")
	elif valik == 10:
		if word.isspace()==True: #Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки"('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция"('\v'))
			print('There is at least one space in this list')
		else:
			print("There is no spaces in this list")
	else:
		print('Invalid input!')
