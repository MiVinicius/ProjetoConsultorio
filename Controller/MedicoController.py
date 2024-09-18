import sys
sys.path.append('.')
from ProjetoConsultorio.Model.MedicoModel import Medico

class MedicoController():
    
    def __init__(self, banco_dados_controller, endereco_controller):
        self.banco_dados_controller = banco_dados_controller
        self.endereco_controller = endereco_controller
    
    def cadastrarMedico(self):
        try:
            nome = str(input("Digite o nome do Médico: \n")).strip()
            cpf = str(input("Digite o CPF: 11 digitos \n")).strip()
            cpf_limpo = Medico.validar_cpf(cpf)
            medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf_limpo)
            if medico_existe is None:
                print("Cadastrando o medico...")
                DataNasc = str(input("Digite a data de nascimento: dd/mm/aaaa \n"))
                telefone = str(input("Digite o telefone: (XX) XXXX-XXXX\n"))
                endereco = self.endereco_controller.cadastrarEndereco()
                salario = float(input("Digite o salário: \n"))
                crm = str(input("Digite o CRM: Sem espaços\n"))
                self.banco_dados_controller.cadastrarMedico(nome, cpf_limpo, DataNasc, telefone, salario, crm, endereco)
                print("cadastro do médico sucedido!")
                input("pressione ENTER para continuar")
                return True
            else:
                print("o medico já existe!")
                input("pressione ENTER para continuar")
                return False
        except Exception as e: 
            print(f"cadastro do Médico falhou por erro: {e}")
            input("pressione ENTER para continuar")
            return False
    
    def buscarMedico(self):
        nome = str(input("Digite o nome do medico: \n")).strip()
        cpf = str(input("Digite o CPF: \n")).strip()
        cpf_limpo = Medico.validar_cpf(cpf)
        medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf_limpo)
        if medico_existe is None:  
            print("o medico não existe!")
            input("pressione ENTER para continuar")
        else: 
            input("pressione ENTER para continuar")
            
    
    def buscarMedico2(self):
        nome = str(input("Digite o nome do medico: \n")).strip()
        cpf = str(input("Digite o CPF: \n")).strip()
        cpf_limpo = Medico.validar_cpf(cpf)
        medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf_limpo)
        if medico_existe is None:
            return None
        else:
            return medico_existe
        
    def modificarMedico(self):
        nomeModificar = str(input("Digite o nome do médico para modificar: \n")).strip()
        cpfModificar = str(input("Digite o CPF para modificar: \n")).strip()
        cpf_limpo = Medico.validar_cpf(cpfModificar)
        medico_existe = self.banco_dados_controller.buscarMedico(nomeModificar, cpf_limpo)
        if medico_existe is None:
            print("O Médico não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do médico: \n")).strip()
            DataNascNovo = str(input("Digite a nova data de nascimento: \n"))
            telefoneNovo = str(input("Digite o telefone: \n"))
            salarioNovo = float(input("Digite o salário: \n"))
            crmNovo = str(input("Digite o CRM: \n"))
            try:
                self.banco_dados_controller.modificarMedico(medico_existe, nomeNovo, medico_existe.cpf, DataNascNovo, telefoneNovo, salarioNovo, crmNovo)
                print(f"O Médico {medico_existe.nome} foi Atualizado")
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print("O Médico não foi Atualizado, erro", e)
                input("pressione ENTER para continuar")
                return False
            
    def atualizarEndereco(self):
        nomeModificar = input("Digite o nome do Medico para buscar: \n").strip()
        cpfModificar = input("Digite o CPF para buscar: \n").strip()
        cpf_limpo = Medico.validar_cpf(cpfModificar)
        medico_existente: Medico = self.banco_dados_controller.buscarMedico(nomeModificar, cpf_limpo)
        if medico_existente is None:
            print("O Médico não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            novoEndereco = self.endereco_controller.cadastrarEndereco()
            try:
                enderecoAntigo = medico_existente.endereco_id
                enderecoAtualizar = self.banco_dados_controller.atualizar_endereco(enderecoAntigo, novoEndereco)
                if enderecoAtualizar:
                    print("Endereço atualizado com sucesso!")
                    input("Pressione ENTER para continuar")
                    return True
                else:
                    print("Erro ao atualizar o endereço.")
                    input("Pressione ENTER para continuar")
            except Exception as e:
                print("Ocorreu um erro ao atualizar o endereço:", e)
                input("Pressione ENTER para continuar")

    def deletarMedico(self):
        try:
            medicoDeletar = self.buscarMedico2()
            self.banco_dados_controller.deletarMedico(medicoDeletar)
            print("o medico foi excluído")
            input("pressione ENTER para continuar")
            return True
        except Exception as e:
            print("o medico não foi excluído, erro", e)
            input("pressione ENTER para continuar")
            return False
        
    def gerar_atestado(self):
        numero = int(input("Digite o número da consulta para procurar: \n"))
        try:
            consulta, endereco, cliente, medico = self.banco_dados_controller.buscarConsultaAlternativa(numero)
            if consulta is not None:
                periodo = input("digite o período do atestado: ex: 3 meses ou 2 semanas ou 2 dias \n")
                atestado_str = f"""
                Atestado

                Atesto para os devidos fins, que o(a) Sr(a).
                {cliente.nome}
                Portador do CPF: {cliente.cpf}
                Data de Nascimento: {cliente.DataNasc}
                Telefone: {cliente.telefone}
                Endereço:
                Estado: {endereco.estado} Cidade: {endereco.cidade}
                Bairro: {endereco.bairro} Rua: {endereco.rua}
                Número: {endereco.numero} CEP: {endereco.cep}
                Esteve sob meus cuidados profissionais:
                Medico: {medico.nome} CRM: {medico.crm}
                No periodo de: {consulta.data}
                Horário: {consulta.horario}
                Necessitando de: {periodo} de convalescença.
                """
                print(atestado_str)
                input("pressione ENTER para continuar")
                return True
            else:
                print("Consulta inexistente")
                input("pressione ENTER para continuar")
            return False
        except Exception as e:
            print("Ocorreu um erro ao gerar o atestado:", e)
            input("pressione ENTER para continuar")
            return False
    
    def gerar_receita(self):
        numero = int(input("Digite o número da consulta para procurar: \n"))
        try:
            consulta, endereco, cliente, medico = self.banco_dados_controller.buscarConsultaAlternativa(numero)
            if consulta is not None:
                print("Gerando receita")
                medicamento = input("digite o nome do medicamento: \n")
                uso = input("digite o uso do medicamento: oral ou intravenosa \n")
                dosagem = input("digite a dosagem do medicamento: \n")
                frequencia = input("digite a frequência do medicamento: \n")
                duracao = input("digite a duração do uso do medicamento: \n")
                receita_str = f"""
                Receituário

                Identificação do Emitente
                Nome Completo: {medico.nome}
                CRM: {cliente.cpf}
                Data de Nascimento: {cliente.DataNasc}
                Telefone: {cliente.telefone}
                
                Paciente:
                Nome Completo: {cliente.nome}
                CPF: {cliente.cpf}
                Data de Nascimento: {cliente.DataNasc}
                Endereço:
                Estado: {endereco.estado} Cidade: {endereco.cidade}
                Bairro: {endereco.bairro} Rua: {endereco.rua}
                Número: {endereco.numero} CEP: {endereco.cep}
                
                Prescrição:
                Medicamentos: {medicamento} - uso: {uso} - dosagem: {dosagem} - frequência: {frequencia} - duração: {duracao}
                """
                print(receita_str)
                input("pressione ENTER para continuar")
                return True
            else:
                print("consulta inexistente")
                input("pressione ENTER para continuar")
                return None
        except Exception as e:
            print("Ocorreu um erro ao gerar a receita:", e)
            input("pressione ENTER para continuar")
            return False