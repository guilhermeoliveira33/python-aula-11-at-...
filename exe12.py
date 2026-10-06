while True:
    print("\n--- GERENCIAR ALUNO ---")
    print("1 - Cadastrar")
    print("2 - Atualizar (Consultar)")
    print("3 - Remover")
    print("4 - Listar")
    print("5 - Sair")

    # 1. Recebe a entrada como texto (string) para poder validar
    entrada = input("Digite uma opção: ")

    # 2. Verifica se o usuário digitou apenas números
    if entrada.isdigit():
        opcao = int(entrada)  # Converte para inteiro após a validação

        match opcao:
            case 1:
                print("Cadastrando Aluno...")
                # nome = input("Digite o nome: ")
            case 2:
                print("Consultando/Atualizando Aluno...")
            case 3:
                print("Removendo Aluno...")
            case 4:
                print("Listando os Alunos...")
            case 5:
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida! Digite um número de 1 até 5.")
    else:
        print("Entrada inválida! Digite apenas números de 1 até 5.")