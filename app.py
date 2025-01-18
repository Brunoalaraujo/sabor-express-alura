import os

restaurantes = [{"nome": "Praça", "categoria":"Japonesa", "ativo":False}, {"nome":"Pizza Suprema", "categoria":"Italiano", "ativo":True}, {"nome":"Cantina", "categoria":"Italiano", "ativo":False} ]

def exibir_nome_do_programa():
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)

def exibir_opcoes():
    print("1. Cadastrar Restaurante.")
    print("2. Listar Restaurantes.")
    print("3. Alternar estado do Restaurante.")
    print("4. Sair.")

def escolher_opcoes():
    
    try:
        opcao_escolhida = int(input('Digite a sua opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurantes()
            case 2: 
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def cadastrar_restaurantes():
    """
    Realiza o cadastro dos Restaurantes no dicionário = dados_do_restaurante
    
    Inputs:
    - nome_do_restaurante: str - Nome do restaurante para ser cadastrado
    - categoria: str - Categoria do restaurante para ser cadastrado
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    """    
    exibir_subtitulo("Cadastrar novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Exibe os restaurantes cadastrados no dicionário
    
    Inputs:
    
    Output:
    
    """    
    exibir_subtitulo("Listando restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado" # Ternário
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}") # ljust(20) 20 espaçamentos
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Altera o status do restaurante entre true/false
    
    Inputs:
     - nome_restaurante: str - Nome do Restaurante
    
    Output:
    - Altera o status entre true/false
    """
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encotrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encotrado = True # Localizando restaurante no dicionário
            restaurante["ativo"] = not restaurante ["ativo"] # Invertentdo o valor da chave (ativo)
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso" # Ternário
            print(mensagem)
    if not restaurante_encotrado:
        print("O restaurante não foi encontrado")         
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    ''' 
    Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()

def opcao_invalida():
    ''' 
    Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' 
    Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print() # Para pular uma linha

def finalizar_app():
    exibir_subtitulo("Finalizar app")

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()