import json

def process_json():
    try:
        with open(r'C:\Users\DELL\Desktop\Venhan assignment\fileHandlingProcessing\employees.json','r') as file:
            jsonData = file.read()
            obj = json.loads(jsonData)
            print(obj['firstName'])
            print(obj)
    except FileNotFoundError:
        print('File not found')

process_json()

# output:
# Bheri
# {'firstName': 'Bheri', 'lastName': 'Usha', 'employee_detais': [{'employee_id': 101, 'designation': 'Developer'}, {'state': 'Telengana', 'company': 'ABC'}]}