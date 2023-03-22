menu = '''
    Escolha qual transformação voce deseja realizar
    Digite:
    (1) - Celsius para Fahrenheit
    (2) - Fahrenheit para Celsius
    (3) - Para sair
    '''


while True:
    aux = input(menu)

    if aux == '1':
        Cel = float(input("Digite o valor de temperatura em °C (sem o °C)\n"))
        Fah = Cel * (9 / 5) + 32
        print(f'Valor em Fahrenheit: {Fah}°F')  

    elif aux == '2':
        Fah = float(input("Digite o valor de temperatura em °F (sem o °F)\n"))
        Cel = (Fah - 32) * (5 / 9)
        print(f'Valor em Celsius: {Cel}°C') 

    elif aux == '3':
        break