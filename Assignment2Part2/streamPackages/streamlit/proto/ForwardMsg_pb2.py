# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/ForwardMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import Delta_pb2 as streamlit_dot_proto_dot_Delta__pb2
from streamlit.proto import NewReport_pb2 as streamlit_dot_proto_dot_NewReport__pb2
from streamlit.proto import PageConfig_pb2 as streamlit_dot_proto_dot_PageConfig__pb2
from streamlit.proto import PageInfo_pb2 as streamlit_dot_proto_dot_PageInfo__pb2
from streamlit.proto import SessionEvent_pb2 as streamlit_dot_proto_dot_SessionEvent__pb2
from streamlit.proto import SessionState_pb2 as streamlit_dot_proto_dot_SessionState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/ForwardMsg.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n streamlit/proto/ForwardMsg.proto\x1a\x1bstreamlit/proto/Delta.proto\x1a\x1fstreamlit/proto/NewReport.proto\x1a streamlit/proto/PageConfig.proto\x1a\x1estreamlit/proto/PageInfo.proto\x1a\"streamlit/proto/SessionEvent.proto\x1a\"streamlit/proto/SessionState.proto\"\x92\x04\n\nForwardMsg\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12%\n\x08metadata\x18\x02 \x01(\x0b\x32\x13.ForwardMsgMetadata\x12 \n\nnew_report\x18\x04 \x01(\x0b\x32\n.NewReportH\x00\x12\x17\n\x05\x64\x65lta\x18\x05 \x01(\x0b\x32\x06.DeltaH\x00\x12&\n\x11page_info_changed\x18\x0c \x01(\x0b\x32\t.PageInfoH\x00\x12*\n\x13page_config_changed\x18\r \x01(\x0b\x32\x0b.PageConfigH\x00\x12;\n\x0freport_finished\x18\x06 \x01(\x0e\x32 .ForwardMsg.ReportFinishedStatusH\x00\x12 \n\x16upload_report_progress\x18\x07 \x01(\rH\x00\x12\x19\n\x0freport_uploaded\x18\x08 \x01(\tH\x00\x12.\n\x15session_state_changed\x18\t \x01(\x0b\x32\r.SessionStateH\x00\x12&\n\rsession_event\x18\n \x01(\x0b\x32\r.SessionEventH\x00\x12\x12\n\x08ref_hash\x18\x0b \x01(\tH\x00\"R\n\x14ReportFinishedStatus\x12\x19\n\x15\x46INISHED_SUCCESSFULLY\x10\x00\x12\x1f\n\x1b\x46INISHED_WITH_COMPILE_ERROR\x10\x01\x42\x06\n\x04type\"r\n\x12\x46orwardMsgMetadata\x12\x11\n\tcacheable\x18\x01 \x01(\x08\x12\x12\n\ndelta_path\x18\x02 \x03(\r\x12\x35\n\x16\x65lement_dimension_spec\x18\x03 \x01(\x0b\x32\x15.ElementDimensionSpec\"5\n\x14\x45lementDimensionSpec\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\rb\x06proto3'
  ,
  dependencies=[streamlit_dot_proto_dot_Delta__pb2.DESCRIPTOR,streamlit_dot_proto_dot_NewReport__pb2.DESCRIPTOR,streamlit_dot_proto_dot_PageConfig__pb2.DESCRIPTOR,streamlit_dot_proto_dot_PageInfo__pb2.DESCRIPTOR,streamlit_dot_proto_dot_SessionEvent__pb2.DESCRIPTOR,streamlit_dot_proto_dot_SessionState__pb2.DESCRIPTOR,])



_FORWARDMSG_REPORTFINISHEDSTATUS = _descriptor.EnumDescriptor(
  name='ReportFinishedStatus',
  full_name='ForwardMsg.ReportFinishedStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FINISHED_SUCCESSFULLY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINISHED_WITH_COMPILE_ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=677,
  serialized_end=759,
)
_sym_db.RegisterEnumDescriptor(_FORWARDMSG_REPORTFINISHEDSTATUS)


_FORWARDMSG = _descriptor.Descriptor(
  name='ForwardMsg',
  full_name='ForwardMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ForwardMsg.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ForwardMsg.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_report', full_name='ForwardMsg.new_report', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delta', full_name='ForwardMsg.delta', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_info_changed', full_name='ForwardMsg.page_info_changed', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_config_changed', full_name='ForwardMsg.page_config_changed', index=5,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_finished', full_name='ForwardMsg.report_finished', index=6,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upload_report_progress', full_name='ForwardMsg.upload_report_progress', index=7,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_uploaded', full_name='ForwardMsg.report_uploaded', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_state_changed', full_name='ForwardMsg.session_state_changed', index=9,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_event', full_name='ForwardMsg.session_event', index=10,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ref_hash', full_name='ForwardMsg.ref_hash', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FORWARDMSG_REPORTFINISHEDSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='ForwardMsg.type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=237,
  serialized_end=767,
)


