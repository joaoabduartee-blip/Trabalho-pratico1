print('Bem-vindo a Loja Joao Pedro A.B Duarte')

valor_pedido = float(input('Qual é o valor do seu pedido? '))
quantidade_parcela = int(input('Em quantas vezes deseja dividir(parcelar) o seu pedido? '))

if quantidade_parcela < 4:
  juros = 0 / 100
  print('Juros do parcelamento: 0%')
elif 4 <= quantidade_parcela < 6:
  juros = 4 / 100
  print('Juros do parcelamento: 4%')
elif 6 <= quantidade_parcela < 9:
  juros = 8 / 100
  print('Juros do parcelamento: 8%')
elif 9 <= quantidade_parcela < 13:
  juros = 16 / 100
  print('Juros do parcelamento: 16%')
else:
  juros = 32 / 100
  print('Juros do parcelamento: 32%')

valor_parcela = valor_pedido * (1 + juros) / quantidade_parcela

valor_totalparcelado = valor_parcela * quantidade_parcela

print(f'Valor total parcelado: {valor_totalparcelado:.2f}')
print(f'Valor da parcela: {valor_parcela:.2f}')
print('Obrigado, volte sempre!')

print('Joao Pedro A.B Duarte')
