
import sys
sys.path.append('.')
import sqlite3
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.AtendenteModel import Atendente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
import Model.TabelaModel


class BancoDadosModel:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    # Create
    def cadastrarUsuario(self, usuario):
        query = '''
        INSERT INTO usuarios (login, senha, tipo, administrador)
        VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(query, (usuario.login, usuario.senha, usuario.tipo, usuario.admin))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def cadastrarEndereco(self, endereco):
        query = '''
        INSERT INTO enderecos (estado, cidade, bairro, rua, numero, cep)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (endereco.estado, endereco.cidade, endereco.bairro, endereco.rua, endereco.numero, endereco.cep))
        self.connection.commit()
        return self.cursor.lastrowid

    def cadastrarCliente(self, cliente, endereco):
        cliente.endereco_id = self.cadastrarEndereco(endereco)
        query = '''
        INSERT INTO clientes (cpf, nome, DataNasc, telefone, endereco_id)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (cliente.cpf, cliente.nome, cliente.DataNasc, cliente.telefone, cliente.endereco_id))
        self.connection.commit()
        return self.cursor.lastrowid

    def cadastrarConsulta(self, consulta):
        query = '''
        INSERT INTO consultas (descricao, data, horario, cliente_id, medico, valor)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (consulta.descricao, consulta.data, consulta.horario, consulta.cliente, consulta.medico, consulta.valor))
        self.connection.commit()
        return self.cursor.lastrowid

    def cadastrarAtendente(self, atendente, endereco):
        atendente.endereco_id = self.cadastrarEndereco(endereco)
        query = '''
        INSERT INTO atendentes (cpf, nome, DataNasc, telefone, endereco_id, salario)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (atendente.cpf, atendente.nome, atendente.DataNasc, atendente.telefone, atendente.endereco_id, atendente.salario))
        self.connection.commit()
        return self.cursor.lastrowid

    def cadastrarMedico(self, medico, endereco):
        medico.endereco_id = self.cadastrarEndereco(endereco)
        query = '''
        INSERT INTO medicos (cpf, nome, DataNasc, telefone, endereco_id, salario, crm)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (medico.cpf, medico.nome, medico.DataNasc, medico.telefone, medico.endereco_id, medico.salario, medico.crm))
        self.connection.commit()
        return self.cursor.lastrowid

    # Retrieve
    def buscarUsuario(self, usuario):
        query = '''
        SELECT * FROM usuarios WHERE login = ? AND senha = ? AND tipo = ? 
        '''
        self.cursor.execute(query, (usuario.login, usuario.senha, usuario.tipo))
        user = self.cursor.fetchone()
        
        if user:
            
            login, senha, tipo, admin = user 
            admin_bool = bool(admin)  
            return Usuario(login, senha, tipo, admin_bool)
        else:
            return None

    def buscarEndereco(self, endereco_id):
        query = '''
        SELECT * FROM enderecos WHERE id = ?
        '''
        self.cursor.execute(query, (endereco_id,))
        return self.cursor.fetchone()

    def buscarCliente(self, nome, cpf):
        try:
            query = '''
            SELECT * FROM clientes WHERE nome = ? AND cpf = ?
            '''
            self.cursor.execute(query, (nome, cpf))
            cliente_data = self.cursor.fetchone()
            if cliente_data:
                cliente_str = (
                    f"Cliente encontrado: CPF = {cliente_data[0]}, Nome = {cliente_data[1]}, "
                    f"Data de Nascimento = {cliente_data[2]}, Telefone = {cliente_data[3]}, "
                    f"Endereço = {cliente_data[4]}"
                )
                print(cliente_str)
                endereco_id = cliente_data[4]
                if endereco_id:
                    self.cursor.execute('SELECT * FROM Enderecos WHERE id = ?', (endereco_id,))
                    endereco = self.cursor.fetchone()
                    if endereco:
                        endereco_str = (
                            f"Endereço encontrado: Estado: {endereco[1]}, Cidade: {endereco[2]}, "
                            f"Bairro: {endereco[3]}, Rua: {endereco[4]} - Número {endereco[5]}, CEP: {endereco[6]}"
                        )
                        print(endereco_str)
                    else:
                        print("Endereço não encontrado.")
                else:
                    print("Cliente não tem um endereço vinculado.")
                return Cliente(
                    nome=cliente_data[1],
                    cpf=cliente_data[0],
                    DataNasc=cliente_data[2],
                    telefone=cliente_data[3],
                    endereco=endereco_id
                )
            else:
                print("Cliente não encontrado.")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o cliente: {e}")
            return None


    def buscarConsulta(self, numero):
        query = '''
        SELECT * FROM consultas WHERE id = ?
        '''
        self.cursor.execute(query, (numero,))
        consult = self.cursor.fetchone()
        if consult:
            return Consulta(consult[2], consult[3], consult[4], consult[5], consult[1], consult[6], consult[0])
        return None
    
    def buscarListaConsulta(self, cliente_id):
        query = '''
        SELECT * FROM consultas WHERE cliente_id = ?
        '''
        self.cursor.execute(query, (cliente_id,))
        consultas = self.cursor.fetchall()
        if consultas:
            lista_consultas = []
            for consult in consultas:
                consulta = Consulta(consult[2], consult[3], consult[4], consult[5], consult[1], consult[6], consult[0])
                lista_consultas.append(consulta)
            return lista_consultas
        return []

    def buscarAtendente(self, nome, cpf):
        try:
            query = '''
            SELECT * FROM atendentes WHERE nome = ? AND cpf = ?
            '''
            self.cursor.execute(query, (nome, cpf))
            atendente_data = self.cursor.fetchone()
            if atendente_data:
                atendente_str = (
                    f"Atendente encontrado: CPF = {atendente_data[0]}, Nome = {atendente_data[1]}, "
                    f"Data de Nascimento = {atendente_data[2]}, Telefone = {atendente_data[3]}, "
                    f"Endereço = {atendente_data[4]}, Salário = {atendente_data[5]}"
                )
                print(atendente_str)
                endereco_id = atendente_data[4]
                if endereco_id:
                    self.cursor.execute('SELECT * FROM Enderecos WHERE id = ?', (endereco_id,))
                    endereco = self.cursor.fetchone()

                    if endereco:
                        endereco_str = (
                            f"Endereço encontrado: Estado: {endereco[1]}, Cidade: {endereco[2]}, "
                            f"Bairro: {endereco[3]}, Rua: {endereco[4]} - Número {endereco[5]}, CEP: {endereco[6]}"
                        )
                        print(endereco_str)
                    else:
                        print("Endereço não encontrado.")
                else:
                    print("Atendente não tem um endereço vinculado.")
                return Atendente(
                    nome=atendente_data[1],
                    cpf=atendente_data[0],
                    DataNasc=atendente_data[2],
                    telefone=atendente_data[3],
                    endereco=endereco_id,
                    salario=atendente_data[5]
                )
            else:
                print("Atendente não encontrado.")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o atendente: {e}")
            return None


    def buscarMedico(self, nome, cpf):
        try:
            query = '''
            SELECT * FROM medicos WHERE nome = ? AND cpf = ?
            '''
            self.cursor.execute(query, (nome, cpf))
            medico_data = self.cursor.fetchone()
            if medico_data:
                medico_str = (
                    f"Médico encontrado: CPF = {medico_data[0]}, Nome = {medico_data[1]}, "
                    f"Data de Nascimento = {medico_data[2]}, Telefone = {medico_data[3]}, "
                    f"Endereço = {medico_data[4]}, Salário = {medico_data[5]}, CRM = {medico_data[6]}"
                )
                print(medico_str)
                endereco_id = medico_data[4]
                endereco_query = 'SELECT * FROM Enderecos WHERE id = ?'
                self.cursor.execute(endereco_query, (endereco_id,))
                endereco = self.cursor.fetchone()
                if endereco:
                    endereco_str = (
                        f"Endereço encontrado: Estado: {endereco[1]}, Cidade: {endereco[2]}, "
                        f"Bairro: {endereco[3]}, Rua: {endereco[4]} - Número {endereco[5]}, CEP: {endereco[6]}"
                    )
                    print(endereco_str)
                else:
                    print("Endereço não encontrado.")
                return Medico(
                    nome=medico_data[1],
                    cpf=medico_data[0],
                    DataNasc=medico_data[2],
                    telefone=medico_data[3],
                    endereco=endereco_id,
                    salario=medico_data[5],
                    crm=medico_data[6]
                )
            else:
                print("Médico não encontrado.")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o médico: {e}")
            return None


    # Update
    def modificarUsuario(self, usuarioAntigo, usuario):
        query = '''
        UPDATE usuarios
        SET login = ?, senha = ?, tipo = ?, administrador = ?
        WHERE id = ?
        '''
        self.cursor.execute(query, (usuario.login, usuario.senha, usuario.tipo, usuario.admin, usuarioAntigo.id))
        self.connection.commit()

    def atualizarEndereco(self, ID, endereco):
        try:
            query = '''
            UPDATE enderecos
            SET estado = ?, cidade = ?, bairro = ?, rua = ?, numero = ?, cep = ?
            WHERE id = ?
            '''
            self.cursor.execute(query, (endereco.estado, endereco.cidade, endereco.bairro, endereco.rua, endereco.numero, endereco.cep, ID.endereco_id))
            self.connection.commit()
            return True
        except sqlite3.OperationalError:
            print("Erro: Não foi possível alterar o endereço.")
            return False

    def modificarCliente(self, clienteAntigo, cliente):
        try:
            query = '''
            UPDATE clientes
            SET nome = ?, DataNasc = ?, telefone = ?
            WHERE cpf = ?
            '''
            self.cursor.execute(query, (cliente.nome, cliente.DataNasc, cliente.telefone, clienteAntigo.cpf))
            self.connection.commit()
            return True
        except sqlite3.OperationalError:
            print("Erro: Não foi possível alterar o cliente.")
            return False
        

    def modificarConsulta(self, consultaAntiga, consulta):
        query = '''
        UPDATE consultas
        SET descricao = ?, data = ?, horario = ?, medico = ?, valor = ?
        WHERE id = ?
        '''
        self.cursor.execute(query, (consulta.descricao, consulta.data, consulta.horario, consulta.medico, consulta.valor, consultaAntiga.numero))
        self.connection.commit()
        return True

    def modificarAtendente(self, atendenteAntigo, atendente):
        query = '''
        UPDATE atendentes
        SET nome = ?, DataNasc = ?, telefone = ?, salario = ?
        WHERE cpf = ?
        '''
        self.cursor.execute(query, (atendente.nome, atendente.DataNasc, atendente.telefone, atendente.salario, atendenteAntigo.cpf))
        self.connection.commit()

    def modificarMedico(self, medicoAntigo, medico):
        query = '''
        UPDATE medicos
        SET nome = ?, DataNasc = ?, telefone = ?, salario = ?, crm = ?
        WHERE cpf = ?
        '''
        self.cursor.execute(query, (medico.nome, medico.DataNasc, medico.telefone, medico.salario, medico.crm, medicoAntigo.cpf))
        self.connection.commit()

    # Delete
    def deletarUsuario(self, usuario):
        query = '''
        DELETE FROM usuarios WHERE login = ?
        '''
        self.cursor.execute(query, (usuario.login,))
        self.connection.commit()

    def deletarCliente(self, cliente):
        query = '''
        DELETE FROM clientes WHERE cpf = ?
        '''
        self.cursor.execute(query, (cliente.cpf,))
        self.connection.commit()
        self._delete_orphan_endereco(cliente.endereco_id)

    def deletarAtendente(self, atendente):
        query = '''
        DELETE FROM atendentes WHERE cpf = ?
        '''
        self.cursor.execute(query, (atendente.cpf,))
        self.connection.commit()
        self._delete_orphan_endereco(atendente.endereco_id)

    def deletarMedico(self, medico):
        query = '''
        DELETE FROM medicos WHERE cpf = ?
        '''
        self.cursor.execute(query, (medico.cpf,))
        self.connection.commit()
        self._delete_orphan_endereco(medico.endereco_id)

    def deletarConsulta(self, consulta):
        query = '''
        DELETE FROM consultas WHERE id = ?
        '''
        self.cursor.execute(query, (consulta.numero,))
        self.connection.commit()

    def deletarEndereco(self, endereco_id):
        query = '''
        SELECT COUNT(*) FROM (
            SELECT endereco_id FROM clientes WHERE endereco_id = ?
            UNION ALL
            SELECT endereco_id FROM medicos WHERE endereco_id = ?
            UNION ALL
            SELECT endereco_id FROM atendentes WHERE endereco_id = ?
        ) AS combined
        '''
        self.cursor.execute(query, (endereco_id, endereco_id, endereco_id))
        count = self.cursor.fetchone()[0]
        if count == 0:
            delete_query = '''
            DELETE FROM enderecos WHERE id = ?
            '''
            self.cursor.execute(delete_query, (endereco_id,))
            self.connection.commit()

    def _delete_orphan_endereco(self, endereco_id):
        query = '''
        SELECT COUNT(*) FROM (
            SELECT endereco_id FROM clientes WHERE endereco_id = ?
            UNION ALL
            SELECT endereco_id FROM medicos WHERE endereco_id = ?
            UNION ALL
            SELECT endereco_id FROM atendentes WHERE endereco_id = ?
        ) AS combined
        '''
        self.cursor.execute(query, (endereco_id, endereco_id, endereco_id))
        count = self.cursor.fetchone()[0]
        if count == 0:
            delete_query = '''
            DELETE FROM enderecos WHERE id = ?
            '''
            self.cursor.execute(delete_query, (endereco_id,))
            self.connection.commit()


    # Adicionais
    
    def obterTodosClientes(self):
        query = 'SELECT * FROM clientes'
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            cliente = Cliente(row[1], row[0], row[2], row[3], row[4])
            print(cliente)
        input("Pressione ENTER para continuar...")
        return 

    def obterTodosMedicos(self):
        query = 'SELECT * FROM medicos'
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            medico = Medico(row[1], row[0], row[2], row[3], row[4], row[5], row[6])
            print(medico)
        input("Pressione ENTER para continuar...")
        return 
        

    def obterTodosAtendentes(self):
        query = 'SELECT * FROM atendentes'
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            atendente = Atendente(row[1], row[0], row[2], row[3], row[4], row[5])
            print(atendente)
        input("Pressione ENTER para continuar...")
        return 

    def obterTodasConsultas(self):
        query = 'SELECT * FROM consultas'
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            consulta = Consulta(row[2], row[3], row[4], row[5], row[1], row[6], row[0])
            print(consulta)
        input("Pressione ENTER para continuar...")
        return

    def calcularValorTotalConsultas(self):
        query = 'SELECT SUM(valor) FROM consultas'
        self.cursor.execute(query)
        total = self.cursor.fetchone()[0]
        if total:
            print("R$ ",total, "reais")
            input("Pressione ENTER para continuar...")
        else :
            print(0.0)
            input("Pressione ENTER para continuar...")
        return   

    def close(self):
        self.connection.close()
        
