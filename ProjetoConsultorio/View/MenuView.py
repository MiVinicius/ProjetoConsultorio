class MenuView():
    
    def menuView(self):
        
        while True:
            print("""
                   Menu 1x    Menu 2x      Menu 3x    
                   Cliente   Consulta    Funcionários   
                  
                  11 - Cadastrar Cliente
                  12 - Buscar Cliente
                  13 - Modificar dados do cliente
                  14 - Remover cliente 
                  
                  21 - Agendamento de consulta
                  22 - Verificar histórico de consultas
                  23 - Modificar consulta
                  24 - Cancelar consulta
                  
                  31 - Cadastrar Médico
                  32 - Cadastrar Funcionários
                  33 - Buscar Médico
                  34 - Buscar Funcionário
                  35 - Modificar dados de Médico
                  36 - Modificar dados de Funcionário
                  37 - Remover Médico
                  38 - Remover Funcionário
                    
                  00 - Sair
                  """)
            opcao = int(input("Digite o número correspondente ao menu: "))
            match opcao:
                case 11:
                    pass
                case 12:
                    pass
                case 13:
                    pass
                case 14:
                    pass
                case 21:
                    pass
                case 22:
                    pass
                case 23:
                    pass
                case 24:
                    pass
                case 31:
                    pass
                case 32:
                    pass
                case 33:
                    pass
                case 34:
                    pass
                case 35:
                    pass
                case 36:
                    pass
                case 37:
                    pass
                case 38:
                    pass
                case 00:
                    break
                case _:
                    print("Opção invalida")
                    
if __name__ == "__main__":
    
    menuview = MenuView()
    menuview.menuView()