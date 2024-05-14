from time import sleep

funcionários = []

print("="*30)
print("{:^30}".format("Cadastro de Funcionários"))
print("="*30)
#Menu
print("[1] - Cadastrar\n[2] - Lista de Funcionários\n[3] - Pesquisar\n[4] - Deletar Funcionários \n[5] - Sair do Programa")
print("")


while True:
    opc = input("Opção: ")
    print("")
    print("="*30)

    if opc.isdigit():
        opc = int(opc)
        
        if opc in (1, 2, 3, 4, 5):

            #Cadastrar Funcionários
            if opc == 1:
                # Cadastro
                print("Cadastrando Funcionário".center(30))
                print("="*30)
                nome = str(input("Nome: ")).strip().capitalize()
                idade = int(input("Idade: "))
                salário = float(input("Salário: "))
                funcionário = (nome, idade, salário)
                funcionários.append(funcionário)
                print("="*30)
                print("")

                
            if opc == 2:
                # Lista de Funcionários
                print("="*30)
                print("Lista de Funcionários".center(30))
                print("="*30)
                for index, funcionário in enumerate(funcionários, start=1):
                    nome, idade, salário = funcionário
                    print(f"{index}\nNome: {nome}\nIdade: {idade}\nSalário: R$ {salário:.2f}\n")
                    print("="*30)
                
                print("="*30)
                print("")
            
            if opc == 3:
                # Pesquisar
                # Em construção . . .
                print("Pesquisar Funcionário".center(30))
                print("="*30)
                
                if len(funcionários) == 0:
                    print("Nenhum funcionário cadastrado")
                
                else:
                    pesq = input("Nome: ")
                    encontrado = False

                    for funcionário in funcionários:
                        nome, idade, salário = funcionário
                        
                        

                        if pesq.lower() == nome.lower():
                            print("Encontrado!")
                            print("="*30)
                            print(f"\nNome: {nome}\nIdade: {idade}\nSalário: R$ {salário:.2f}\n")
                            print("="*30)
                            encontrado = True
                            break

                    if not encontrado:
                        print("Funcionário não encontrado ")
                        


                print("="*30)
                print("")
            
            if opc == 4:

                pesq = input("Nome do Funcionário a ser\nexcluído: ")
                encontrado = False
                for funcionário in funcionários:
                    nome, idade, salário = funcionário

                    if pesq.lower() == nome.lower():
                        print("="*30)
                        print(f'\nNome: {nome}\nIdade: {idade}\nSalário: R$ {salário: .2f}\n')
                        print("="*30)
                        encontrado = True

                        delete = input("Deletar? S/N: ")
                        print("")

                        if delete in 'sn':

                            if delete.lower() == 's':
                                funcionários.remove(funcionário)

                            if delete.lower() == 'n':
                                print("Exclusão cancelada")
                        else:
                            print("="*30)
                            print("Opção inválida!".center(30))
                            print("="*30)
                            print("")

                
                if not encontrado:
                    print("="*30)
                    print("Funcionário não encontrado!")
                    print("="*30)






            if opc == 5:
                # Sair do programa
                print("Saindo . . .")
                sleep(2)
                break

        else:
            print("Valor fora do intervalo, tente\nnovamente")
            print("="*30)

    else:
        print("Opção Inválida, Tende novamente!".center(30))
        print("="*30)

print("\n")
print("="*30)
print("Programa encerrado".center(30))
print("="*30)