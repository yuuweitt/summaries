import json
from datetime import datetime
import calendar
import pytz

def read_json_files(path_to_file): 
    with open(path_to_file, encoding="UTF-8") as p: 
        data = json.load(p) 
        p.close()
    return reversed(data['conversation'])


def time_zone(date, time):
    tw = pytz.timezone('Asia/Taipei')
    dt = date + " " + time
    utc_time = datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
    
    # Return the local date and time corresponding to the POSIX timestamp
    utc_ts = calendar.timegm(utc_time.utctimetuple())
    local_time = datetime.fromtimestamp(utc_ts).replace(microsecond=utc_time.microsecond)

    return local_time


if __name__ == '__main__':
    sender = ""
    tmp = ""
    data = read_json_files("./Test.json")
    # for item in data['conversation']:
    for item in data:
        tmp = sender
        sender = item['sender']
        if(sender != tmp):
            print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - ")
            tmp = sender
        try:
            text = item['text']
        except:
            text = item['media']
        created_at = item['created_at'].split('.')[0]
        local_time = time_zone(created_at.split('T')[0], created_at.split('T')[1])
        message = str(sender) + " " + str(local_time) + " " + str(text)
        print(message)


# print(data2['sender'])
# json_str = json.dumps(data)
# data2 = json.loads(json_str)
# print(data2)
# print(type(data2))

# def read_file(path):
#     with open(path, 'r', encoding="UTF-8") as f:
#         data =  f.read()
#     return data

# if __name__ == '__main__':
#     data = read_file("Test.json")
#     print(data)