import googlemaps


class GoogleMapMock:

	def geocode(self, place):
		return [{'formatted_address': 'adress', 'geometry': {'location': 'info location'}}]
