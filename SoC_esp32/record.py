import ujson
from variables import RECORD_PATH

def writer(file):
    def write_row(row):
        line = ','.join(str(item) for item in row) + '\n'
        file.write(line)
    return write_row

def reader(file):
    def read_rows():
        lines = file.readlines()
        return [line.strip().split(',') for line in lines]
    return read_rows

def csv_to_json():
    data_to_convert = []
    headers = ['time', 'temperature', 'humidity']
    with open(RECORD_PATH, 'r') as f:
        lines = f.readlines()
        for line in lines:
            values = line.strip().split(',')
            row = {headers[i]: values[i] for i in range(len(headers))}
            data_to_convert.append(row)
    return ujson.dumps(data_to_convert)