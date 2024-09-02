from model.banco_de_dados import BancoDeDados
from model.endereco import Endereco
from controller.controller_cliente import ControllerCliente
from controller.controller_consulta import ControllerConsulta
from controller.controller_medico import ControllerMedico
from controller.controller_atendente import ControllerAtendente
from controller.controller_relatorio import ControllerRelatorio
from view.view_cliente import ViewCliente
from view.view_consulta import ViewConsulta
from view.view_medico import ViewMedico
from view.view_atendente import ViewAtendente
from view.view_menu import ViewMenu
from controller.controller_auth import ControllerAuth

def main():
    banco_de_dados = BancoDeDados()
    banco_de_dados.carregar_dados()

    view_cliente = ViewCliente()
    view_consulta = ViewConsulta()
    view_medico = ViewMedico()
    view_atendente = ViewAtendente()
    view_menu = ViewMenu()

    controller_cliente = ControllerCliente(banco_de_dados, view_cliente)
    controller_consulta = ControllerConsulta(banco_de_dados, view_consulta)
    controller_medico = ControllerMedico(banco_de_dados, view_medico)
    controller_atendente = ControllerAtendente(banco_de_dados, view_atendente)
    controller_relatorio = ControllerRelatorio(banco_de_dados)
    controller_auth = ControllerAuth(banco_de_dados)

    while True:
        view_menu.mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do Cliente: ")
            cpf = input("CPF do Cliente: ")
            endereco = Endereco(
                cidade=input("Cidade: "),
                rua=input("Rua: "),
                bairro=input("Bairro: "),
                cep=input("CEP: "),
                numero=input("Número: ")
            )
            controller_cliente.adicionar_cliente(nome, cpf, endereco)

        elif escolha == '2':
            cpf = input("CPF do Cliente: ")
            controller_cliente.mostrar_cliente(cpf)

        elif escolha == '3':
            cpf = input("CPF do Cliente para remover: ")
            controller_cliente.remover_cliente(cpf)

        elif escolha == '4':
            descricao = input("Descrição da Consulta: ")
            data = input("Data (AAAA-MM-DD): ")
            horario = input("Horário (HH:MM): ")
            valor = float(input("Valor: "))
            cliente_cpf = input("CPF do Cliente: ")
            medico_crm = input("CRM do Médico: ")

            cliente = banco_de_dados.buscar_cliente(cliente_cpf)
            medico = banco_de_dados.buscar_medico(medico_crm)

            if cliente and medico:
                controller_consulta.adicionar_consulta(descricao, data, horario, valor, cliente, medico)
            else:
                print("Cliente ou Médico não encontrado!")

        elif escolha == '5':
            cliente_cpf = input("CPF do Cliente: ")
            controller_consulta.mostrar_consulta(cliente_cpf)

        elif escolha == '6':
            cliente_cpf = input("CPF do Cliente para remover a consulta: ")
            controller_consulta.remover_consulta(cliente_cpf)

        elif escolha == '7':
            nome = input("Nome do Médico: ")
            cpf = input("CPF do Médico: ")
            endereco = Endereco(
                cidade=input("Cidade: "),
                rua=input("Rua: "),
                bairro=input("Bairro: "),
                cep=input("CEP: "),
                numero=input("Número: ")
            )
            login = input("Login do Médico: ")
            senha = input("Senha do Médico: ")
            salario = float(input("Salário do Médico: "))
            especialidade = input("Especialidade do Médico: ")
            crm = input("CRM do Médico: ")

            controller_medico.adicionar_medico(nome, cpf, endereco, login, senha, salario, especialidade, crm)

        elif escolha == '8':
            crm = input("CRM do Médico: ")
            controller_medico.mostrar_medico(crm)

        elif escolha == '9':
            crm = input("CRM do Médico para remover: ")
            controller_medico.remover_medico(crm)

        elif escolha == '10':
            nome = input("Nome do Atendente: ")
            cpf = input("CPF do Atendente: ")
            endereco = Endereco(
                cidade=input("Cidade: "),
                rua=input("Rua: "),
                bairro=input("Bairro: "),
                cep=input("CEP: "),
                numero=input("Número: ")
            )
            login = input("Login do Atendente: ")
            senha = input("Senha do Atendente: ")
            salario = float(input("Salário do Atendente: "))

            controller_atendente.adicionar_atendente(nome, cpf, endereco, login, senha, salario)

        elif escolha == '11':
            login = input("Login do Atendente: ")
            controller_atendente.mostrar_atendente(login)

        elif escolha == '12':
            login = input("Login do Atendente para remover: ")
            controller_atendente.remover_atendente(login)

        elif escolha == '13':
            controller_relatorio.gerar_relatorio_consultas()

        elif escolha == '14':
            controller_relatorio.gerar_relatorio_clientes()

        elif escolha == '0':
            banco_de_dados.salvar_dados()
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
