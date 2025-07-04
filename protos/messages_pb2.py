# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/messages.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'protos/messages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protos/messages.proto\"q\n\nDeviceInfo\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x19\n\x04type\x18\x02 \x01(\x0e\x32\x0b.DeviceType\x12\x12\n\nip_address\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x13\n\x0bis_actuator\x18\x05 \x01(\x08\"\x18\n\x07\x43ommand\x12\r\n\x05state\x18\x01 \x01(\x08\"\x17\n\x05Query\x12\x0e\n\x06status\x18\x01 \x01(\x08\"<\n\nSensorData\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x0c\n\x04unit\x18\x03 \x01(\t\"\x97\x01\n\x10SmartCityMessage\x12\x1e\n\x07\x64\x65vices\x18\x01 \x01(\x0b\x32\x0b.DeviceInfoH\x00\x12\x1b\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x08.CommandH\x00\x12\"\n\x0bsensor_data\x18\x03 \x01(\x0b\x32\x0b.SensorDataH\x00\x12\x17\n\x05query\x18\x04 \x01(\x0b\x32\x06.QueryH\x00\x42\t\n\x07payload*x\n\nDeviceType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nLIGHT_POST\x10\x01\x12\x11\n\rTRAFFIC_LIGHT\x10\x02\x12\n\n\x06\x43\x41MERA\x10\x03\x12\x16\n\x12TEMPERATURE_SENSOR\x10\x04\x12\x16\n\x12\x41IR_QUALITY_SENSOR\x10\x05*)\n\x07TLState\x12\t\n\x05GREEN\x10\x00\x12\n\n\x06YELLOW\x10\x01\x12\x07\n\x03RED\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DEVICETYPE']._serialized_start=407
  _globals['_DEVICETYPE']._serialized_end=527
  _globals['_TLSTATE']._serialized_start=529
  _globals['_TLSTATE']._serialized_end=570
  _globals['_DEVICEINFO']._serialized_start=25
  _globals['_DEVICEINFO']._serialized_end=138
  _globals['_COMMAND']._serialized_start=140
  _globals['_COMMAND']._serialized_end=164
  _globals['_QUERY']._serialized_start=166
  _globals['_QUERY']._serialized_end=189
  _globals['_SENSORDATA']._serialized_start=191
  _globals['_SENSORDATA']._serialized_end=251
  _globals['_SMARTCITYMESSAGE']._serialized_start=254
  _globals['_SMARTCITYMESSAGE']._serialized_end=405
# @@protoc_insertion_point(module_scope)
