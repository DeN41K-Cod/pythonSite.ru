var firstNumber = document.querySelector('#firstNumber');
var secondNumber = document.querySelector('#secondNumber');
var operation = document.querySelector("#operation");

var sbmt = document.querySelector('#sbmt');

sbmt.addEventListener('click', function() {
	alert("+ это прибавление,\n - это вычитание,\n * это умножение,\n ** это возведение в степень,\n / это деление");
	alert('Первое число: ' + firstNumber.value + ';\n второе число: ' + secondNumber.value + ';\n Вид операции: ' + operation.value);
});