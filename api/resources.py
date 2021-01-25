import grpc
from flask_restful import Resource, marshal_with, request
from google.protobuf import json_format
from pydantic import ValidationError

import cliente_pb2
import cliente_pb2_grpc
import endereco_pb2
import endereco_pb2_grpc
from schemas import ClienteId, ClientePOST, ClientePUT, EnderecoId, EnderecoPOST


def get_endereco_stub():
    channel = grpc.insecure_channel("grpc_endereco:50051")
    return endereco_pb2_grpc.EnderecoServiceStub(channel)


def get_cliente_stub():
    channel = grpc.insecure_channel("grpc_cliente:50051")
    return cliente_pb2_grpc.ClienteServiceStub(channel)


class EnderecoList(Resource):
    def get(self):
        stub = get_endereco_stub()
        result = {"enderecos": []}
        for endereco in stub.List(endereco_pb2.Endereco()):
            result["enderecos"].append(json_format.MessageToDict(endereco))
        return result

    """
    def post(self):
        try:
            endereco = endereco_pb2.Endereco(
                **EnderecoPOST(**request.json).dict()
            )
        except ValidationError as e:
            return {"erro": str(e)}, 422
        stub = get_endereco_stub()
        result = {"endereco": json_format.MessageToDict(stub.Create(endereco))}
        return result, 201
    """


class Endereco(Resource):
    def get(self, endereco_id):
        try:
            EnderecoId(id=endereco_id).dict()
            endereco_data = {"id": endereco_id}
            endereco = endereco_pb2.Endereco(**endereco_data)
        except ValidationError as e:
            return {"erro": str(e)}, 422
        stub = get_endereco_stub()
        result = {}
        result["endereco"] = json_format.MessageToDict(stub.Retrieve(endereco))
        if not result["endereco"]:
            return result, 404
        return result

    def put(self, endereco_id):
        try:
            EnderecoId(id=endereco_id).dict()
            endereco_data = {"id": endereco_id}
            endereco_data.update(EnderecoPOST(**request.json).dict())
            endereco = endereco_pb2.Endereco(**endereco_data)
        except ValidationError as e:
            return {"erro": str(e)}, 422

        stub = get_endereco_stub()
        result = {}
        result["endereco"] = json_format.MessageToDict(stub.Update(endereco))
        if not result["endereco"]:
            return result, 404
        return result

    """
    def delete(self, endereco_id):
        try:
            EnderecoId(id=endereco_id).dict()
            endereco_data = {"id": endereco_id}
            endereco = endereco_pb2.Endereco(**endereco_data)
        except ValidationError as e:
            return {"erro": str(e)}, 422

        stub = get_endereco_stub()
        result = json_format.MessageToDict(stub.Delete(endereco))
        if not result.get("status"):
            return result, 404
        return result, 204
    """


class ClienteList(Resource):
    def get(self):
        stub = get_cliente_stub()
        result = {"clientes": []}
        for cliente in stub.List(cliente_pb2.Cliente()):
            result["clientes"].append(json_format.MessageToDict(cliente))
        return result

    def post(self):
        try:
            cliente = cliente_pb2.Cliente(**ClientePOST(**request.json).dict())
        except ValidationError as e:
            return {"erro": str(e)}, 422
        stub = get_cliente_stub()
        result = {"cliente": json_format.MessageToDict(stub.Create(cliente))}
        return result, 201


class Cliente(Resource):
    def get(self, cliente_id):
        try:
            ClienteId(id=cliente_id).dict()
            cliente_data = {"id": cliente_id}
            cliente = cliente_pb2.Cliente(**cliente_data)
        except ValidationError as e:
            return {"erro": str(e)}, 422
        stub = get_cliente_stub()
        result = {}
        result["cliente"] = json_format.MessageToDict(stub.Retrieve(cliente))
        if not result["cliente"]:
            return result, 404
        return result

    def put(self, cliente_id):
        try:
            ClienteId(id=cliente_id).dict()
            cliente_data = {"id": cliente_id}
            cliente_data.update(ClientePUT(**request.json).dict())
            cliente = cliente_pb2.Cliente(**cliente_data)
        except ValidationError as e:
            return {"erro": str(e)}, 422

        stub = get_cliente_stub()
        result = {}
        result["cliente"] = json_format.MessageToDict(stub.Update(cliente))
        if not result["cliente"]:
            return result, 404
        return result

    def delete(self, cliente_id):
        try:
            ClienteId(id=cliente_id).dict()
            cliente_data = {"id": cliente_id}
            cliente = cliente_pb2.Cliente(**cliente_data)
        except ValidationError as e:
            return {"erro": str(e)}, 422

        stub = get_cliente_stub()
        result = json_format.MessageToDict(stub.Delete(cliente))
        if not result.get("status"):
            return result, 404
        return result, 204
