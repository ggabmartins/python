n1 = float(input("Digite a nota da sua primeira atividade: "))
n2 = float(input("Digite a nota da sua segunda atividade: "))
n3 = float(input("Digite a nota da sua terceira atividade: "))
if 0 > n1 or n2 or n3 > 10: 
    print("Nota inválida, por favor insira um valor de 0 a 10.")
else: 
    m = (n1+n2+n3)/3
    print("Média: ", m)
    
    if m >= 6:
        print("Aprovado direto.")
    else:
        print("Nota insuficiente para reprovação direta.")
        if m >= 3:
            print("Recuperação.")
        else: 
             print("Reprovado direto.")
    
    
    

