import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from myphone import number

def get_location_info(phone_number):
    pep_number = phonenumbers.parse(phone_number, "FR")
    location = geocoder.description_for_number(pep_number, 'fr')
    service_provider = phonenumbers.parse(phone_number, "FR")
    carrier_name = carrier.name_for_number(service_provider, 'fr')
    return location, carrier_name

def get_coordinates(location, api_key):
    geocoder = OpenCageGeocode(api_key)
    query = str(location)
    results = geocoder.geocode(query)
    if results and 'geometry' in results[0]:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        return lat, lng
    return None

def create_map_and_save(location, coordinates, file_name="mylocation.html"):
    my_map = folium.Map(location=coordinates, zoom_start=9)
    folium.Marker(coordinates, popup=location).add_to(my_map)
    my_map.save(file_name)

if __name__ == "__main__":
    api_key = 'f2b52a0a3b60420f9d40ba89ad94c8fb'

    location, carrier_name = get_location_info(number)
    print(location)
    print(carrier_name)

    coordinates = get_coordinates(location, api_key)
    if coordinates:
        print(coordinates)
        create_map_and_save(location, coordinates)
    else:
        print("Coordinates not found.")
