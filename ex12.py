preço = float(input('qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava {} na promoção vai custar {:.2f}'.format(preço, novo))
