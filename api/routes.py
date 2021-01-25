from resources import Cliente, ClienteList, Endereco, EnderecoList


def register_resources(app):
    app.add_resource(EnderecoList, "/api/endereco/")
    app.add_resource(Endereco, "/api/endereco/<endereco_id>/")

    app.add_resource(ClienteList, "/api/cliente/")
    app.add_resource(Cliente, "/api/cliente/<cliente_id>/")
