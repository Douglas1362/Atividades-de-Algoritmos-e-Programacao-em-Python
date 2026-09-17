# 12. Desconto em uma compra 
# Uma loja oferece descontos de acordo com o valor da compra: 
# Até R$ 100,00       
# → sem desconto 
# De R$ 100,01 a 500  → 10% de desconto 
# Acima de R$ 500     → 20% de desconto 
# Leia o valor da compra e mostre: 
# ● valor original; 
# ● percentual de desconto; 
# ● valor do desconto; 
# ● valor final da compra.

compra = float(input("Digite o valor da Comrpa: R$"))

desconto10 = compra * 0.10
desconto20 = compra * 0.20

valorf10 = compra - desconto10
valorf20 = compra - desconto20

if compra <= 100.00:
    print("Compra sem desconto, R$", compra)
elif compra < 500.00:
    print("Sua compra teve um desconto de 10% = R$", desconto10, "valor final da compra sera de: R$", valorf10)
elif compra >= 500.00:
    print("Sua compra teve um desconto de 20% = R$", desconto20, "valor final da compra sera de: R$", valorf20)