import json

def read_json_files(path_to_file): 
    with open(path_to_file, encoding="UTF-8") as p: 
        data = json.load(p) 
        p.close()
    return reversed(data['conversation'])


if __name__ == '__main__':
    sender = ""
    tmp = ""
    data = read_json_files("./Freemy17.json")
    print(type(data))
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
        date = created_at.split('T')[0]
        time = created_at.split('T')[1]
        string = str(sender) + " " + str(date) + " " + str(time) + " " + str(text)
        print(string)
        # print(sender, date, time, text)

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