if __name__ == "ProjetoConsultorio.Model.BancoDadosModel":  # A maior gambiarra da minha vida! kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
    tabela = Model.TabelaModel.main()                       # não tive ideia melhor na hora kkkkkkkkkkkkk
    banco = BancoDadosModel('Consultorio.db')
    user = Usuario("administrador", "administrador", 0, True)
    banco.cadastrarUsuario(user)
    
# if __name__:
#     print(__name__)

# if __name__ == "__main__":
#     banco = BancoDadosModel('Consultorio.db')

    # Testes!
    
    # enderecoOrfao = banco._delete_orphan_endereco(1)
    
    # enderec = Endereco("São paulo", "Santos", "Tijuca", "Jacarepaguá", "90", "12.345-678")
    # client = Cliente("Misael", "1234567800", "8888-8888", enderec)
    # cliente1 = banco.cadastrarCliente(client)
    
    # buscar1 = banco.buscarCliente(Cliente("Misael", "1234567800", None, None))
    # print(buscar1)
    # buscarEnder = banco.buscarEndereco("1")
    # print(buscarEnder)
    # ender = Endereco("Pernambuco", "Recife", "Porto digital", "Inhegas", "108", "00.415-218")
    # mudarEnder = banco.atualizarEndereco(Cliente(buscar1[1], buscar1[0], buscar1[2], buscar1[3]), ender)
    
    # cliente2 = Cliente("Marta", "12345678900", "9999-9999", enderec)
    # modificar = banco.modificarCliente(Cliente(buscar1[1], buscar1[0], buscar1[2], buscar1[3]), cliente2)
    
    # buscar2 = banco.buscarCliente(Cliente("Marta", "12345678900", None, None))
    # print(buscar2)
    # deletar = banco.deletarCliente(Cliente(buscar2[1], buscar2[0], buscar2[2], buscar2[3]))
    
    
    
    # enderec = Endereco("São paulo", "Santos", "Tijuca", "Jacarepaguá", "90", "12.345-678")
    # client = Atendente("Misael", "12345678900", "8888-8888", enderec, "1500")
    # cliente1 = banco.cadastrarAtendente(client)
    
    # buscar1 = banco.buscarAtendente(Atendente("Misael", "12345678900", None, None, None))
    # print(buscar1)
    # buscarEnder = banco.buscarEndereco("2")
    # print(buscarEnder)
    # ender = Endereco("Pernambuco", "Recife", "Porto digital", "Inhegas", "108", "00.415-218")
    # mudarEnder = banco.atualizarEndereco(Atendente(buscar1[1], buscar1[0], buscar1[3], buscar1[2], buscar1[4]), ender)
    
    
    # cliente2 = Atendente("Marta", "12345678900", "9999-9999", enderec, "2000")
    # modificar = banco.modificarAtendente(Atendente(buscar1[1], buscar1[0], buscar1[3], buscar1[2], buscar1[4]), cliente2)
    
    # buscar2 = banco.buscarAtendente(Atendente("Marta", "12345678900", None, None, None))
    # print(buscar2)
    # deletar = banco.deletarAtendente(Atendente(buscar2[1], buscar2[0], buscar2[2], buscar2[3], buscar2[4]))
    
    
    
    # enderec = Endereco("São paulo", "Santos", "Tijuca", "Jacarepaguá", "90", "12.345-678")
    # client = Medico("Misael", "123456789000", "8888-8888", enderec, "1500", "Pediatra")
    # cliente1 = banco.cadastrarMedico(client)
    
    # buscar1 = banco.buscarMedico(Medico("Misael", "123456789000", None, None, None, None))
    # print(buscar1)
    # buscarEnder = banco.buscarEndereco("3")
    # print(buscarEnder)
    # ender = Endereco("Pernambuco", "Recife", "Porto digital", "Inhegas", "108", "00.415-218")
    # mudarEnder = banco.atualizarEndereco(Atendente(buscar1[1], buscar1[0], buscar1[3], buscar1[2], buscar1[4]), ender)
    
    # cliente2 = Medico("Marta", "12345678900", "9999-9999", enderec, "2000", "Cardiologista")
    # modificar = banco.modificarMedico(Medico(buscar1[1], buscar1[0], buscar1[3], buscar1[2], buscar1[4], buscar1[5]), cliente2)
    
    # buscar2 = banco.buscarMedico(Medico("Marta", "12345678900", None, None, None, None))
    # print(buscar2)
    # deletar = banco.deletarMedico(Medico(buscar2[1], buscar2[0], buscar2[3], buscar2[2], buscar2[4], buscar2[5]))
    
    
    
    # user = Usuario("administrador", "administrador", 0, True)
    # banco.cadastrarUsuario(user)
    
    # usuario = banco.buscarUsuario(Usuario("admin", "admin", 0))
    # print(usuario)
    
    # user2 = Usuario("user", "user", 1, False)
    # modificar = banco.modificarUsuario(Usuario(usuario[1], usuario[2], usuario[3], usuario[4], usuario[0]), user2)
    
    # buscar = banco.buscarUsuario(Usuario("user", "user", 1))
    # print(buscar)
    # deletar = banco.deletarUsuario(Usuario(buscar[1], buscar[2], buscar[3]))
    # deletar = banco.deletarUsuario(Usuario("admin", "admin", 0))
    
    
    # medico = banco.buscarMedico(Medico("Misael", "123456789000", None, None, None, None))
    # cliente = banco.buscarCliente(Cliente("Misael", "1234567800", None, None))
    # consulta = Consulta("Consulta de teste", "01/01/2022", "10:00", 100.00, cliente[0], medico[5])
    # # consultaCadast = banco.cadastrarConsulta(consulta)
    # consultaBusc = banco.buscarConsulta(1)
    # print(consultaBusc)
    # consultaAntiga = Consulta(consultaBusc[2], consultaBusc[3], consultaBusc[4], consultaBusc[5], consultaBusc[1], consultaBusc[6], consultaBusc[0])
    # consultaNova = Consulta("Consulta de modificação", "07/09/2024", "17:00", 150.00, cliente[0], medico[5])
    # consultaModif = banco.modificarConsulta(consultaAntiga, consultaNova)
    # delet = banco.deletarConsulta(2)
    
    
    
    # endereco = Endereco("São paulo", "Santos", "Tijuca", "Jacarepagua", "90", "12.345-678")
    # cliente = Cliente("Misael", "12345678900", "8888-8888", endereco)
    # # banco.cadastrarCliente(cliente)
    # cliente0 = banco.buscarCliente(cliente)
    # print(cliente0)
    # print(banco.buscarEndereco(str(cliente0[3])))
    # endereco2 = Endereco("Paraiba", "João pessoa", "Campina Grande", "Campis", "60", "10.765-008")
    # cliente2 = Cliente("Marta", "12345678900", "9999-9999", endereco2)
    # banco.modificarCliente(Cliente(cliente0[1], cliente0[0], cliente0[2], cliente0[3]), cliente2)
    # endereco0 = banco.buscarEndereco(str(2))
    # print(endereco0)
    # banco.atualizarEndereco(Endereco("São paulo", "Santos", "Tijuca", "Jacarepagua", "90", "12.345-678", "2"), endereco2)
    # cliente10 = Cliente(cliente0[1], cliente0[0], cliente0[2], cliente0[3])
    # print(cliente10)
    # deletar = banco.deletarCliente(cliente10)
    # buscar = banco.buscarCliente(Cliente("Marta", "12345678900", None, None))
    # deletar = banco.deletarCliente(Cliente(buscar[1], buscar[0], buscar[2], buscar[3]))

