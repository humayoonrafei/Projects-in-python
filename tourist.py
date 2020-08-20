destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
 traveler_destination1=traveler[1]
 return get_destination_index(traveler_destination1)



print(get_traveler_location(test_traveler))

