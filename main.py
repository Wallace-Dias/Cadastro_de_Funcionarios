from time import sleep

funcionários = []

print("="*30)
print("{:^30}".format("Cadastro de Funcionários"))
print("="*30)
#Menu
print("[1] - Cadastrar\n[2] - Lista de Funcionários\n[3] - Pesquisar\n[4] - Deletar Funcionários \n[5] - Sair do Programa")
print("")


while True:
    opc = int(input("Opção: "))
    print("")
    print("="*30)

    #Cadastrar Funcionários
    if opc == 1:
        # Cadastro
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
        print("")
    
    if opc == 3:
        # Pesquisar
        print("Em construção . . .")
        print("="*30)
        print("")
    
    if opc == 4:
        print("Em construção. . .")

    if opc == 5:
        # Sair do programa
        print("Saindo . . .")
        sleep(2)
        break

print("\n")
print("="*30)
print("Programa encerrado".center(30))
print("="*30)