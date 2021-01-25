import uuid
from concurrent import futures

import grpc
from google.protobuf import json_format
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict

import endereco_pb2
import endereco_pb2_grpc
from db import Endereco


class EnderecoServiceServicer(endereco_pb2_grpc.EnderecoServiceServicer):
    def Create(self, request, context):
        obj = Endereco.create(
            id=uuid.uuid4(), **json_format.MessageToDict(request)
        )
        obj.id = str(obj.id)
        return endereco_pb2.Endereco(**model_to_dict(obj))

    def List(self, request, context):
        for obj in Endereco.select():
            obj.id = str(obj.id)
            yield endereco_pb2.Endereco(**model_to_dict(obj))

    def Retrieve(self, request, context):
        try:
            obj = Endereco.get(Endereco.id == request.id)
        except DoesNotExist:
            return endereco_pb2.Endereco()
        obj.id = str(obj.id)
        return endereco_pb2.Endereco(**model_to_dict(obj))

    def Update(self, request, context):
        try:
            obj = Endereco.get(Endereco.id == request.id)
        except DoesNotExist:
            return endereco_pb2.Endereco()
        for key, value in json_format.MessageToDict(request).items():
            setattr(obj, key, value)
        obj.save()
        obj.id = str(obj.id)
        return endereco_pb2.Endereco(**model_to_dict(obj))

    def Delete(self, request, context):
        try:
            obj = Endereco.get(Endereco.id == request.id)
        except DoesNotExist:
            return endereco_pb2.Endereco()
        obj.delete_instance()
        return endereco_pb2.DeleteResponse(
            status="deletado",
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    endereco_pb2_grpc.add_EnderecoServiceServicer_to_server(
        EnderecoServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
