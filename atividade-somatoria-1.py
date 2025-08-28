print('|',60*'-','|')
print('| 🩺 Monitoramento de Saúde com Cálculo de IMC ')
print('|',60*'-','|')
nome = input('| Digite seu nome: ')
peso = float(input('| Informe seu peso(Kg): '))
altura = float(input('| Informe sua altura(m): '))
print('|',60*'-','|')
imc = peso / (altura**2)
if imc <= 18.5:
    print(f'| Seu IMC é de {imc:.2f}, você esta abaixo do peso')
elif imc <=24.9:
    print(f'| Seu IMC é de {imc:.2f}, você esta com Peso normal')
elif imc <=29.9:
    print(f'| Seu IMC é de {imc:.2f}, você esta com sobrepeso')
elif imc <=34.9:
    print(f'| Seu IMC é de {imc:.2f}, você esta com obesidade Grau I')
elif imc <=39.9:
    print(f'| Seu IMC é de {imc:.2f}, você esta com obesidade Grau II')
else:
    print(f'| Seu IMC é de {imc:.2f}, você esta com obesidade Grau III (mórbida)')
print('|',60*'-','|')
print(f'| Nome: {nome}')
if imc>30:
    print(f'| Situação: {imc:.2f}, tome mais cuidado com a sua saude!⚠️ ')
else:
    print(f'| Situação: {imc:.2f}, Esta tudo ok!')
print(f'| Obrigada {nome}, seu monitoramento foi concluido!✅')
print('|',60*'-','|')