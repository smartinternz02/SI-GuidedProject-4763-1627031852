import wiotp.sdk.device
import datetime
import time

import pyqrcode
import cv2
myConfig = {
    "identity": {
        "orgId": "g3kuc1",
        "typeId": "vitap",
        "deviceId":"7011"
    },
    "auth": {
        "token": "vitap123"
    }
}

def myCommandCallback (cmd):
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient (config=myConfig, logHandlers=None)
client.connect()
i=0
p=[]
n=[]
c=input("Enter in to add stock else enter out --> ")
while True:
 s=cv2.imread(input("Input file to be scanned: "))
 d=cv2.QRCodeDetector()
 data, bbox, straight_qrcode = d.detectAndDecode(s)
 r=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
 if c=='in': 
  if(p.count(data)>=1):
     n[p.index(data)]=n[p.index(data)]+1
     i=i+1
  if(p.count(data)==0):
     p.append(data)
     n.append(1)
     i=i+1
  if bbox is not None:
    myData={"stock_in": data,'stock_total': i,'products':p ,'quantity':n, 'date_time':r }
    client.publishEvent (eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print ("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
 else :
  if(p.count(data)>=1):
     i=i-1
     n[p.index(data)]=n[p.index(data)]-1
  if bbox is not None:
   myData={'stock_out\n': data, 'stock_total': i, 'products':r ,'quantity':n ,'date_time':r}
   client.publishEvent (eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
   print ("Published data Successfully: %s", myData)
   client.commandCallback = myCommandCallback
 c=input("Enter in to add stock else enter out --> ")

client.disconnect()
