class Pagamento:
    def __init__(self, id_pagamento, data_pagamento, valor_pagamento, codigo_imovel):
        self.id_pagamento = id_pagamento
        self.data_pagamento = data_pagamento
        self.valor_pagamento = valor_pagamento
        self.codigo_imovel = codigo_imovel

    def __str__(self):
        return f"ID: {self.id_pagamento}, Data: {self.data_pagamento}, Valor: {self.valor_pagamento}, Código do Imóvel: {self.codigo_imovel}"

class EstruturaAnalogica:
    def __init__(self, id_pagamento, data_pagamento, valor_pagamento, id_imovel, descricao_imovel, nome_tipo_imovel):
        self.id_pagamento = id_pagamento
        self.data_pagamento = data_pagamento
        self.valor_pagamento = valor_pagamento
        self.id_imovel = id_imovel
        self.descricao_imovel = descricao_imovel
        self.nome_tipo_imovel = nome_tipo_imovel

    def __str__(self):
        return f"ID do Pagamento: {self.id_pagamento}, Data de Pagamento: {self.data_pagamento}, " \
               f"Valor do Pagamento: {self.valor_pagamento}, ID do Imóvel: {self.id_imovel}, " \
               f"Descrição do Imóvel: {self.descricao_imovel}, Tipo de Imóvel: {self.nome_tipo_imovel}"


