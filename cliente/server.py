import uuid
from concurrent import futures

import grpc
from google.protobuf import json_format
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict

import cliente_pb2
import cliente_pb2_grpc
import endereco_pb2
import endereco_pb2_grpc
from db import Cliente
from schemas import ClienteUpdateSchema, EnderecoCreateSchema


def get_endereco_stub():
    channel = grpc.insecure_channel("grpc_endereco:50051")
    return endereco_pb2_grpc.EnderecoServiceStub(channel)


class ClienteServiceServicer(cliente_pb2_grpc.ClienteServiceServicer):
    def Create(self, request, context):
        endereco_dict = {}
        for key in EnderecoCreateSchema:
            endereco_dict[key] = getattr(request, key)
        endereco = endereco_pb2.Endereco(**endereco_dict)

        stub = get_endereco_stub()
        endereco_id = stub.Create(endereco).id

        cliente_dict = {"endereco_id": endereco_id}
        for key in ClienteUpdateSchema:
            cliente_dict[key] = getattr(request, key)

        obj = Cliente.create(id=uuid.uuid4(), **cliente_dict)
        obj.id = str(obj.id)
        obj.endereco_id = str(obj.endereco_id)
        return cliente_pb2.Cliente(**model_to_dict(obj))

    def List(self, request, context):
        for obj in Cliente.select():
            obj.id = str(obj.id)
            obj.endereco_id = str(obj.endereco_id)
            yield cliente_pb2.Cliente(**model_to_dict(obj))

    def Retrieve(self, request, context):
        try:
            obj = Cliente.get(Cliente.id == request.id)
        except DoesNotExist:
            return cliente_pb2.Cliente()
        obj.id = str(obj.id)
        obj.endereco_id = str(obj.endereco_id)
        return cliente_pb2.Cliente(**model_to_dict(obj))

    def Update(self, request, context):
        try:
            obj = Cliente.get(Cliente.id == request.id)
        except DoesNotExist:
            return cliente_pb2.Cliente()
        for key in ClienteUpdateSchema:
            setattr(obj, key, getattr(request, key))
        obj.save()
        obj.id = str(obj.id)
        obj.endereco_id = str(obj.endereco_id)
        return cliente_pb2.Cliente(**model_to_dict(obj))

    def Delete(self, request, context):
        try:
            obj = Cliente.get(Cliente.id == request.id)
        except DoesNotExist:
            return cliente_pb2.Cliente()
        endereco = endereco_pb2.Endereco(id=str(obj.endereco_id))
        stub = get_endereco_stub()
        stub.Delete(endereco)
        obj.delete_instance()
        return cliente_pb2.DeleteResponse(
            status="deletado",
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cliente_pb2_grpc.add_ClienteServiceServicer_to_server(
        ClienteServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
