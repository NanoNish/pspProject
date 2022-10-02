from mergedata.models import Data
import csv

def run():
    with open('mergedata/mergedata.csv') as file:
        reader = csv.reader(file)
        next(reader)
        Data.objects.all().delete()
        for row in reader:
            print(row)
            # print(row[0]," ",row[-1]," ",row[1])
            # print(type(row[2]))
            data = Data(Time=row[1],HelioDist=row[2], HGILat=row[3], HGILon=row[4], 
             BR=row[5], BT=row[6], BN=row[7], B=row[8], 
             VR=row[9], VT=row[10], VN=row[11], Speed=row[12], 
             FlowEle=row[13], FlowAng=row[14], Density=row[15], Temp=row[16], 
             isBNaN=row[17], isSpeedNaN=row[18])
            data.save() 
            break

if __name__ == '__main__':
    run()