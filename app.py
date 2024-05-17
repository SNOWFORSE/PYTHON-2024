import os

def exibir_nome_do_programa():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_opçoes():
    print("1. Cadastro Resteurante")
    print("2. Listar Resteurantes")
    print("3. Ativar Restaurante")
    print("4. Sair\n")
 
def finalizar_app():
    os.system("cls")
    print("finalizando o app\n")


def opaçao_invalida():
    print("Opção Invalida")
    input("Digite uma tecla para voltar ao menu principal")


def escolher_opçao():
    try:
        opção_escolhida =  int (input("Escolha uma Opção: "))
        # opção_escolhida = int(opção_escolhida) 

        if opção_escolhida == 1:
            print("Cadastrar Restaurante")
        elif opção_escolhida == 2:
            print("Listar Restaurantes")
        elif opção_escolhida == 3:
            print("Ativar Restaurante")
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opaçao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opçao()

if __name__ == "__main__":
    main()