_FORWARDMSGMETADATA = _descriptor.Descriptor(
  name='ForwardMsgMetadata',
  full_name='ForwardMsgMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cacheable', full_name='ForwardMsgMetadata.cacheable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delta_path', full_name='ForwardMsgMetadata.delta_path', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='element_dimension_spec', full_name='ForwardMsgMetadata.element_dimension_spec', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=769,
  serialized_end=883,
)


_ELEMENTDIMENSIONSPEC = _descriptor.Descriptor(
  name='ElementDimensionSpec',
  full_name='ElementDimensionSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='ElementDimensionSpec.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='ElementDimensionSpec.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=885,
  serialized_end=938,
)

_FORWARDMSG.fields_by_name['metadata'].message_type = _FORWARDMSGMETADATA
_FORWARDMSG.fields_by_name['new_report'].message_type = streamlit_dot_proto_dot_NewReport__pb2._NEWREPORT
_FORWARDMSG.fields_by_name['delta'].message_type = streamlit_dot_proto_dot_Delta__pb2._DELTA
_FORWARDMSG.fields_by_name['page_info_changed'].message_type = streamlit_dot_proto_dot_PageInfo__pb2._PAGEINFO
_FORWARDMSG.fields_by_name['page_config_changed'].message_type = streamlit_dot_proto_dot_PageConfig__pb2._PAGECONFIG
_FORWARDMSG.fields_by_name['report_finished'].enum_type = _FORWARDMSG_REPORTFINISHEDSTATUS
_FORWARDMSG.fields_by_name['session_state_changed'].message_type = streamlit_dot_proto_dot_SessionState__pb2._SESSIONSTATE
_FORWARDMSG.fields_by_name['session_event'].message_type = streamlit_dot_proto_dot_SessionEvent__pb2._SESSIONEVENT
_FORWARDMSG_REPORTFINISHEDSTATUS.containing_type = _FORWARDMSG
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['new_report'])
_FORWARDMSG.fields_by_name['new_report'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['delta'])
_FORWARDMSG.fields_by_name['delta'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['page_info_changed'])
_FORWARDMSG.fields_by_name['page_info_changed'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['page_config_changed'])
_FORWARDMSG.fields_by_name['page_config_changed'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['report_finished'])
_FORWARDMSG.fields_by_name['report_finished'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['upload_report_progress'])
_FORWARDMSG.fields_by_name['upload_report_progress'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['report_uploaded'])
_FORWARDMSG.fields_by_name['report_uploaded'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['session_state_changed'])
_FORWARDMSG.fields_by_name['session_state_changed'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['session_event'])
_FORWARDMSG.fields_by_name['session_event'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSG.oneofs_by_name['type'].fields.append(
  _FORWARDMSG.fields_by_name['ref_hash'])
_FORWARDMSG.fields_by_name['ref_hash'].containing_oneof = _FORWARDMSG.oneofs_by_name['type']
_FORWARDMSGMETADATA.fields_by_name['element_dimension_spec'].message_type = _ELEMENTDIMENSIONSPEC
DESCRIPTOR.message_types_by_name['ForwardMsg'] = _FORWARDMSG
DESCRIPTOR.message_types_by_name['ForwardMsgMetadata'] = _FORWARDMSGMETADATA
DESCRIPTOR.message_types_by_name['ElementDimensionSpec'] = _ELEMENTDIMENSIONSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ForwardMsg = _reflection.GeneratedProtocolMessageType('ForwardMsg', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDMSG,
  '__module__' : 'streamlit.proto.ForwardMsg_pb2'
  # @@protoc_insertion_point(class_scope:ForwardMsg)
  })
_sym_db.RegisterMessage(ForwardMsg)

ForwardMsgMetadata = _reflection.GeneratedProtocolMessageType('ForwardMsgMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDMSGMETADATA,
  '__module__' : 'streamlit.proto.ForwardMsg_pb2'
  # @@protoc_insertion_point(class_scope:ForwardMsgMetadata)
  })
_sym_db.RegisterMessage(ForwardMsgMetadata)

ElementDimensionSpec = _reflection.GeneratedProtocolMessageType('ElementDimensionSpec', (_message.Message,), {
  'DESCRIPTOR' : _ELEMENTDIMENSIONSPEC,
  '__module__' : 'streamlit.proto.ForwardMsg_pb2'
  # @@protoc_insertion_point(class_scope:ElementDimensionSpec)
  })
_sym_db.RegisterMessage(ElementDimensionSpec)


# @@protoc_insertion_point(module_scope)
