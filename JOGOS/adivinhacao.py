print("------------------------------------------------------------------")
print("                    BEM VINDO AO JOGO!                            ")
print("------------------------------------------------------------------")

print("Vamos brincar do jogo da adivinhacao?")
print("Escolhi um numero que esta de 0 a 10.")
print("Sera que voce consegue acerta?")

print("------------------------------------------------------------------")
print("                        Boa sorte!                                ")
print("------------------------------------------------------------------")

numero = 10

chute_1 = input("Qual numero que eu escolhi?")
chute = int(chute_1)

certo = chute == numero
maior = chute > numero
menor = chute < numero


if (certo):
    print("Você adivinhou!")
    print("------------------------------------------------------------------")
    print("                    Fim do jogo.                                  ")
    print("------------------------------------------------------------------")
else:
    if (maior):
        print("Você errou! O chute foi maior que o numero que eu escolhi."
              )
        print("Tente novamente"
              )
    elif (menor):
        print("Você errou! O chute foi menor que o numero que eu escolhi.")
        print("Tente novamente")