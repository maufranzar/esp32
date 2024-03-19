import urequests
import ujson


def writer(file):
    def write_row(row):
        line = ','.join(str(item) for item in row) + '\n'
        file.write(line)
    return write_row


def reader(file):
    lines = file.readlines()
    return [line.strip().split(',') for line in lines]


def to_json(data):
    json_data = ujson.dumps({
        "time": data[0],
        "temperature": data[1],
        "humidity": data[2],
        "light": data[3],
        "distance": data[4]
    })
    return json_data

def sent_json(json_data):
    headers = {'Content-Type': 'application/json'}
    response = urequests.post(
        'http://192.168.0.12:8000/data/',
        data=json_data,
        headers=headers)
    print(response.text)
    return response