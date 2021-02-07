import unittest
import CubeVol
class test_CubeVol(unittest.TestCase):
	def test_volume(self):
                #Testing Numbers
		result = CubeVol.Volume(1)
		self.assertEqual(result, 1)
		
		result = CubeVol.Volume(2)
		self.assertEqual(result, 8)
		
		result = CubeVol.Volume(3)
		self.assertEqual(result, 27)
	def test_volume_negatives(self):
                #Testing negatives
		result = CubeVol.Volume(-1)
		self.assertEqual(result, -1)
		
		result = CubeVol.Volume(-5)
		self.assertEqual(result, -1)
	def test_volume_text(self):
		#Testing text
		result = CubeVol.Volume("Words")
		self.assertEqual(result, -1)
		
		result = CubeVol.Volume("3")
		self.assertEqual(result, -1)
	def test_volume_complex(self):
		#testing complex numbers
		result = CubeVol.Volume(complex(5,2))
		self.assertEqual(result, -1)


if __name__ == "__main__":
        unittest.main()




