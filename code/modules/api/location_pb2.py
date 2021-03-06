# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='location.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0elocation.proto\"f\n\x15\x43reateLocationRequest\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\t\x12\x15\n\rcreation_time\x18\x04 \x01(\t\")\n\x16\x43reateLocationResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\")\n\x12GetLocationRequest\x12\x13\n\x0blocation_id\x18\x01 \x01(\x05\"n\n\x08Location\x12\x13\n\x0blocation_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12\x10\n\x08latitude\x18\x04 \x01(\t\x12\x15\n\rcreation_time\x18\x05 \x01(\t\"f\n\x1bListExposedLocationsRequest\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\x12\x0e\n\x06meters\x18\x04 \x01(\x05\"\x82\x01\n\x0f\x45xposedLocation\x12\x13\n\x0blocation_id\x18\x01 \x01(\x05\x12\x19\n\x11\x65xposed_person_id\x18\x02 \x01(\x05\x12\x14\n\x0c\x65xposed_long\x18\x03 \x01(\t\x12\x13\n\x0b\x65xposed_lat\x18\x04 \x01(\t\x12\x14\n\x0c\x65xposed_time\x18\x05 \x01(\t\"C\n\x1cListExposedLocationsResponse\x12#\n\tlocations\x18\x01 \x03(\x0b\x32\x10.ExposedLocation2\xd8\x01\n\x0fLocationService\x12\x41\n\x0e\x43reateLocation\x12\x16.CreateLocationRequest\x1a\x17.CreateLocationResponse\x12-\n\x0bGetLocation\x12\x13.GetLocationRequest\x1a\t.Location\x12S\n\x14ListExposedLocations\x12\x1c.ListExposedLocationsRequest\x1a\x1d.ListExposedLocationsResponseb\x06proto3'
)




_CREATELOCATIONREQUEST = _descriptor.Descriptor(
  name='CreateLocationRequest',
  full_name='CreateLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='CreateLocationRequest.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='CreateLocationRequest.longitude', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='CreateLocationRequest.latitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='CreateLocationRequest.creation_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=18,
  serialized_end=120,
)


_CREATELOCATIONRESPONSE = _descriptor.Descriptor(
  name='CreateLocationResponse',
  full_name='CreateLocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='CreateLocationResponse.message', index=0,
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
  serialized_start=122,
  serialized_end=163,
)


_GETLOCATIONREQUEST = _descriptor.Descriptor(
  name='GetLocationRequest',
  full_name='GetLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location_id', full_name='GetLocationRequest.location_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=165,
  serialized_end=206,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location_id', full_name='Location.location_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='Location.person_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='Location.creation_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=208,
  serialized_end=318,
)


_LISTEXPOSEDLOCATIONSREQUEST = _descriptor.Descriptor(
  name='ListExposedLocationsRequest',
  full_name='ListExposedLocationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='ListExposedLocationsRequest.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='ListExposedLocationsRequest.start_date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='ListExposedLocationsRequest.end_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meters', full_name='ListExposedLocationsRequest.meters', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=320,
  serialized_end=422,
)


_EXPOSEDLOCATION = _descriptor.Descriptor(
  name='ExposedLocation',
  full_name='ExposedLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location_id', full_name='ExposedLocation.location_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exposed_person_id', full_name='ExposedLocation.exposed_person_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exposed_long', full_name='ExposedLocation.exposed_long', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exposed_lat', full_name='ExposedLocation.exposed_lat', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exposed_time', full_name='ExposedLocation.exposed_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=425,
  serialized_end=555,
)


_LISTEXPOSEDLOCATIONSRESPONSE = _descriptor.Descriptor(
  name='ListExposedLocationsResponse',
  full_name='ListExposedLocationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locations', full_name='ListExposedLocationsResponse.locations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=557,
  serialized_end=624,
)

_LISTEXPOSEDLOCATIONSRESPONSE.fields_by_name['locations'].message_type = _EXPOSEDLOCATION
DESCRIPTOR.message_types_by_name['CreateLocationRequest'] = _CREATELOCATIONREQUEST
DESCRIPTOR.message_types_by_name['CreateLocationResponse'] = _CREATELOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetLocationRequest'] = _GETLOCATIONREQUEST
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['ListExposedLocationsRequest'] = _LISTEXPOSEDLOCATIONSREQUEST
DESCRIPTOR.message_types_by_name['ExposedLocation'] = _EXPOSEDLOCATION
DESCRIPTOR.message_types_by_name['ListExposedLocationsResponse'] = _LISTEXPOSEDLOCATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateLocationRequest = _reflection.GeneratedProtocolMessageType('CreateLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOCATIONREQUEST,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:CreateLocationRequest)
  })
_sym_db.RegisterMessage(CreateLocationRequest)

CreateLocationResponse = _reflection.GeneratedProtocolMessageType('CreateLocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOCATIONRESPONSE,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:CreateLocationResponse)
  })
_sym_db.RegisterMessage(CreateLocationResponse)

GetLocationRequest = _reflection.GeneratedProtocolMessageType('GetLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOCATIONREQUEST,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:GetLocationRequest)
  })
_sym_db.RegisterMessage(GetLocationRequest)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

ListExposedLocationsRequest = _reflection.GeneratedProtocolMessageType('ListExposedLocationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEXPOSEDLOCATIONSREQUEST,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:ListExposedLocationsRequest)
  })
_sym_db.RegisterMessage(ListExposedLocationsRequest)

ExposedLocation = _reflection.GeneratedProtocolMessageType('ExposedLocation', (_message.Message,), {
  'DESCRIPTOR' : _EXPOSEDLOCATION,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:ExposedLocation)
  })
_sym_db.RegisterMessage(ExposedLocation)

ListExposedLocationsResponse = _reflection.GeneratedProtocolMessageType('ListExposedLocationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEXPOSEDLOCATIONSRESPONSE,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:ListExposedLocationsResponse)
  })
_sym_db.RegisterMessage(ListExposedLocationsResponse)



_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=627,
  serialized_end=843,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateLocation',
    full_name='LocationService.CreateLocation',
    index=0,
    containing_service=None,
    input_type=_CREATELOCATIONREQUEST,
    output_type=_CREATELOCATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLocation',
    full_name='LocationService.GetLocation',
    index=1,
    containing_service=None,
    input_type=_GETLOCATIONREQUEST,
    output_type=_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListExposedLocations',
    full_name='LocationService.ListExposedLocations',
    index=2,
    containing_service=None,
    input_type=_LISTEXPOSEDLOCATIONSREQUEST,
    output_type=_LISTEXPOSEDLOCATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)

DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE

# @@protoc_insertion_point(module_scope)
