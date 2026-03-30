def print_lyrics():
    print("I thought I heard you laugh once, no?")
    print("I guess it must have been a ghost")

print_lyrics()

print(type(print_lyrics()))



#switch case no phyton
#match case

escolhaUser = 0
match escolhaUser:
    case 0:
        status = "Sair do programa"
    case 1:
        status = 'Entrar no programa'
    case _:
        status = "ERRO"

print (status)


#ex

idade = int(input("Digite sua idade: "))
if (idade>=16 and idade<18) or idade>70:
    print("Seu voto é opcional")
elif idade<16:
    print("Você não pode votar")
else:
    print("Seu voto não é opcional")