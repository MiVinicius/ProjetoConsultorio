import sys
sys.path.append('.')    
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import re
from datetime import datetime, date

@dataclass
class Pessoa(ABC):
    _nome: str
    _cpf: str
    _DataNasc: str
    _telefone: str
    _endereco_id: Optional[int] = None

    def __post_init__(self):
        self._nome = self._validar_nome(self._nome)
        self._cpf = self._validar_cpf(self._cpf)
        self._DataNasc = self._validar_data_nasc(self._DataNasc)
        self._telefone = self._validar_telefone(self._telefone)
        if self._endereco_id is not None:
            self._endereco_id = self._validar_endereco_id(self._endereco_id)

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def DataNasc(self) -> str:
        return self._DataNasc

    @property
    def telefone(self) -> str:
        return self._telefone

    @property
    def endereco_id(self) -> Optional[int]:
        return self._endereco_id
    
    @endereco_id.setter   
    def endereco_id(self, new_endereco_id: Optional[int]):
        self._endereco_id = self._validar_endereco_id(new_endereco_id)

    def _validar_nome(self, nome: str) -> str:
        if len(nome) > 50:
            raise ValueError("Nome deve ter no máximo 50 caracteres.")
        return nome

    def _validar_cpf(self, cpf: str) -> str:
        cleaned_cpf = re.sub(r'[.-]', '', cpf)  # vair remover pontos e traços
        if not re.match(r'^\d{11}$', cleaned_cpf):
            raise ValueError("CPF deve conter 11 dígitos.")
        return cleaned_cpf

    def _validar_data_nasc(self, data_nasc: str) -> str:
        try:
            data = datetime.strptime(data_nasc, "%d/%m/%Y")
            if data.date() > date.today():
                raise ValueError("A data de nascimento não pode ser no futuro.")
            return data.strftime("%d/%m/%Y")
        except ValueError as e:
            raise ValueError(f"Formato de data inválido. Use dd/mm/yyyy. Erro: {str(e)}")

    def _validar_telefone(self, telefone: str) -> str:
        cleaned_telefone = re.sub(r'[\s()-]', '', telefone)  # vai remover espaços, parênteses e traços
        if not re.match(r'^\d{10,11}$', cleaned_telefone):
            raise ValueError("Telefone deve conter 10 ou 11 dígitos.")
        return cleaned_telefone

    def _validar_endereco_id(self, endereco_id: int) -> int:
        if not isinstance(endereco_id, int) or endereco_id <= 0:
            raise ValueError("ID do endereço deve ser um inteiro positivo.")
        return endereco_id

    @property
    def idade(self) -> int:
        DataNasc = datetime.strptime(self._DataNasc, "%d/%m/%Y")
        hoje = date.today()
        idade = hoje.year - DataNasc.year
        if hoje.month < DataNasc.month or (hoje.month == DataNasc.month and hoje.day < DataNasc.day):
            idade -= 1
        return idade

    @abstractmethod
    def mostrar_informacoes(self) -> str:
        pass

