import math

class sphere:

	# Class attribute, all instances created from this class will have 
	# a shape of sphere 
	shape = 'sphere'
	
	# intiializer/instance attributes
	def __init__ (self, name, radius, mass):
		self.name = name
		self.radius = radius
		self.mass = mass

	# use an instance method to get other attributes like volume, surface area, and density

	# volume of sphere = (4/3)*pi*r^3
	def calculate_volume(self, name, radius):
		volume = (4/3) * math.pi * (math.pow(radius, 3))
		return volume

	# surface area of a sphere = 4*pi*r^2	
	def calculate_surface_area(self, name, radius):
		surface_area = 4 * math.pi * (math.pow(radius, 2))
		return surface_area

	def calculate_density(self, name, volume, mass):
		density = volume/mass
		return density


def main():
	red = sphere('red', 17, 0.25)
	# print(red)
	# print(red.radius, red.mass, red.name)

	volume = red.calculate_volume(red.name, red.radius)
	surface_area = red.calculate_surface_area(red.name, red.radius)
	density = red.calculate_density(red.name, volume, red.mass)

	print('volume: {}'.format(volume))
	print('surface_area: {}'.format(surface_area))
	print('density: {}'.format(density))
	print('alphabetical listing of attributes in the scope of red: {}'.format(dir(red)))

if __name__ == '__main__':
	main()