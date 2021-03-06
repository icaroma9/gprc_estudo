# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cliente.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cliente.proto',
  package='cliente',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcliente.proto\x12\x07\x63liente\"\xd8\x01\n\x07\x43liente\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x11\n\tsobrenome\x18\x03 \x01(\t\x12\x0b\n\x03\x63pf\x18\x04 \x01(\t\x12\x0c\n\x04sexo\x18\x05 \x01(\t\x12\x10\n\x08telefone\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\x12\x13\n\x0b\x65ndereco_id\x18\x08 \x01(\t\x12\x12\n\nlogradouro\x18\t \x01(\t\x12\x0b\n\x03\x63\x65p\x18\n \x01(\t\x12\x0e\n\x06\x62\x61irro\x18\x0b \x01(\t\x12\x0e\n\x06\x63idade\x18\x0c \x01(\t\x12\x0e\n\x06\x65stado\x18\r \x01(\t\" \n\x0e\x44\x65leteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\x89\x02\n\x0e\x43lienteService\x12.\n\x06\x43reate\x12\x10.cliente.Cliente\x1a\x10.cliente.Cliente\"\x00\x12.\n\x04List\x12\x10.cliente.Cliente\x1a\x10.cliente.Cliente\"\x00\x30\x01\x12\x30\n\x08Retrieve\x12\x10.cliente.Cliente\x1a\x10.cliente.Cliente\"\x00\x12.\n\x06Update\x12\x10.cliente.Cliente\x1a\x10.cliente.Cliente\"\x00\x12\x35\n\x06\x44\x65lete\x12\x10.cliente.Cliente\x1a\x17.cliente.DeleteResponse\"\x00\x62\x06proto3'
)




_CLIENTE = _descriptor.Descriptor(
  name='Cliente',
  full_name='cliente.Cliente',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cliente.Cliente.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nome', full_name='cliente.Cliente.nome', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sobrenome', full_name='cliente.Cliente.sobrenome', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpf', full_name='cliente.Cliente.cpf', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sexo', full_name='cliente.Cliente.sexo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='telefone', full_name='cliente.Cliente.telefone', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='cliente.Cliente.email', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endereco_id', full_name='cliente.Cliente.endereco_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logradouro', full_name='cliente.Cliente.logradouro', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cep', full_name='cliente.Cliente.cep', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bairro', full_name='cliente.Cliente.bairro', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cidade', full_name='cliente.Cliente.cidade', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='estado', full_name='cliente.Cliente.estado', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=243,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='cliente.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cliente.DeleteResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=277,
)

DESCRIPTOR.message_types_by_name['Cliente'] = _CLIENTE
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cliente = _reflection.GeneratedProtocolMessageType('Cliente', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTE,
  '__module__' : 'cliente_pb2'
  # @@protoc_insertion_point(class_scope:cliente.Cliente)
  })
_sym_db.RegisterMessage(Cliente)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'cliente_pb2'
  # @@protoc_insertion_point(class_scope:cliente.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)



_CLIENTESERVICE = _descriptor.ServiceDescriptor(
  name='ClienteService',
  full_name='cliente.ClienteService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=280,
  serialized_end=545,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='cliente.ClienteService.Create',
    index=0,
    containing_service=None,
    input_type=_CLIENTE,
    output_type=_CLIENTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='cliente.ClienteService.List',
    index=1,
    containing_service=None,
    input_type=_CLIENTE,
    output_type=_CLIENTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='cliente.ClienteService.Retrieve',
    index=2,
    containing_service=None,
    input_type=_CLIENTE,
    output_type=_CLIENTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='cliente.ClienteService.Update',
    index=3,
    containing_service=None,
    input_type=_CLIENTE,
    output_type=_CLIENTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='cliente.ClienteService.Delete',
    index=4,
    containing_service=None,
    input_type=_CLIENTE,
    output_type=_DELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENTESERVICE)

DESCRIPTOR.services_by_name['ClienteService'] = _CLIENTESERVICE

# @@protoc_insertion_point(module_scope)
