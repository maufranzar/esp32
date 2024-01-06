import os
from record import reader, writer
from variables import RECORD_PATH, RECORD_NAME

def init_csv():
    if RECORD_NAME in os.listdir("/sd/"):
        return "a"
    else:
        with open(RECORD_PATH, "w") as f:
            csv_writer = writer(f)
            csv_writer(["time", "temperature", "humidity"])
        return "w"
    
    
def last_row():
    with open(RECORD_PATH, "r") as f:
        read_rows = reader(f)
        rows = read_rows()
        last_line = rows[-1] if rows else None
    return last_line
    

def data(time:int, temp:int, hum:int):
    last_line = last_row()
    if last_line is not None:
        if last_line == [str(time), str(temp), str(hum)]:
            return True
    return False