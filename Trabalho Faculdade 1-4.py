print('Bem vindo a loja do Luiz Fernando Valentim') #apresentação do sistema

valorProduto = float(input('Entre com o valor do produto: ')) #valor do produto que o cliente comprou
qtdProduto = int(input('Entre com a quantidade de produtos: ')) #quantidade de produtos
valorFinal = valorProduto * qtdProduto #cálculo para saber o valor de todos produtos

if (qtdProduto <= 4): #sem desconto
    valorDesconto = valorFinal - valorFinal 

elif (qtdProduto >= 5) and (qtdProduto <= 19):
     valorDesconto = valorFinal - valorFinal * 0.03 #3% de desconto

elif (qtdProduto >= 20) and (qtdProduto <= 99):
     valorDesconto = valorFinal - valorFinal * 0.06 #6% de desconto
else:
     valorDesconto = valorFinal - valorFinal * 0.1 #10% de desconto

print('O valor sem desconto foi: {}'.format(valorFinal)) #resultado dos cáculos sem desconto
print('O valor com desconto foi: {}'.format(valorDesconto)) #resultado dos cáculos com desconto
