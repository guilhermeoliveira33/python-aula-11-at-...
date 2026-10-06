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

        if opcao.isdigit():
            if opcao == 1:
                print("Cadastrando Aluno...")
                # nome = input("Digite o nome: ")
            elif opcao == 2:
                print("Consultando/Atualizando Aluno...")
            elif opcao == 3:
                print("Removendo Aluno...")
            elif opcao == 4:
                print("Listando os Alunos...")
            elif opcao == 5:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! Digite um número de 1 até 5.")
    else:
        print("Entrada inválida! Digite apenas números de 1 até 5.")