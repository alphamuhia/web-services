import xml.etree.ElementTree as ET
import json

# data = ''' 
# <bookstore>
#     <book id="1">
#         <title>The front door</title>
#         <author>alpha peter</author>
#         <price>29.99</price>
#         <year>2010</year>
#         <rating>6 stars</rating>
#     </book>
#     <book id="2">
#         <title>The back door</title>
#         <author>muhia alpha</author>
#         <price>29.99</price>
#         <year>1015</year>
#         <rating>4 stars</rating>
#     </book>
# </bookstore>'''

# book = ET.fromstring(data)

# for book in book.findall('book'):
#     title = book.find('title').text
#     author = book.find('author').text
#     price = book.find('price').text
#     year = book.find('year').text
#     rating = book.find('rating').text
    
#     # Print the details for each book
#     print(f"Title: {title}")
#     print(f"Author: {author}")
#     print(f"Price: {price}")
#     print(f"Year: {year}")
#     print(f"Rating: {rating}")




#     # xml schema


# data = ''' 
# <bookstore>
#     <book id="1">
#         <title>The front door</title>
#         <author>alpha peter</author>
#         <price>29.99</price>
#         <year>2010</year>
#         <rating>6 stars</rating>
#     </book>
#     <book id="2">
#         <title>The back door</title>
#         <author>muhia alpha</author>
#         <price>29.99</price>
#         <year>1015</year>
#         <rating>4 stars</rating>
#     </book>
# </bookstore>'''

# data = '''<?xml version="1.0" encoding="UTF-8"?>
# <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

#     <xs:element name="bookstore">
#         <xs:complexType>
#             <xs:sequence>
#                 <xs:element name="book">
#                     <xs:complexType>
#                         <xs:sequence>
#                             <xs:element name="title" type="xs:string"/>
#                             <xs:element name="author" type="xs:string"/>
#                             <xs:element name="price" type="xs:decimal"/>
#                             <xs:element name="year" type="xs:positiveInteger"/>
#                             <xs:element name="rating" type="xs:string"/>
#                         </xs:sequence>
#                         <xs:attribute name="id" type="xs:positiveInteger" use="required"/>
#                     </xs:complexType>
#                 </xs:element>
#             </xs:sequence>
#         </xs:complexType>
#     </xs:element>

# </xs:schema>
# '''



# # JSON

# student = {
#     "name":"peter",
#     "age": 20,
#     "class": "Softwere eng",
#     "adress": "Rwai",
#     "phone_number": "+254745937215"
# }

# with open("data.json", 'w') as file:
#     json.dump(student ,file)

# with open('data.json', 'r') as file:
#     student = json.load(file)

