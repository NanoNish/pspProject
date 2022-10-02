import requests
import csv

def run():
    file = open('mergedata/mergedata.csv')
    print('Loaded')
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
        body = {'Time':row[1], 'HelioDist':row[2], 'HGILat':row[3], 'HGILon':row[4],
                 'BR':row[5], 'BT':row[6], 'BN':row[7], 'B':row[8],
                 'VR':row[9], 'VT':row[10], 'VN':row[11], 'Speed':row[12],
                 'FlowEle':row[13], 'FlowAng':row[14], 'Density':row[15], 'Temp':row[16],
                 'isBNaN':row[17], 'isSpeedNaN':row[18]}
        requests.post('http://127.0.0.1:8000/mergedata/data/', data=body)
    return

if __name__ == '__main__':
    run()