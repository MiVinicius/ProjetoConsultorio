import sys
sys.path.append('.')
import sqlite3


def create_table_usuarios(cursor):

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS usuarios (

        login TEXT PRIMARY KEY NOT NULL UNIQUE,

        senha TEXT NOT NULL,

        tipo INTEGER NOT NULL,

        administrador BOOLEAN
        
    )

    ''')


def create_table_enderecos(cursor):

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS enderecos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        estado TEXT NOT NULL,

        cidade TEXT NOT NULL,

        bairro TEXT NOT NULL,

        rua TEXT NOT NULL,

        numero TEXT NOT NULL,

        cep TEXT NOT NULL
        

    )

    ''')


def create_table_clientes(cursor):

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS clientes (

        cpf TEXT PRIMARY KEY NOT NULL UNIQUE,

        nome TEXT NOT NULL,
        
        DataNasc TEXT NOT NULL,

        telefone TEXT,

        endereco_id INTEGER,

        FOREIGN KEY (endereco_id) REFERENCES enderecos (id)

    )

    ''') 


def create_table_consultas(cursor):

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS consultas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        cliente_id INTEGER,

        descricao TEXT NOT NULL,

        data TEXT NOT NULL,

        horario TEXT NOT NULL,
        
        valor FLOAT NOT NULL,

        medico TEXT NOT NULL,

        FOREIGN KEY (cliente_id) REFERENCES clientes (cpf),

        FOREIGN KEY (medico) REFERENCES medicos (crm)

    )

    ''')


def create_table_medicos(cursor):

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS medicos (

        cpf TEXT PRIMARY KEY NOT NULL UNIQUE,

        nome TEXT NOT NULL,
        
        DataNasc TEXT NOT NULL,
        
        telefone TEXT NOT NULL,

        endereco_id INTEGER,

        salario FLOAT NOT NULL,

        crm TEXT NOT NULL UNIQUE,

        FOREIGN KEY (endereco_id) REFERENCES enderecos (id)

    )

    ''')


def create_table_atendentes(cursor):

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS atendentes (

        cpf TEXT PRIMARY KEY NOT NULL UNIQUE,

        nome TEXT NOT NULL,
        
        DataNasc TEXT NOT NULL,
        
        telefone TEXT NOT NULL,

        endereco_id INTEGER,

        salario FLOAT NOT NULL,

        FOREIGN KEY (endereco_id) REFERENCES enderecos (id)

    )

    ''')
    



def main():


    connection = sqlite3.connect('Consultorio.db')

    cursor = connection.cursor()



    create_table_usuarios(cursor)

    create_table_enderecos(cursor)

    create_table_clientes(cursor)

    create_table_consultas(cursor)

    create_table_medicos(cursor)

    create_table_atendentes(cursor)



    connection.commit()

    connection.close()


if __name__ == "__main__":

    main()