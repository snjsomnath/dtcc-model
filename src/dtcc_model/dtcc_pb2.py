# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dtcc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndtcc.proto\x12\x04\x44TCC\" \n\x08Vector2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"+\n\x08Vector3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\".\n\x08Triangle\x12\n\n\x02v0\x18\x01 \x01(\x05\x12\n\n\x02v1\x18\x02 \x01(\x05\x12\n\n\x02v2\x18\x03 \x01(\x05\"=\n\x0bTetrahedron\x12\n\n\x02v0\x18\x01 \x01(\x05\x12\n\n\x02v1\x18\x02 \x01(\x05\x12\n\n\x02v2\x18\x03 \x01(\x05\x12\n\n\x02v3\x18\x04 \x01(\x05\"E\n\rBoundingBox2D\x12\x19\n\x01p\x18\x01 \x01(\x0b\x32\x0e.DTCC.Vector2D\x12\x19\n\x01q\x18\x02 \x01(\x0b\x32\x0e.DTCC.Vector2D\"E\n\rBoundingBox3D\x12\x19\n\x01p\x18\x01 \x01(\x0b\x32\x0e.DTCC.Vector3D\x12\x19\n\x01q\x18\x02 \x01(\x0b\x32\x0e.DTCC.Vector3D\",\n\nMultiPoint\x12\x1e\n\x06points\x18\x01 \x03(\x0b\x32\x0e.DTCC.Vector2D\".\n\x0cMultiPoint3D\x12\x1e\n\x06points\x18\x01 \x03(\x0b\x32\x0e.DTCC.Vector3D\".\n\nLineString\x12 \n\x08vertices\x18\x01 \x03(\x0b\x32\x0e.DTCC.Vector2D\"0\n\x0cLineString3D\x12 \n\x08vertices\x18\x01 \x03(\x0b\x32\x0e.DTCC.Vector3D\".\n\nLinearRing\x12 \n\x08vertices\x18\x01 \x03(\x0b\x32\x0e.DTCC.Vector2D\"K\n\x07Polygon\x12\x1f\n\x05shell\x18\x01 \x01(\x0b\x32\x10.DTCC.LinearRing\x12\x1f\n\x05holes\x18\x02 \x03(\x0b\x32\x10.DTCC.LinearRing\"/\n\x0cMultiPolygon\x12\x1f\n\x08polygons\x18\x01 \x03(\x0b\x32\r.DTCC.Polygon\"n\n\x06Grid2D\x12(\n\x0b\x62oundingBox\x18\x01 \x01(\x0b\x32\x13.DTCC.BoundingBox2D\x12\r\n\x05xSize\x18\x02 \x01(\x05\x12\r\n\x05ySize\x18\x03 \x01(\x05\x12\r\n\x05xStep\x18\x04 \x01(\x02\x12\r\n\x05yStep\x18\x05 \x01(\x02\"\x8c\x01\n\x06Grid3D\x12(\n\x0b\x62oundingBox\x18\x01 \x01(\x0b\x32\x13.DTCC.BoundingBox3D\x12\r\n\x05xSize\x18\x02 \x01(\x05\x12\r\n\x05ySize\x18\x03 \x01(\x05\x12\r\n\x05zSize\x18\x04 \x01(\x05\x12\r\n\x05xStep\x18\x05 \x01(\x02\x12\r\n\x05yStep\x18\x06 \x01(\x02\x12\r\n\x05zStep\x18\x07 \x01(\x02\"8\n\x04Mesh\x12\x10\n\x08vertices\x18\x01 \x03(\x02\x12\x0f\n\x07normals\x18\x02 \x03(\x02\x12\r\n\x05\x66\x61\x63\x65s\x18\x03 \x03(\x05\">\n\nVolumeMesh\x12\x10\n\x08vertices\x18\x01 \x03(\x02\x12\r\n\x05\x63\x65lls\x18\x02 \x03(\x02\x12\x0f\n\x07markers\x18\x03 \x03(\x05\"9\n\x0bGridField2D\x12\x1a\n\x04grid\x18\x01 \x01(\x0b\x32\x0c.DTCC.Grid2D\x12\x0e\n\x06values\x18\x02 \x03(\x02\"9\n\x0bGridField3D\x12\x1a\n\x04grid\x18\x01 \x01(\x0b\x32\x0c.DTCC.Grid3D\x12\x0e\n\x06values\x18\x02 \x03(\x02\"?\n\x11GridVectorField2D\x12\x1a\n\x04grid\x18\x01 \x01(\x0b\x32\x0c.DTCC.Grid2D\x12\x0e\n\x06values\x18\x02 \x03(\x02\"?\n\x11GridVectorField3D\x12\x1a\n\x04grid\x18\x01 \x01(\x0b\x32\x0c.DTCC.Grid3D\x12\x0e\n\x06values\x18\x02 \x03(\x02\"5\n\tMeshField\x12\x18\n\x04mesh\x18\x01 \x01(\x0b\x32\n.DTCC.Mesh\x12\x0e\n\x06values\x18\x02 \x03(\x02\";\n\x0fMeshVectorField\x12\x18\n\x04mesh\x18\x01 \x01(\x0b\x32\n.DTCC.Mesh\x12\x0e\n\x06values\x18\x02 \x03(\x02\"A\n\x0fVolumeMeshField\x12\x1e\n\x04mesh\x18\x01 \x01(\x0b\x32\x10.DTCC.VolumeMesh\x12\x0e\n\x06values\x18\x02 \x03(\x02\"C\n\x11VolumeVectorField\x12\x1e\n\x04mesh\x18\x01 \x01(\x0b\x32\x10.DTCC.VolumeMesh\x12\x0e\n\x06values\x18\x02 \x03(\x02\"\xdd\x01\n\nPointCloud\x12\x0e\n\x06points\x18\x01 \x03(\x02\x12#\n\x06\x62ounds\x18\x02 \x01(\x0b\x32\x13.DTCC.BoundingBox2D\x12\x16\n\x0e\x63lassification\x18\x03 \x03(\r\x12\x11\n\tintensity\x18\x04 \x03(\r\x12\x14\n\x0creturnNumber\x18\x05 \x03(\r\x12\x12\n\nnumReturns\x18\x06 \x03(\r\x12\x1b\n\x13usedClassifications\x18\x07 \x03(\r\x12(\n\x0cgeoreference\x18\x08 \x01(\x0b\x32\x12.DTCC.Georeference\"\x95\x01\n\x08\x42uilding\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12 \n\tfootPrint\x18\x02 \x01(\x0b\x32\r.DTCC.Polygon\x12\x0e\n\x06height\x18\x03 \x01(\x01\x12\x14\n\x0cgroundHeight\x18\x04 \x01(\x01\x12$\n\nroofpoints\x18\x05 \x01(\x0b\x32\x10.DTCC.PointCloud\x12\r\n\x05\x65rror\x18\x06 \x01(\x04\"\xa1\x01\n\tCityModel\x12!\n\tbuildings\x18\x01 \x03(\x0b\x32\x0e.DTCC.Building\x12#\n\x06\x62ounds\x18\x02 \x01(\x0b\x32\x13.DTCC.BoundingBox2D\x12(\n\x0cgeoreference\x18\x03 \x01(\x0b\x32\x12.DTCC.Georeference\x12\"\n\x07terrain\x18\x04 \x01(\x0b\x32\x11.DTCC.GridField2D\"A\n\x0cGeoreference\x12\x0b\n\x03\x63rs\x18\x01 \x01(\t\x12\x0c\n\x04\x65psg\x18\x02 \x01(\x05\x12\n\n\x02x0\x18\x03 \x01(\x01\x12\n\n\x02y0\x18\x04 \x01(\x01\x42\x02H\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dtcc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _VECTOR2D._serialized_start=20
  _VECTOR2D._serialized_end=52
  _VECTOR3D._serialized_start=54
  _VECTOR3D._serialized_end=97
  _TRIANGLE._serialized_start=99
  _TRIANGLE._serialized_end=145
  _TETRAHEDRON._serialized_start=147
  _TETRAHEDRON._serialized_end=208
  _BOUNDINGBOX2D._serialized_start=210
  _BOUNDINGBOX2D._serialized_end=279
  _BOUNDINGBOX3D._serialized_start=281
  _BOUNDINGBOX3D._serialized_end=350
  _MULTIPOINT._serialized_start=352
  _MULTIPOINT._serialized_end=396
  _MULTIPOINT3D._serialized_start=398
  _MULTIPOINT3D._serialized_end=444
  _LINESTRING._serialized_start=446
  _LINESTRING._serialized_end=492
  _LINESTRING3D._serialized_start=494
  _LINESTRING3D._serialized_end=542
  _LINEARRING._serialized_start=544
  _LINEARRING._serialized_end=590
  _POLYGON._serialized_start=592
  _POLYGON._serialized_end=667
  _MULTIPOLYGON._serialized_start=669
  _MULTIPOLYGON._serialized_end=716
  _GRID2D._serialized_start=718
  _GRID2D._serialized_end=828
  _GRID3D._serialized_start=831
  _GRID3D._serialized_end=971
  _MESH._serialized_start=973
  _MESH._serialized_end=1029
  _VOLUMEMESH._serialized_start=1031
  _VOLUMEMESH._serialized_end=1093
  _GRIDFIELD2D._serialized_start=1095
  _GRIDFIELD2D._serialized_end=1152
  _GRIDFIELD3D._serialized_start=1154
  _GRIDFIELD3D._serialized_end=1211
  _GRIDVECTORFIELD2D._serialized_start=1213
  _GRIDVECTORFIELD2D._serialized_end=1276
  _GRIDVECTORFIELD3D._serialized_start=1278
  _GRIDVECTORFIELD3D._serialized_end=1341
  _MESHFIELD._serialized_start=1343
  _MESHFIELD._serialized_end=1396
  _MESHVECTORFIELD._serialized_start=1398
  _MESHVECTORFIELD._serialized_end=1457
  _VOLUMEMESHFIELD._serialized_start=1459
  _VOLUMEMESHFIELD._serialized_end=1524
  _VOLUMEVECTORFIELD._serialized_start=1526
  _VOLUMEVECTORFIELD._serialized_end=1593
  _POINTCLOUD._serialized_start=1596
  _POINTCLOUD._serialized_end=1817
  _BUILDING._serialized_start=1820
  _BUILDING._serialized_end=1969
  _CITYMODEL._serialized_start=1972
  _CITYMODEL._serialized_end=2133
  _GEOREFERENCE._serialized_start=2135
  _GEOREFERENCE._serialized_end=2200
# @@protoc_insertion_point(module_scope)
