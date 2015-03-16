from random import choice
steps=0
gamer_counter=0
eu_counter=0
print("se prepare para me enfrentar, seu perdedor!!!")
jogadas=["pedra","papel","tesoura","lagarto","spock"]

print("escolha entre pedra, lagarto, papel, tesoura ou spock")
while steps<5:
    if gamer_counter>eu_counter:
        print(gamer_counter," a ",eu_counter,"para mim")
    else:
        if gamer_counter<eu_counter:
            print(eu_counter,"a",gamer_counter,"para voce")
        else:
            if gamer_counter==eu_counter:
                print(gamer_counter,"a",eu_counter)
    gamer=choice(jogadas)
    
    eu=input("estou pronto, escolha uma jogada \n")
    
    while eu!=("pedra") and eu!=("papel") and eu!=("tesoura") and eu!=("lagarto") and eu!=("spock"):
        print("jogada nao encontrada, escolha novamente")
        print("escolha entre pedra, lagarto, papel, tesoura ou spock")
        eu=input("\n")
         
     
    if gamer==("pedra"):
       if eu==("tesoura") or eu==("lagarto"):
            gamer_counter+=1
            print(gamer,", ponto para mim ")
       else:
           if eu!=("pedra"):
                eu_counter+=1
                print(gamer,", ponto para voce")
           else:
                print(gamer,", empate")                    
    else:
        if gamer==("lagarto"):
            if eu==("papel") or eu==("spock"):
                gamer_counter+=1
                print(gamer,", ponto para mim")
            else:
                if eu!=("lagarto"):
                    eu_counter+=1
                    print(gamer,", ponto para voce")
                else:
                    print(gamer,", empate")
        else:
            if gamer==("papel"):
                if eu==("pedra") or eu==("spock"):
                    gamer_counter+=1
                    print(gamer,", ponto para mim")
                else:
                    if eu!=("papel"):
                        eu_counter+=1
                        print(gamer,", ponto para voce")
                    else:
                        print(gamer,", empate")
            else:
                if gamer==("tesoura"):
                    if eu==("papel") or eu==("lagarto"):
                        gamer_counter+=1
                        print(gamer,", ponto para mim")
                    else:
                        if eu!=("tesoura"):
                            eu_counter+=1
                            print(gamer,", ponto para voce")
                        else:
                            print(gamer,", empate")
                else:
                    if gamer==("spock"):
                        if eu==("pedra") or eu==("tesoura"):
                            gamer_counter+=1
                            print(gamer,", ponto para mim")
                        else:
                            if eu!=5:
                                eu_counter+=1
                                print(gamer,", ponto para voce")
                            else:
                                print(gamer,", empate")
    steps+=1                    
                    
if eu_counter>gamer_counter:
    print("voce ganhou de",eu_counter,"a",gamer_counter)
else:
    if gamer_counter>eu_counter:
        print("eu ganhei de",gamer_counter,"a",eu_counter,"seu lixo")
    else:
        if gamer_counter==eu_counter:
            print("nos empatamos por",gamer_counter,"a",eu_counter)