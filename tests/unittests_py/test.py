import unittest

import sys
from pathlib import Path

sys.path.append( str((Path(__file__).parent / "../../datamodel_io").resolve() ))

import cityModel, pointCloud

class TestBuildings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.building_shp_file = str((Path(__file__).parent / ".."/ "data" / "MinimalCase" / "propertyMap.shp").resolve())
        cls.building_las_file = str((Path(__file__).parent / ".."/ "data" / "MinimalCase" / "pointcloud.las").resolve())

    def test_load_shp_buildings(self):
        cm = cityModel.loadBuildings(self.building_shp_file,'uuid')
        self.assertEqual(len(cm.buildings),5)

    def test_load_pointcloud(self):
        pc = pointCloud.loadLAS(self.building_las_file, return_serialized = False)
        self.assertEqual(len(pc.points),8148)

if __name__ == '__main__':
    unittest.main()