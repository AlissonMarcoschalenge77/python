# Plataforma TDB - Responde
# Sistema de Gestão de Atendimentos e Interações de Saúde Bucal
# Integrantes: Alisson Kawan Evangelista Silva (RM: 567598) e Marcos Vinicius de Jesus Almeida (RM: 567214)

# Listas para armazenamento em memória
pacientes = []
voluntarios = []
consultas = []
manifestacoes = []

# Loop principal do sistema
while True:
    # Exibição do menu principal
    print("\n" + "="*50)
    print("Bem-vindo ao menu da plataforma TDB - Responde")
    print("="*50)
    print("\nEscolha a melhor opção para seu atendimento:\n")
    print("1 - Cadastro de paciente")
    print("2 - Quero ser dentista voluntário")
    print("3 - Quero remarcar uma consulta")
    print("4 - Quero cancelar uma consulta")
    print("5 - Quero fazer uma reclamação")
    print("6 - Quero fazer um elogio")
    print("7 - Quero fazer uma sugestão")
    print("8 - Sair")
    print("="*50)
    
    # Tratamento de entrada do usuário
    try:
        opcao = int(input("\nDigite o número da opção desejada: "))
        print("\n")
        
        # Opção 1: Cadastro de Paciente
        if opcao == 1:
            print(f"Você escolheu a opção {opcao} - Cadastro de paciente")
            print("\n=== CADASTRO DE PACIENTE ===")
            nome = input("Nome completo: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            
            # Criação do dicionário do paciente
            paciente = {
                'nome': nome,
                'cpf': cpf,
                'telefone': telefone
            }
            
            # Adiciona o paciente à lista
            pacientes.append(paciente)
            print(f"\nPaciente {nome} cadastrado com sucesso!")
            input("\nPressione ENTER para voltar ao menu...")
        
        # Opção 2: Registro de Dentista Voluntário
        elif opcao == 2:
            print(f"Você escolheu a opção {opcao} - Quero ser dentista voluntário")
            print("\n=== REGISTRO DE DENTISTA VOLUNTÁRIO ===")
            nome = input("Nome completo: ")
            cro = input("Número do CRO: ")
            telefone = input("Telefone: ")
            especialidade = input("Especialidade: ")
            
            # Criação do dicionário do voluntário
            voluntario = {
                'nome': nome,
                'cro': cro,
                'telefone': telefone,
                'especialidade': especialidade
            }
            
            # Adiciona o voluntário à lista
            voluntarios.append(voluntario)
            print(f"\nDentista {nome} registrado como voluntário com sucesso!")
            input("\nPressione ENTER para voltar ao menu...")
        
        # Opção 3: Remarcar Consulta
        elif opcao == 3:
            print(f"Você escolheu a opção {opcao} - Quero remarcar uma consulta")
            print("\n=== REMARCAR CONSULTA ===")
            
            # Verifica se há consultas cadastradas
            if len(consultas) == 0:
                print("Não há consultas cadastradas no sistema.")
                input("\nPressione ENTER para voltar ao menu...")
            else:
                # Lista as consultas existentes
                print("\nConsultas cadastradas:")
                contador = 1
                for consulta in consultas:
                    print(f"{contador}. Paciente: {consulta['paciente']} - Data: {consulta['data']}")
                    contador = contador + 1
                
                # Solicita qual consulta remarcar
                try:
                    numero_consulta = int(input("\nNúmero da consulta a remarcar: "))
                    
                    if numero_consulta >= 1 and numero_consulta <= len(consultas):
                        nova_data = input("Nova data (DD/MM/AAAA): ")
                        consultas[numero_consulta - 1]['data'] = nova_data
                        print(f"\nConsulta remarcada para {nova_data} com sucesso!")
                    else:
                        print("Número de consulta inválido!")
                except ValueError:
                    print("Por favor, digite um número válido!")
                
                input("\nPressione ENTER para voltar ao menu...")
        
        # Opção 4: Cancelar Consulta
        elif opcao == 4:
            print(f"Você escolheu a opção {opcao} - Quero cancelar uma consulta")
            print("\n=== CANCELAR CONSULTA ===")
            
            # Verifica se há consultas cadastradas
            if len(consultas) == 0:
                print("Não há consultas cadastradas no sistema.")
                input("\nPressione ENTER para voltar ao menu...")
            else:
                # Lista as consultas existentes
                print("\nConsultas cadastradas:")
                contador = 1
                for consulta in consultas:
                    print(f"{contador}. Paciente: {consulta['paciente']} - Data: {consulta['data']}")
                    contador = contador + 1
                
                # Solicita qual consulta cancelar
                try:
                    numero_consulta = int(input("\nNúmero da consulta a cancelar: "))
                    
                    if numero_consulta >= 1 and numero_consulta <= len(consultas):
                        consulta_cancelada = consultas.pop(numero_consulta - 1)
                        print(f"\nConsulta de {consulta_cancelada['paciente']} cancelada com sucesso!")
                    else:
                        print("Número de consulta inválido!")
                except ValueError:
                    print("Por favor, digite um número válido!")
                
                input("\nPressione ENTER para voltar ao menu...")
        
        # Opção 5: Fazer uma Reclamação
        elif opcao == 5:
            print(f"Você escolheu a opção {opcao} - Quero fazer uma reclamação")
            print("\n=== REGISTRAR RECLAMAÇÃO ===")
            nome = input("Seu nome: ")
            mensagem = input("Digite sua reclamação: ")
            
            # Criação do dicionário da manifestação
            manifestacao = {
                'tipo': 'reclamação',
                'nome': nome,
                'mensagem': mensagem
            }
            
            # Adiciona a manifestação à lista
            manifestacoes.append(manifestacao)
            print("\nReclamação registrada com sucesso! Obrigado pelo feedback.")
            input("\nPressione ENTER para voltar ao menu...")
        
        # Opção 6: Fazer um Elogio
        elif opcao == 6:
            print(f"Você escolheu a opção {opcao} - Quero fazer um elogio")
            print("\n=== REGISTRAR ELOGIO ===")
            nome = input("Seu nome: ")
            mensagem = input("Digite seu elogio: ")
            
            # Criação do dicionário da manifestação
            manifestacao = {
                'tipo': 'elogio',
                'nome': nome,
                'mensagem': mensagem
            }
            
            # Adiciona a manifestação à lista
            manifestacoes.append(manifestacao)
            print("\nElogio registrado com sucesso! Obrigado pelo feedback.")
            input("\nPressione ENTER para voltar ao menu...")
        
        # Opção 7: Fazer uma Sugestão
        elif opcao == 7:
            print(f"Você escolheu a opção {opcao} - Quero fazer uma sugestão")
            print("\n=== REGISTRAR SUGESTÃO ===")
            nome = input("Seu nome: ")
            mensagem = input("Digite sua sugestão: ")
            
            # Criação do dicionário da manifestação
            manifestacao = {
                'tipo': 'sugestão',
                'nome': nome,
                'mensagem': mensagem
            }
            
            # Adiciona a manifestação à lista
            manifestacoes.append(manifestacao)
            print("\nSugestão registrada com sucesso! Obrigado pelo feedback.")
            input("\nPressione ENTER para voltar ao menu...")
        
        # Opção 8: Sair do Sistema
        elif opcao == 8:
            print("Saindo do sistema... Obrigado por usar a Plataforma TDB - Responde!")
            break
        
        # Opção inválida
        else:
            print("Digite um número válido entre 1 e 8!")
            input("\nPressione ENTER para continuar...")
    
    # Tratamento de erro para entrada não numérica
    except ValueError:
        print("Por favor, digite um número válido!")
        input("\nPressione ENTER para continuar...")