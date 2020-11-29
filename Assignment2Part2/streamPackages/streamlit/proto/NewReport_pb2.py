# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/NewReport.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import SessionState_pb2 as streamlit_dot_proto_dot_SessionState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/NewReport.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fstreamlit/proto/NewReport.proto\x1a\"streamlit/proto/SessionState.proto\"\x88\x01\n\tNewReport\x12\x1f\n\ninitialize\x18\x01 \x01(\x0b\x32\x0b.Initialize\x12\x11\n\treport_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0bscript_path\x18\x04 \x01(\t\x12$\n\rdeploy_params\x18\x05 \x01(\x0b\x32\r.DeployParams\"\xbf\x01\n\nInitialize\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x17\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x07.Config\x12*\n\x10\x65nvironment_info\x18\x03 \x01(\x0b\x32\x10.EnvironmentInfo\x12$\n\rsession_state\x18\x04 \x01(\x0b\x32\r.SessionState\x12\x14\n\x0c\x63ommand_line\x18\x05 \x01(\t\x12\x12\n\nsession_id\x18\x06 \x01(\t\"\x8e\x01\n\x06\x43onfig\x12\x17\n\x0fsharing_enabled\x18\x01 \x01(\x08\x12\x1a\n\x12gather_usage_stats\x18\x02 \x01(\x08\x12\x1e\n\x16max_cached_message_age\x18\x03 \x01(\x05\x12\x14\n\x0cmapbox_token\x18\x04 \x01(\t\x12\x19\n\x11\x61llow_run_on_save\x18\x05 \x01(\x08\"j\n\x08UserInfo\x12\x17\n\x0finstallation_id\x18\x01 \x01(\t\x12\x1a\n\x12installation_id_v1\x18\x03 \x01(\t\x12\x1a\n\x12installation_id_v2\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"D\n\x0f\x45nvironmentInfo\x12\x19\n\x11streamlit_version\x18\x01 \x01(\t\x12\x16\n\x0epython_version\x18\x02 \x01(\t\"B\n\x0c\x44\x65ployParams\x12\x12\n\nrepository\x18\x01 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x02 \x01(\t\x12\x0e\n\x06module\x18\x03 \x01(\tb\x06proto3'
  ,
  dependencies=[streamlit_dot_proto_dot_SessionState__pb2.DESCRIPTOR,])




_NEWREPORT = _descriptor.Descriptor(
  name='NewReport',
  full_name='NewReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='initialize', full_name='NewReport.initialize', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_id', full_name='NewReport.report_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='NewReport.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='script_path', full_name='NewReport.script_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deploy_params', full_name='NewReport.deploy_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=72,
  serialized_end=208,
)


_INITIALIZE = _descriptor.Descriptor(
  name='Initialize',
  full_name='Initialize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='Initialize.user_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='Initialize.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environment_info', full_name='Initialize.environment_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_state', full_name='Initialize.session_state', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_line', full_name='Initialize.command_line', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='Initialize.session_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=211,
  serialized_end=402,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sharing_enabled', full_name='Config.sharing_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gather_usage_stats', full_name='Config.gather_usage_stats', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_cached_message_age', full_name='Config.max_cached_message_age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapbox_token', full_name='Config.mapbox_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_run_on_save', full_name='Config.allow_run_on_save', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=405,
  serialized_end=547,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='installation_id', full_name='UserInfo.installation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='installation_id_v1', full_name='UserInfo.installation_id_v1', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='installation_id_v2', full_name='UserInfo.installation_id_v2', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='UserInfo.email', index=3,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=549,
  serialized_end=655,
)


_ENVIRONMENTINFO = _descriptor.Descriptor(
  name='EnvironmentInfo',
  full_name='EnvironmentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='streamlit_version', full_name='EnvironmentInfo.streamlit_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='python_version', full_name='EnvironmentInfo.python_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=657,
  serialized_end=725,
)


_DEPLOYPARAMS = _descriptor.Descriptor(
  name='DeployParams',
  full_name='DeployParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='DeployParams.repository', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='branch', full_name='DeployParams.branch', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='DeployParams.module', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=727,
  serialized_end=793,
)

_NEWREPORT.fields_by_name['initialize'].message_type = _INITIALIZE
_NEWREPORT.fields_by_name['deploy_params'].message_type = _DEPLOYPARAMS
_INITIALIZE.fields_by_name['user_info'].message_type = _USERINFO
_INITIALIZE.fields_by_name['config'].message_type = _CONFIG
_INITIALIZE.fields_by_name['environment_info'].message_type = _ENVIRONMENTINFO
_INITIALIZE.fields_by_name['session_state'].message_type = streamlit_dot_proto_dot_SessionState__pb2._SESSIONSTATE
DESCRIPTOR.message_types_by_name['NewReport'] = _NEWREPORT
DESCRIPTOR.message_types_by_name['Initialize'] = _INITIALIZE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['EnvironmentInfo'] = _ENVIRONMENTINFO
DESCRIPTOR.message_types_by_name['DeployParams'] = _DEPLOYPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewReport = _reflection.GeneratedProtocolMessageType('NewReport', (_message.Message,), {
  'DESCRIPTOR' : _NEWREPORT,
  '__module__' : 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:NewReport)
  })
_sym_db.RegisterMessage(NewReport)

Initialize = _reflection.GeneratedProtocolMessageType('Initialize', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZE,
  '__module__' : 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:Initialize)
  })
_sym_db.RegisterMessage(Initialize)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  })
_sym_db.RegisterMessage(Config)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

EnvironmentInfo = _reflection.GeneratedProtocolMessageType('EnvironmentInfo', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENTINFO,
  '__module__' : 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:EnvironmentInfo)
  })
_sym_db.RegisterMessage(EnvironmentInfo)

DeployParams = _reflection.GeneratedProtocolMessageType('DeployParams', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYPARAMS,
  '__module__' : 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:DeployParams)
  })
_sym_db.RegisterMessage(DeployParams)


# @@protoc_insertion_point(module_scope)
