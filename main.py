import phonenumbers
from phone import number
import opencage
import folium
import opencage.geocoder
from phonenumbers import geocoder, carrier

# Provide a default region code
pepnumber = phonenumbers.parse(number, "US")
location = geocoder.description_for_number(pepnumber, "en")
service_provider = carrier.name_for_number(pepnumber, "en")

print(location)
print(service_provider)
from phonenumbers import timezone
time_zone = timezone.time_zones_for_number(pepnumber)
print(time_zone)

from opencage.geocoder import OpenCageGeocode
key= 'add api key'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("Location.html")