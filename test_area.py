from unittest import TestCase
import area

class TestShapeAreas(TestCase):
    def test_triangle_are(self):
        #A triangle with height 4 and base 5 should have area 10
        self.assertEqual(10, area.triangle_area(4, 5))

    def test_triangle_are_floating_point(self):
        self.assertEqual(12.18, area.triangle_area(4.2, 5.8))

    def test_triangle_negative_height_base_raises_value_exception(self):

        with self.assertRaises(ValueError):
            area.triangle_area(9, -10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10)
#Test for 0 values for both height and base | either one as well
    def test_triangle_base_height_zero(self):
        self.assertRaises(0, area.triangle_area(10, 0))
        self.assertRaises(0,  area.triangle_area(0, 10))  
        self.assertRaises(0, area.triangle_area(0, 0))
            