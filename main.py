from time import sleep

print("="*30)
print("{:^30}".format("Cadastro de Funcionários"))
print("="*30)
#Menu
print("[1] - Cadastrar\n[2] - Lista de Funcionários\n[3] - Pesquisar\n[4] - Sair")
print("")
lista = []
registro = 1

while True:
    opc = int(input("Opção: "))
    print("")
    print("="*30)

    #Cadastrar Funcionários
    if opc == 1:
        nome = str(input("Nome: ")).strip().capitalize()
        idade = int(input("Idade: "))
        salário = float(input("Salário: "))
        funcionario = (nome, idade, salário, registro)
        lista.append(funcionario)
        registro += 1
        print("="*30)
        print("")

        
    if opc == 2:
        #print(f"Nome: {nome}\nIdade: {idade}\nSalário: R$ {salário:.2f}")
        for index, funcionario in enumerate(lista, start=1):
            nome, idade, salário, registro = funcionario
            print(f"{index}. \nN°:{registro} \nNome:{nome} \nIdade: {idade} \nSalário: R${salário:.2f}")


        print("="*30)
        print("")
    
    if opc == 3:
        print("Em construção . . .")
        print("="*30)
        print("")

    if opc == 4:
        print("Saindo . . .")
        sleep(2)
        break

print("\n")
print("="*30)
print("Programa encerrado".center(30))
print("="*30)