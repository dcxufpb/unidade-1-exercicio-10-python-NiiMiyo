# coding: utf-8


def is_empty(value: str) -> bool:
    return (value == None) or (len(value) == value.count(" "))


class Loja:

    def __init__(self, nome_loja, logradouro, numero, complemento, bairro,
                 municipio, estado, cep, telefone, observacao, cnpj,
                 inscricao_estadual):
        self.nome_loja = nome_loja
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.observacao = observacao
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    def verifica_loja(self):
        if is_empty(self.nome_loja):
            raise Exception("O campo nome da loja é obrigatório")

        if is_empty(self.logradouro):
            raise Exception('O campo logradouro do endereço é obrigatório')

        if is_empty(self.municipio):
            raise Exception('O campo município do endereço é obrigatório')

        if is_empty(self.estado):
            raise Exception('O campo estado do endereço é obrigatório')

        if is_empty(self.cnpj):
            raise Exception('O campo CNPJ da loja é obrigatório')

        if is_empty(self.inscricao_estadual):
            raise Exception('O campo inscrição estadual da loja é obrigatório')

    def dados_loja(self):
        # Implemente aqui
        self.verifica_loja()

        numero = int()
        try:
            numero = int(self.numero)
        except Exception:
            numero = 0

        if numero <= 0:
            numero = "s/n"

        linha2 = f"{self.logradouro}, {numero}"
        if not is_empty(self.complemento):
            linha2 += f" {self.complemento}"

        linha3 = str()
        if not is_empty(self.bairro):
            linha3 += f"{self.bairro} - "
        linha3 += f"{self.municipio} - {self.estado}"

        linha4 = str()
        if not is_empty(self.cep):
            linha4 = f"CEP:{self.cep}"
        if not is_empty(self.telefone):
            if not is_empty(linha4):
                linha4 += " "
            linha4 += f"Tel {self.telefone}"
        if not is_empty(linha4):
            linha4 += "\n"

        linha5 = str()
        if not is_empty(self.observacao):
            linha5 = self.observacao

        output = f"{self.nome_loja}\n"
        output += f"{linha2}\n"
        output += f"{linha3}\n"
        output += f"{linha4}"
        output += f"{linha5}\n"
        output += f"CNPJ: {self.cnpj}\n"
        output += f"IE: {self.inscricao_estadual}"

        return output
