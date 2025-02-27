def esPrimo(num):
    i = 0
    for n in range(2, num):
        if num % 2 != 0:
            i += 1
    
    if i > 0:
        return False
        
    return True

num = input('Ingrese un numero para ver si es primo')

if esPrimo(num):
    print(f'el numero {num} es primo')
else:
    print(f'el numero {num} no es primo')