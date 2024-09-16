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
        self.nome = self._nome
        self.cpf = self._cpf
        self.DataNasc = self._DataNasc
        self.telefone = self._telefone
        
        

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        if len(value) > 50:
            raise ValueError("Nome deve ter no máximo 50 caracteres.")
        self._nome = value

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, value: str) -> None:
        cleaned_cpf = re.sub(r'[.-]', '', value)
        if not re.match(r'^\d{11}$', cleaned_cpf):
            raise ValueError("CPF deve conter 11 dígitos.")
        self._cpf = cleaned_cpf

    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, value: str) -> None:
        cleaned_telefone = re.sub(r'[\s()-]', '', value)
        if not re.match(r'^\d{10,11}$', cleaned_telefone):
            raise ValueError("Telefone deve conter 10 ou 11 dígitos.")
        self._telefone = cleaned_telefone

    @property
    def DataNasc(self) -> str:
        return self._DataNasc

    @DataNasc.setter
    def DataNasc(self, value: str) -> None:
        try:
            data = datetime.strptime(value, "%d/%m/%Y")
            if data.date() > date.today():
                raise ValueError("A data de nascimento não pode ser no futuro.")
            self._DataNasc = data.strftime("%d/%m/%Y")
        except ValueError as e:
            raise ValueError(f"Formato de data inválido. Use dd/mm/yyyy. Erro: {str(e)}")

    @property       # será que eu coloco?
    def idade(self) -> int:
        DataNasc = datetime.strptime(self._DataNasc, "%d/%m/%Y")
        hoje = date.today()
        idade = hoje.year - DataNasc.year
        if hoje.month < DataNasc.month or (hoje.month == DataNasc.month and hoje.day < DataNasc.day):
            idade -= 1
        return idade

    @property
    def endereco_id(self) -> Optional[int]:
        return self._endereco_id

    @endereco_id.setter      # aqui só entra o ID
    def endereco_id(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do endereço deve ser um inteiro positivo.")
        self._endereco_id = value

    @abstractmethod
    def mostrar_informacoes(self) -> str:
        pass
    
