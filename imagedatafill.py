import requests

def generatereq(str, parent):
    body = {'Folder':parent, 'PNG':str[6:31], 'Time':str[32:48]}
    requests.post('http://127.0.0.1:8000/imagedata/image/', data=body)
    return

def run():
    file = open('imageinput.txt', 'rt')
    parent = 'PNGs_Orbit12_outer'
    for row in file:
        print(row)
        # print(row)
        # print(row[6:31] + '*')
        # print(row[32:48] + '*')
        # print(row[49:53] + '*')
        generatereq(row, parent)
    return

if __name__ == '__main__':
    run()