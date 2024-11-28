import random
import json
import xml.etree.ElementTree as ET
import csv

def weather_data(cities):
    conditions = ['Rainy', 'Windy', 'Sunny', 'Snowy', 'Cloudy', 'Stormy']
    return {
        city: {
            'Temperature (°C)': round(random.uniform(-10, 40), 1),
            'Humidity (%)': random.randint(20, 100),
            'Wind Speed (km/h)': round(random.uniform(0, 20), 1),
            'Condition': random.choice(conditions),
        }
        for city in cities
    }

def save_data_to_json(weather_data, file_name):
    with open(file_name, 'w') as file:
        json.dump(weather_data, file, indent=4)
    print(f"Weather data saved to '{file_name}' (JSON format).")

def save_data_to_csv(weather_data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'Temperature (°C)', 'Humidity (%)', 'Wind Speed (km/h)', 'Condition'])
        writer.writerows(
            [city, data['Temperature (°C)'], data['Humidity (%)'], data['Wind Speed (km/h)'], data['Condition']]
            for city, data in weather_data.items()
        )
    print(f"Weather data saved to '{file_name}' (CSV format).")

def convert_to_xml(weather_data):
    root = ET.Element("WeatherData")
    for city, data in weather_data.items():
        city_element = ET.SubElement(root, "City", name=city)
        for key, value in data.items():
            ET.SubElement(city_element, key.replace(" ", "").replace("(", "").replace(")", "")).text = str(value)
    return ET.tostring(root, encoding='unicode', method='xml')

cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Mumbai']
weather_data = weather_data(cities)

for city, data in weather_data.items():
    print(f"{city}: {data}")

save_data_to_json(weather_data, "weather.json")
save_data_to_csv(weather_data, "weather.csv")

print("\nXML Format:")
print(convert_to_xml(weather_data))

# # xml schema

# data = """
#     <xs:element name="WeatherData">
#         <xs:complexType>
#             <xs:sequence>
#                 <xs:element name="City">
#                     <xs:complexType>
#                         <xs:sequence>
#                             <xs:element name="TemperatureC" type="xs:float"/>
#                             <xs:element name="Humidity" type="xs:int"/>
#                             <xs:element name="WindSpeedkmh" type="xs:float"/>
#                             <xs:element name="Condition" type="xs:string"/>
#                         </xs:sequence>
#                         <xs:attribute name="name" type="xs:string" use="required"/>
#                     </xs:complexType>
#                 </xs:element>
#             </xs:sequence>
#         </xs:complexType>
#     </xs:element>
# </xs:schema>
# """
