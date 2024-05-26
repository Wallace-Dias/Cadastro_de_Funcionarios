from time import sleep
import funções

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
                funções.cadastrar_funcionario(funcionários)
                
            # Lista de Funcionários
            if opc == 2:
                funções.listar_funcionario(funcionários)
                
            # Pesquisar Funcionários
            if opc == 3:
                funções.pesquiar_funcionario(funcionários)
                
            
            # Deletar 1 funcionário ou todos
            if opc == 4:
                funções.deletar_funcionario(funcionários)                

            # Sair do programa
            if opc == 5:
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