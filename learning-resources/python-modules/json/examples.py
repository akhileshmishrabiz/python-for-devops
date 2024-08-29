import json

# 1. Parsing JSON String into Python Object
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)
print("Parsed JSON string into Python dictionary:")
print(python_dict)
print(f"Name: {python_dict['name']}, Age: {python_dict['age']}, City: {python_dict['city']}")

# 2. Converting Python Object to JSON String
python_dict = {"name": "Bob", "age": 25, "city": "Los Angeles"}
json_string = json.dumps(python_dict)
print("\nConverted Python dictionary to JSON string:")
print(json_string)

# 3. Reading JSON from a File
try:
    with open('example.json', 'r') as file:
        data = json.load(file)
        print("\nRead JSON from file 'example.json':")
        print(data)
except FileNotFoundError as e:
    print(f"Error: {e}")

# 4. Writing JSON to a File
data_to_write = {"name": "Charlie", "age": 35, "city": "Chicago"}
with open('example.json', 'w') as file:
    json.dump(data_to_write, file, indent=4)
    print("\nWritten JSON to file 'example.json'")

# 5. Pretty Printing JSON
pretty_json_string = json.dumps(data_to_write, indent=4)
print("\nPretty printed JSON string:")
print(pretty_json_string)

# 6. Handling Complex Data Types
# JSON supports only basic data types (numbers, strings, lists, dictionaries, Booleans, and null). To handle complex data types, use custom serialization.
import datetime

def datetime_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

data_with_date = {"name": "Daisy", "joined": datetime.datetime(2023, 5, 10, 15, 34, 56)}
json_string_with_date = json.dumps(data_with_date, default=datetime_serializer)
print("\nSerialized JSON string with datetime object:")
print(json_string_with_date)

# 7. Decoding JSON with Custom Decoder
class CustomDecoder(json.JSONDecoder):
    def decode(self, s):
        result = super().decode(s)
        if 'joined' in result:
            result['joined'] = datetime.datetime.fromisoformat(result['joined'])
        return result

decoded_data_with_date = json.loads(json_string_with_date, cls=CustomDecoder)
print("\nDecoded JSON string with custom decoder:")
print(decoded_data_with_date)

# 8. Working with JSON Arrays
json_array_string = '[{"name": "Eve", "age": 28}, {"name": "Frank", "age": 32}]'
python_list = json.loads(json_array_string)
print("\nParsed JSON array string into Python list:")
print(python_list)

# 9. Using `json.dumps` with Various Options
data_options = {"name": "George", "active": True, "balance": None, "friends": ["Alice", "Bob"]}
json_string_options = json.dumps(data_options, indent=4, separators=(',', ': '), sort_keys=True)
print("\nJSON string with various options (indentation, separators, sorted keys):")
print(json_string_options)

# 10. Encoding Python Objects with Custom Serialization
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_serializer(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age}
    raise TypeError("Type not serializable")

person = Person("Hannah", 27)
json_string_person = json.dumps(person, default=person_serializer)
print("\nSerialized JSON string with custom object (Person):")
print(json_string_person)
