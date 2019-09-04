# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    usd_to_arg_rate = 58

    return usd_to_arg_rate * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte dolares a pesos argentinos.')
    print('')

    ammount = float(raw_input('Ingresa la cantidad de dolares que quieres convertir: '))

    result = foreign_exchange_calculator(ammount)

    print('${} dolares son ${} pesos argentinos'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()
    print('Final {}')
