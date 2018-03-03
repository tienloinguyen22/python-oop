class Properties():
	def __init__(self, square='', beds='', baths='', **kwargs):
		super().__init__(**kwargs)
		self.square = square
		self.bed_rooms = beds
		self.bath_rooms = baths

	def display(self):
		print('PROPERTY INFORMATION: ')
		print('==================================')
		print('Square feet: {}'.format(self.square))
		print('Number of bedrooms: {}'.format(self.bed_rooms))
		print('Number of bathrooms: {}'.format(self.bath_rooms))

	def prompt_init():
		return dict(
			square = input('Enter Square root: '),
			beds = input('Number of bedrooms: '),
			baths = input('Number of bathrooms: '))
	prompt_init = staticmethod(prompt_init)

def check_valid(prompt_str, valid_list):
	value = input(prompt_str)
	if value not in valid_list:
		print('Not valid !!!')
		check_valid(prompt_str, valid_list)
	return value

class Apartment(Properties):
	def __init__(self, balcony='', laundry='', **kwargs):
		super().__init__(**kwargs)
		self.balcony = balcony
		self.laundry = laundry

	def display(self):
		super().display()
		print('APARTMENT INFORMATION: ')
		print('===================================')
		print('Balcony: {}'.format(self.balcony))
		print('Laundry: {}'.format(self.laundry))

	def prompt_init():
		valid_balcony = ['yes', 'no', 'solarium']
		valid_laundry = ['coin','ensuite','none']
		parent_init = Properties.prompt_init()
		balcony = check_valid('Balcony: ', valid_balcony)
		laundry = check_valid('Laundry: ', valid_laundry)
		parent_init.update({'balcony': balcony, 'laundry': laundry})
		return parent_init
	prompt_init = staticmethod(prompt_init)

class House(Properties):
	def __init__(self, stories='', garage='', fenced='', **kwargs):
		super().__init__(**kwargs)
		self.stories = stories
		self.garage = garage
		self.fenced = fenced

	def display(self):
		super().display()
		print('HOUSE INFORMATION: ')
		print('====================================')
		print('Number of stories: {}'.format(self.stories))
		print('Garage: {}'.format(self.garage))
		print('Fenced yeard: {}'.format(self.fenced))

	def prompt_init():
		valid_garage = ['attached', 'detached', 'none']
		parent_init = Properties.prompt_init()
		stories = input('Number of stories: ')
		garage = check_valid('Garage: ', valid_garage)
		fenced = input('Fenced yeard: ')
		parent_init.update({'stories': stories, 'garage': garage, 'fenced': fenced})
		return parent_init
	prompt_init = staticmethod(prompt_init)

class Purchase():
	def __init__(self, price, taxes):
		self.price = price
		self.taxes = taxes

	def display(self):
		print('PURCHASE INFORMATION: ')
		print('======================================')
		PRINT('Price: {}'.format(self.price))
		print('Estimate taxes: {}'.format(self.taxes))

	def prompt_init():
		return dict(price = input('Price: '),
					taxes = input('Taxes: '))
	prompt_init = staticmethod(prompt_init)

class Rental():
	def __init__(self, furnished, utilities, rent):
		self.furnished = furnished
		self.utilities = utilities
		self.rent = rent

	def display(self):
		print('RENTAL INFORMATION: ')
		print('=======================================')
		print('Furnished: {}'.format(self.furnished))
		print('Utilities: {}'.format(self.utilities))
		print('Rent price: {}'.format(self.rent))

	def prompt_init():
		return dict(furnished = input('Furnished: '),
					utilities = input('Utilities: '),
					rent = input('Rent price: '))
	prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Apartment, Purchase):
	def prompt_init():
		init = Apartment.prompt_init()
		init.update(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class ApartmentRental(Apartment, Rental):
	def prompt_init():
		init = Apartment.prompt_init()
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class HousePurchase(House, Purchase):
	def prompt_init():
		init = House.prompt_init()
		init.update(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class HouseRental(House, Rental):
	def prompt_init():
		init = House.prompt_init()
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class Agent():
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.property_list = []

	def view_properties(self):
		if self.property_list:
			for property in self.property_list:
				property.display()
		else:
			print('U dont have any property !!')

	def add_properties(self):
		type_map = {
					('apartment','purchase'): ApartmentPurchase,
					('apartment', 'rental'): ApartmentRental,
					('house', 'purchase'): HousePurchase,
					('house', 'rental'): HouseRental}

		proper = input('Property type: ')
		pay = input('Payment type: ')
		type = type_map[(proper, pay)]
		kwargs = type.prompt_init()
		self.property_list.append(type(**kwargs))
		print('Add property successfully !!!')











