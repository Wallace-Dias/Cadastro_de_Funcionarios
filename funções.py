
def cadastrar_funcionario (funcionários):
    print("Cadastrando Funcionário".center(30))
    print("="*30)
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    salário = float(input("Salário: "))
    funcionário = (nome, idade, salário)
    funcionários.append(funcionário)
    print("="*30)
    print("")

def listar_funcionario(funcionários):
    if len(funcionários) == 0:
        
        print("Lista Vazia")
        print("="*30)
        print("")

    else:
        
        print("Lista de Funcionários".center(30))
        print("="*30)
        for index, funcionário in enumerate(funcionários, start=1):
            nome, idade, salário = funcionário
            print(f"{index}\nNome: {nome}\nIdade: {idade}\nSalário: R$ {salário:.2f}\n")
            print("="*30)
        
        print("="*30)
        print("")

def pesquiar_funcionario(funcionários):
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

def deletar_funcionario(funcionários):
    esq = int(input("[1] - Deletar funcionário em específico\n[2] - Excluir todos os funcionários\nOpcão: "))

    if esq == 1:

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

    # Deleta todos
    elif esq == 2:
        print("\nApagando todos os cadastros . . .")
        sleep(2)
        funcionários.clear()
        print("\nLista Vazia")
    else:
        print("\nValor Inválido!")
