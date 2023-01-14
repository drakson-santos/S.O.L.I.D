# Esta classe fere a responsabilidade unica.
# Além de saber a estrutura da entidade resposta (Response), também sabe e é responsavel por
# converter a resposta para um formato especifico.

# Problema
class Response:

    def __init__(self, data, status):
        self.data = data
        self.status = status

    def get_response(self, response_type):

        if response_type == "json":
            return { "data": self.data }
        elif response_type == "yaml":
            return f"<xml>{self.data}</xsm>"
        elif response_type == "base64":
            # Logica para converter em base64
            return "13279173912"

# Agora separamos a classe responsavel por saber a estrutura da resposta e
# separamos a logica para converter dados em algum formato.
# Se observarmos, por conta da separação das responsabilidades, a classe que converte dados
# pode ser reutilizada.

# Solução
class Response:

    def __init__(self, value, status):
        self.value = value
        self.status = status

class Convert:

    def __init__(self, data):
        self.data = data

    def to(self, format):
        if format == "json":
            return { "data": self.data }
        elif format == "yaml":
            return f"<xml>{self.data}</xsm>"
        elif format == "base64":
            # Logica para converter em base64
            return "13279173912"

response = Response([], 200)
response_coverted = Convert(response).to("json")