from model.model_banco_de_dados import ModelBancoDeDados
from model.model_administrador import ModelAdministrador
from model.model_atendente import ModelAtendente
from model.model_medico import ModelMedico
from model.model_endereco import ModelEndereco
from view.view_cliente import ViewCliente
from view.view_consulta import ViewConsulta
from view.view_menu_administrador import ViewMenuAdministrador
from view.view_menu_medico import ViewMenuMedico
from view.view_menu_atendente import ViewMenuAtendente
from controller.controller_administrador import ControllerAdministrador
from controller.controller_cliente import ControllerCliente
from controller.controller_consulta import ControllerConsulta
from controller.controller_medico import ControllerMedico
from controller.controller_atendente import ControllerAtendente
from controller.controller_auth import ControllerAuth

def main():
    banco_de_dados = ModelBancoDeDados()
    banco_de_dados.carregar_dados()

    view_cliente = ViewCliente()
    view_consulta = ViewConsulta()
    view_menu_admin = ViewMenuAdministrador()
    view_menu_medico = ViewMenuMedico()
    view_menu_atendente = ViewMenuAtendente()

    controller_cliente = ControllerCliente(banco_de_dados, view_cliente)
    controller_consulta = ControllerConsulta(banco_de_dados, view_consulta)
    controller_medico = ControllerMedico(banco_de_dados, view_menu_medico)
    controller_atendente = ControllerAtendente(banco_de_dados, view_menu_atendente)
    controller_auth = ControllerAuth(banco_de_dados)

    controller_admin = ControllerAdministrador(banco_de_dados)

    usuario_logado = None
    while usuario_logado is None:
        usuario_logado = controller_auth.autenticar_usuario()

    while True:
        if isinstance(usuario_logado, ModelAdministrador):
            view_menu_admin.mostrar_menu()
        elif isinstance(usuario_logado, ModelMedico):
            view_menu_medico.mostrar_menu()
        elif isinstance(usuario_logado, ModelAtendente):
            view_menu_atendente.mostrar_menu()

        escolha = input("Escolha uma opção: ")

        if isinstance(usuario_logado, ModelAdministrador):
            if escolha == '10':
                # Lógica para criação de administrador
                nome = input("Nome: ")
                cpf = input("CPF: ")
                endereco = ModelEndereco(input("Cidade: "), input("Rua: "), input("Bairro: "), input("CEP: "), input("Número: "))
                telefone = input("Telefone: ")
                login = input("Login: ")
                senha = input("Senha: ")
                salario = float(input("Salário: "))
                controller_admin.criar_administrador(nome, cpf, endereco, telefone, login, senha, salario)
            elif escolha == '11':
                # Lógica para edição de administrador
                cpf_admin = input("CPF do administrador a ser editado: ")
                admin = next((a for a in banco_de_dados.administradores if a.cpf == cpf_admin), None)
                if admin:
                    novos_dados = {}
                    novos_dados['nome'] = input(f"Nome ({admin.nome}): ") or admin.nome
                    novos_dados['telefone'] = input(f"Telefone ({admin.telefone}): ") or admin.telefone
                    # Continue com outros campos
                    controller_admin.editar_administrador(admin, novos_dados)
                else:
                    print("Administrador não encontrado.")
            elif escolha == '12':
                # Lógica para remoção de administrador
                cpf_admin = input("CPF do administrador a ser removido: ")
                admin = next((a for a in banco_de_dados.administradores if a.cpf == cpf_admin), None)
                if admin:
                    controller_admin.remover_administrador(admin)
                else:
                    print("Administrador não encontrado.")
            # Continue com outras opções

        if escolha == '0':
            banco_de_dados.salvar_dados()
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
