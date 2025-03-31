age = int(input("Quantos anos você tem: "))

if 18 <= age <= 60: 
    print("Pode doar sangue!")
else:
    if 16 <= age <= 17: 
        print("Possui autorização dos pais?, responde com S ou N")
        autorização  = input()
        if autorização == "s" or autorização == "S":
            print("Apresentar autorização quando for doar.")
        else: 
            print("Não pode doar sangue.")
    else: 
        print("Não pode doar.")


