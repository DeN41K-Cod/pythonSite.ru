#!C:/Users/User/AppData/Local/Programs/Python/Python37-32/python.exe
# -*- coding: utf-8 -*

print("Content-Type: text/html\n")
print("<html><head>")
print('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
print("<link rel='stylesheet' href='/css/style.css'>")
print("<title>Сайт на Питоне</title>")
print("</head><body>")

import cgi

print("<br><br>")
print("<div class='container'>")
print("<div class='alert alert-light'>")
print("<a style='text-decoration: none; color: black' href='/'><h1>Сайт на Питоне</h1></a>")
print("</div>")
print("</div>")

print("<br>")
print("<div class='container'>")
print("<div class='alert alert-light'>")

class Arithmetic:
	def __init__(self, x, y, operation):
		self.x = x
		self.y = y
		self.operation = operation
	
	def arithmetic(self, x, y, operation):
		if self.operation == '+':
			return self.x + self.y
		elif self.operation == '-':
			return self.x - self.y
		elif self.operation == '*':
			return self.x * self.y
		elif self.operation == '**':
			return self.x ** self.y
		else:
			return self.x / self.y

print("<br>")
print("<form method='POST' action='/'>")

print("<p>Введите первое число: </p>")
print("<input class='form-control' id='firstNumber' type='number' min='1' value='1' name='x'>")
print("<br><br>")

print("<p>Введите второе число: </p>")
print("<input class='form-control' id='secondNumber' type='number' min='1' value='1' name='y'>")
print("<br><br>")

print("<p>Введите вид операции: </p>")
print("<select class='form-control' id='operation' name='operation'>")
print("<option value='+' selected>Прибавить</option>")
print("<option value='-'>Вычесть</option>")
print("<option value='*'>Умножить</option>")
print("<option value='**'>Возвести в степень</option>")
print("<option value='/'>Поделить</option>")
print("</select>")
print("<br><br>")
print("<input class='btn btn-outline-dark' type='submit' id='sbmt' name='sbmt' value='Показать результат'>")
print("<br><br>")
print('<script src="js/script.js" charset="utf-8"></script>')
print("</form>")

form = cgi.FieldStorage()
x = int(form.getvalue('x'))
y = int(form.getvalue('y'))
operation = form.getvalue('operation')

arit = Arithmetic(x, y, operation)

result = arit.arithmetic(x, y, operation)

print("<p>Результат: %s</p>" % result)

print("</div>")
print("</div>")

print('<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>')
print('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>')

print("</body></html>")
