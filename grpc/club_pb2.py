# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: club.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nclub.proto\"G\n\x04\x43lub\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x14\n\x0cuser_id_list\x18\x04 \x03(\r\"\x19\n\x0b\x43lubRequest\x12\n\n\x02id\x18\x01 \x01(\r\"C\n\x0c\x43lubResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x04\x63lub\x18\x03 \x01(\x0b\x32\x05.Club27\n\x0b\x43lubManager\x12(\n\x07GetClub\x12\x0c.ClubRequest\x1a\r.ClubResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'club_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLUB._serialized_start=14
  _CLUB._serialized_end=85
  _CLUBREQUEST._serialized_start=87
  _CLUBREQUEST._serialized_end=112
  _CLUBRESPONSE._serialized_start=114
  _CLUBRESPONSE._serialized_end=181
  _CLUBMANAGER._serialized_start=183
  _CLUBMANAGER._serialized_end=238
# @@protoc_insertion_point(module_scope)
