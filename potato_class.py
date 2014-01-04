from crop_class import *

class Potato(Crop):
	"""A potato crop"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default value for potato
		#growth rate = 1; light need = 3; water need = 6
		super().__init__(1,3,6)
		self._type = "Potato"

def main():
	raw_input()
	#create a new potato crop
	potato_crop = Potato()

	print(potato_crop.report())
	#manually grow the crop
	manual_grow(potato_crop)
	print(potato_crop.report())
	raw_input()

if __name__ == "__main__":
	main()
	raw_input()
	
