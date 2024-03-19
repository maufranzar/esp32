import os
from variables import RECORD_PATH, RECORD_NAME
from record import reader, writer


def init_csv():
    if RECORD_NAME in os.listdir("/sd/"):
        return "a"
    else:
        with open(RECORD_PATH, "w") as f:
            csv_writer = writer(f)
            csv_writer(["time","temperature","humidity","light","distance"])
        return "w"
    
    
def last_row():
    with open(RECORD_PATH, "r") as f:
        read_rows = reader(f)
        last_line = None
        for row in read_rows:
            last_line = row
    return last_line
    

def data(time:int, temp:int, hum:int, light:float, distance:float):
    last_line = last_row()
    if last_line is not None:
        if last_line == [str(time),str(temp),str(hum),str(light),str(distance)]:
            return True
    return False
