import re
import uuid

from pydantic import BaseModel, EmailStr, validator


class EnderecoId(BaseModel):
    id: uuid.UUID


class EnderecoPOST(BaseModel):
    cep: str
    logradouro: str
    bairro: str
    cidade: str
    estado: str

    @validator("cep")
    def cep_validation(cls, v):
        regex = "^\d{5}-\d{3}$"
        assert re.search(regex, v), "CEP deve estar no formato XXXXX-XXX"
        return v

    @validator("estado")
    def estado_validation(cls, v):
        estado_list = [
            "AL",
            "AC",
            "AP",
            "AM",
            "BA",
            "CE",
            "ES",
            "GO",
            "MA",
            "MT",
            "MS",
            "MG",
            "PA",
            "PB",
            "PR",
            "PE",
            "PI",
            "RJ",
            "RN",
            "RS",
            "RO",
            "RR",
            "SC",
            "SP",
            "SE",
            "TO",
            "DF",
        ]
        assert v in estado_list, (
            "Estado inválido. Valores: {" ".join(estado_list)}"
        )
        return v


class ClienteId(BaseModel):
    id: uuid.UUID


class ClientePUT(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    sexo: str
    telefone: str
    email: EmailStr

    @validator("sexo")
    def sexo_validation(cls, v):
        sexo_list = ["M", "F"]
        assert v in sexo_list, "Sexo inválido. Valores: {" ".join(sexo_list)}"
        return v

    @validator("cpf")
    def cpf_validation(cls, v):
        regex = "^\d{3}.\d{3}.\d{3}-\d{2}$"
        assert re.search(regex, v), "CPF deve estar no formato XXX.XXX.XXX-XX"
        return v

    @validator("telefone")
    def telefone_validation(cls, v):
        regex = "^\(\d{2}\) \d{5}-\d{4}$"
        assert re.search(regex, v), "CPF deve estar no formato (XX) XXXXX-XXXX"
        return v


class ClientePOST(EnderecoPOST, ClientePUT):
    pass
