from time import sleep

print("="*30)
print("{:^30}".format("Cadastro de Funcionários"))
print("="*30)
#Menu
print("[1] - Cadastrar\n[2] - Lista de Funcionários\n[3] - Pesquisar\n[4] - Sair")
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
        print("="*30)
        print("")

        
    if opc == 2:
        # Lista de Funcionários
        print("="*30)
        print("Lista de Funcionários".center(30))
        print("="*30)
        print(f"Nome: {nome}\nIdade: {idade}\nSalário: R$ {salário:.2f}")
        


        print("="*30)
        print("")
    
    if opc == 3:
        # Pesquisar
        print("Em construção . . .")
        print("="*30)
        print("")

    if opc == 4:
        # Sair do programa
        print("Saindo . . .")
        sleep(2)
        break

print("\n")
print("="*30)
print("Programa encerrado".center(30))
print("="*30)