def fizzbuzz(numero):
    numero = int(numero)
    if numero < 1:
	raise ValueError()

    output = []
    for a in range(1, numero + 1):
        if a % 15 == 0:
	   valor = 'FizzBuzz'
	elif a % 3 == 0:
           valor = 'Fizz'
	elif a % 5 == 0:
           valor = 'Buzz'
        else:
            valor = a
        output.append(valor)
    return output


