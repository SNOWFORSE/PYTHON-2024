import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")


print("1. Cadastro Resteurante")
print("2. Listar Resteurantes")
print("3. Ativar Restaurante")
print("4. Sair\n")

opção_escolhida =  int (input("Escolha uma Opção: "))
# opção_escolhida = int(opção_escolhida) 

def finalizar_app():
    os.system("cls")
    print("finalizando o app\n")





if opção_escolhida == 1:
    print("Cadastrar Restaurante")
elif opção_escolhida == 2:
    print("Listar Restaurantes")
elif opção_escolhida == 3:
    print("Ativar Restaurante")
else:
    finalizar_app()

def main():
    exibir_nome_do_programa()

if __name__ == "__main__":
    main()
