import sys
sys.path.append('.')
import sqlite3
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.AtendenteModel import Atendente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model import TabelaModel
from ProjetoConsultorio.Model.EnderecoModel import Endereco

class BancoDadosModel:
    
    def __init__(self, db_path):
        self.db_path = db_path

    # Create
    def cadastrarUsuario(self, usuario):
        query = '''
        INSERT INTO usuarios (login, senha, tipo, administrador)
        VALUES (?, ?, ?, ?)
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (usuario.login, usuario.senha, usuario.tipo, usuario.admin))
            connection.commit()
            return cursor.lastrowid
    
    def cadastrarEndereco(self, endereco):
        query = '''
        INSERT INTO enderecos (estado, cidade, bairro, rua, numero, cep)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (endereco.estado, endereco.cidade, endereco.bairro, endereco.rua, endereco.numero, endereco.cep))
            connection.commit()
            return cursor.lastrowid

    def cadastrarCliente(self, cliente, endereco):
        cliente.endereco_id = self.cadastrarEndereco(endereco)
        query = '''
        INSERT INTO clientes (cpf, nome, DataNasc, telefone, endereco_id)
        VALUES (?, ?, ?, ?, ?)
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (cliente.cpf, cliente.nome, cliente.DataNasc, cliente.telefone, cliente.endereco_id))
            connection.commit()
            return cursor.lastrowid

    def cadastrarConsulta(self, consulta):
        query = '''
        INSERT INTO consultas (descricao, data, horario, cliente_id, medico, valor)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (consulta.descricao, consulta.data, consulta.horario, consulta.cliente, consulta.medico, consulta.valor))
            connection.commit()
            return cursor.lastrowid

    def cadastrarAtendente(self, atendente, endereco):
        atendente.endereco_id = self.cadastrarEndereco(endereco)
        query = '''
        INSERT INTO atendentes (cpf, nome, DataNasc, telefone, endereco_id, salario)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (atendente.cpf, atendente.nome, atendente.DataNasc, atendente.telefone, atendente.endereco_id, atendente.salario))
            connection.commit()
            return cursor.lastrowid

    def cadastrarMedico(self, medico, endereco):
        medico.endereco_id = self.cadastrarEndereco(endereco)
        query = '''
        INSERT INTO medicos (cpf, nome, DataNasc, telefone, endereco_id, salario, crm)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (medico.cpf, medico.nome, medico.DataNasc, medico.telefone, medico.endereco_id, medico.salario, medico.crm))
            connection.commit()
            return cursor.lastrowid
        
    # Retrieve
        
    def buscarUsuario(self, usuario):
        query = '''
        SELECT * FROM usuarios WHERE login = ? AND senha = ? AND tipo = ? 
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (usuario.login, usuario.senha, usuario.tipo))
            user = cursor.fetchone()
            
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
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (endereco_id,))
            return cursor.fetchone()

    def buscarCliente(self, nome, cpf):
        try:
            query = '''
            SELECT * FROM clientes WHERE nome = ? AND cpf = ?
            '''
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (nome, cpf))
                cliente_data = cursor.fetchone()
                if cliente_data:
                    cliente_str = (
                        f"Cliente encontrado: CPF = {cliente_data[0]}, Nome = {cliente_data[1]}, "
                        f"Data de Nascimento = {cliente_data[2]}, Telefone = {cliente_data[3]}, "
                        f"Endereço = {cliente_data[4]}"
                    )
                    print()
                    print(cliente_str)
                    endereco_id = cliente_data[4]
                    if endereco_id:
                        cursor.execute('SELECT * FROM enderecos WHERE id = ?', (endereco_id,))
                        endereco = cursor.fetchone()
                        if endereco:
                            endereco_str = (
                                f"Endereço encontrado: Estado: {endereco[1]}, Cidade: {endereco[2]}, "
                                f"Bairro: {endereco[3]}, Rua: {endereco[4]} - Número {endereco[5]}, CEP: {endereco[6]}"
                            )
                            print(endereco_str)
                            print()
                        else:
                            print("Endereço não encontrado.")
                    else:
                        print("Cliente não tem um endereço vinculado.")
                    return Cliente(
                        nome=cliente_data[1],
                        cpf=cliente_data[0],
                        DataNasc=cliente_data[2],
                        telefone=cliente_data[3],
                        endereco_id=endereco_id
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
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (numero,))
            consult = cursor.fetchone()
            if consult:
                return Consulta(consult[2], consult[3], consult[4], consult[5], str(consult[1]), consult[6], consult[0])
            return None
    
    def buscarConsultaAlternativa(self, numero):
        query = """
        SELECT 
            c.id, c.descricao, c.data, c.horario, c.valor, c.medico,
            cl.nome, cl.cpf, cl.DataNasc, cl.telefone,
            e.rua, e.numero, e.bairro, e.cidade, e.estado, e.cep,
            m.cpf, m.nome, m.DataNasc, m.telefone, m.salario, m.crm
        FROM 
            consultas c
        INNER JOIN clientes cl ON c.cliente_id = cl.cpf
        INNER JOIN enderecos e ON cl.endereco_id = e.id
        INNER JOIN medicos m ON c.medico = m.crm
        WHERE c.id = ?
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (numero,))
            result = cursor.fetchone()
            if result:
                consulta_id, descricao, data, horario, valor, cMedico, nome, cpf, DataNasc, telefone, rua, numero, bairro, cidade, estado, cep, medico_cpf, medico_nome, medico_DataNasc, medico_telefone, medico_salario, medico_crm = result
                endereco = Endereco(estado, cidade, bairro, rua, numero, cep)
                cliente = Cliente(nome, str(cpf), DataNasc, telefone, None)
                medico = Medico(medico_nome, str(medico_cpf), medico_DataNasc, medico_telefone, None, medico_salario, medico_crm)
                consulta = Consulta(descricao, data, horario, valor, cpf, cMedico, consulta_id)
                return consulta, endereco, cliente, medico
            return None

    def buscarListaConsulta(self, cliente_id):
        query = '''
        SELECT * FROM consultas WHERE cliente_id = ?
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (cliente_id,))
            consultas = cursor.fetchall()
            if consultas:
                lista_consultas = []
                for consult in consultas:
                    consulta = Consulta(consult[2], consult[3], consult[4], consult[5], str(consult[1]), consult[6], consult[0])
                    lista_consultas.append(consulta)
                return lista_consultas
            return []

    def buscarAtendente(self, nome, cpf):
        try:
            query = '''
            SELECT * FROM atendentes WHERE nome = ? AND cpf = ?
            '''
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (nome, cpf))
                atendente_data = cursor.fetchone()
                if atendente_data:
                    atendente_str = (
                        f"Atendente encontrado: CPF = {atendente_data[0]}, Nome = {atendente_data[1]}, "
                        f"Data de Nascimento = {atendente_data[2]}, Telefone = {atendente_data[3]}, "
                        f"Endereço = {atendente_data[4]}, Salário = {atendente_data[5]}"
                    )
                    print()
                    print(atendente_str)
                    endereco_id = atendente_data[4]
                    if endereco_id:
                        cursor.execute('SELECT * FROM enderecos WHERE id = ?', (endereco_id,))
                        endereco = cursor.fetchone()

                        if endereco:
                            endereco_str = (
                                f"Endereço encontrado: Estado: {endereco[1]}, Cidade: {endereco[2]}, "
                                f"Bairro: {endereco[3]}, Rua: {endereco[4]} - Número {endereco[5]}, CEP: {endereco[6]}"
                            )
                            print(endereco_str)
                            print()
                        else:
                            print("Endereço não encontrado.")
                    else:
                        print("Atendente não tem um endereço vinculado.")
                    return Atendente(
                        nome=atendente_data[1],
                        cpf=atendente_data[0],
                        DataNasc=atendente_data[2],
                        telefone=atendente_data[3],
                        endereco_id=endereco_id,
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
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (nome, cpf))
                medico_data = cursor.fetchone()
                if medico_data:
                    medico_str = (
                        f"Médico encontrado: CPF = {medico_data[0]}, Nome = {medico_data[1]}, "
                        f"Data de Nascimento = {medico_data[2]}, Telefone = {medico_data[3]}, "
                        f"Endereço = {medico_data[4]}, Salário = {medico_data[5]}, CRM = {medico_data[6]}"
                    )
                    print()
                    print(medico_str)
                    endereco_id = medico_data[4]
                    endereco_query = 'SELECT * FROM enderecos WHERE id = ?'
                    cursor.execute(endereco_query, (endereco_id,))
                    endereco = cursor.fetchone()
                    if endereco:
                        endereco_str = (
                            f"Endereço encontrado: Estado: {endereco[1]}, Cidade: {endereco[2]}, "
                            f"Bairro: {endereco[3]}, Rua: {endereco[4]} - Número {endereco[5]}, CEP: {endereco[6]}"
                        )
                        print(endereco_str)
                        print()
                    else:
                        print("Endereço não encontrado.")
                    return Medico(
                        nome=medico_data[1],
                        cpf=medico_data[0],
                        DataNasc=medico_data[2],
                        telefone=medico_data[3],
                        endereco_id=endereco_id,
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
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (usuario.login, usuario.senha, usuario.tipo, usuario.admin, usuarioAntigo.id))
            connection.commit()

    def atualizarEndereco(self, ID, endereco):
        try:
            query = '''
            UPDATE enderecos
            SET estado = ?, cidade = ?, bairro = ?, rua = ?, numero = ?, cep = ?
            WHERE id = ?
            '''
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (endereco.estado, endereco.cidade, endereco.bairro, endereco.rua, endereco.numero, endereco.cep, ID))
                connection.commit()
            return True
        except sqlite3.OperationalError:
            print("Erro: Não foi possível alterar o endereço.")
            return False

    def modificarCliente(self, clienteAntigo, cliente):
        try:
            query = '''
            UPDATE clientes
            SET nome = ?, DataNasc = ?, telefone = ?
            WHERE cpf = ?
            '''
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (cliente.nome, cliente.DataNasc, cliente.telefone, clienteAntigo.cpf))
                connection.commit()
            return True
        except sqlite3.OperationalError:
            print("Erro: Não foi possível alterar o cliente.")
            return False

    def modificarConsulta(self, consultaAntiga, consulta):
        query = '''
        UPDATE consultas
        SET descricao = ?, data = ?, horario = ?, medico = ?, valor = ?
        WHERE id = ?
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (consulta.descricao, consulta.data, consulta.horario, consulta.medico, consulta.valor, consultaAntiga.numero))
            connection.commit()
        return True

    def modificarAtendente(self, atendenteAntigo, atendente):
        query = '''
        UPDATE atendentes
        SET nome = ?, DataNasc = ?, telefone = ?, salario = ?
        WHERE cpf = ?
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (atendente.nome, atendente.DataNasc, atendente.telefone, atendente.salario, atendenteAntigo.cpf))
            connection.commit()

    def modificarMedico(self, medicoAntigo, medico):
        query = '''
        UPDATE medicos
        SET nome = ?, DataNasc = ?, telefone = ?, salario = ?, crm = ?
        WHERE cpf = ?
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (medico.nome, medico.DataNasc, medico.telefone, medico.salario, medico.crm, medicoAntigo.cpf))
            connection.commit()
            
    # Delete
    
    def deletarUsuario(self, usuario):
        query = '''
        DELETE FROM usuarios WHERE login = ?
        '''
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (usuario.login,))
            connection.commit()

    def deletarCliente(self, cliente):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = '''
            DELETE FROM clientes WHERE cpf = ?
            '''
            cursor.execute(query, (cliente.cpf,))
            connection.commit()
            self._delete_orphan_endereco(connection, cursor, cliente.endereco_id)

    def deletarAtendente(self, atendente):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = '''
            DELETE FROM atendentes WHERE cpf = ?
            '''
            cursor.execute(query, (atendente.cpf,))
            connection.commit()
            self._delete_orphan_endereco(connection, cursor, atendente.endereco_id)

    def deletarMedico(self, medico):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = '''
            DELETE FROM medicos WHERE cpf = ?
            '''
            cursor.execute(query, (medico.cpf,))
            connection.commit()
            self._delete_orphan_endereco(connection, cursor, medico.endereco_id)

    def deletarConsulta(self, consulta):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = '''
            DELETE FROM consultas WHERE id = ?
            '''
            cursor.execute(query, (consulta.numero,))
            connection.commit()

    def deletarEndereco(self, endereco_id):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = '''
            SELECT COUNT(*) FROM (
                SELECT endereco_id FROM clientes WHERE endereco_id = ?
                UNION ALL
                SELECT endereco_id FROM medicos WHERE endereco_id = ?
                UNION ALL
                SELECT endereco_id FROM atendentes WHERE endereco_id = ?
            ) AS combined
            '''
            cursor.execute(query, (endereco_id, endereco_id, endereco_id))
            count = cursor.fetchone()[0]
            if count == 0:
                delete_query = '''
                DELETE FROM enderecos WHERE id = ?
                '''
                cursor.execute(delete_query, (endereco_id,))
                connection.commit()

    def _delete_orphan_endereco(self, connection, cursor, endereco_id):
        query = '''
        SELECT COUNT(*) FROM (
            SELECT endereco_id FROM clientes WHERE endereco_id = ?
            UNION ALL
            SELECT endereco_id FROM medicos WHERE endereco_id = ?
            UNION ALL
            SELECT endereco_id FROM atendentes WHERE endereco_id = ?
        ) AS combined
        '''
        cursor.execute(query, (endereco_id, endereco_id, endereco_id))
        count = cursor.fetchone()[0]
        if count == 0:
            delete_query = '''
            DELETE FROM enderecos WHERE id = ?
            '''
            cursor.execute(delete_query, (endereco_id,))
            connection.commit()
            
    # Adicionais
            
    def obterTodosClientes(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM clientes'
            cursor.execute(query)
            for row in cursor.fetchall():  
                cliente = Cliente(row[1], row[0], row[2], row[3], row[4])
                print(cliente)
            input("Pressione ENTER para continuar...")
            return 

    
    def obterTodosMedicos(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM medicos'
            cursor.execute(query)
            for row in cursor.fetchall():  
                medico = Medico(row[1], row[0], row[2], row[3], row[4], row[5], row[6])
                print(medico)
            input("Pressione ENTER para continuar...")
            return 

    
    def obterTodosAtendentes(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM atendentes'
            cursor.execute(query)
            for row in cursor.fetchall():  
                atendente = Atendente(row[1], row[0], row[2], row[3], row[4], row[5])
                print(atendente)
            input("Pressione ENTER para continuar...")
            return 

    
    def obterTodasConsultas(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM consultas'
            cursor.execute(query)
            for row in cursor.fetchall():  
                consulta = Consulta(row[2], row[3], row[4], row[5], str(row[1]), row[6], row[0])
                print()
                print(consulta)
            input("Pressione ENTER para continuar...")
            return

    
    def calcularValorTotalConsultas(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = 'SELECT SUM(valor) FROM consultas'
            cursor.execute(query)
            total = cursor.fetchone()[0] 
            if total:
                print("R$ ", total, "reais")
                input("Pressione ENTER para continuar...")
            else:
                print(0.0)
                input("Pressione ENTER para continuar...")
            return

        
if __name__ == "ProjetoConsultorio.Model.BancoDadosModel":  # A maior gambiarra da minha vida! kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
    tabela = TabelaModel.main()                             # não tive ideia melhor na hora kkkkkkkkkkkkk
    banco = BancoDadosModel('Consultorio.db')               
    user = Usuario("admin", "admin", 0, True)
    userBuscar = banco.buscarUsuario(user)
    if userBuscar is None:
        banco.cadastrarUsuario(user)