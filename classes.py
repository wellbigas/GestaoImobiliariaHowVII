class Pagamento:
    def __init__(self, id_pagamento, data_pagamento, valor_pagamento, codigo_imovel):
        self.id_pagamento = id_pagamento
        self.data_pagamento = data_pagamento
        self.valor_pagamento = valor_pagamento
        self.codigo_imovel = codigo_imovel

    def __str__(self):
        return f"ID: {self.id_pagamento}, Data: {self.data_pagamento}, Valor: {self.valor_pagamento}, Código do Imóvel: {self.codigo_imovel}"


