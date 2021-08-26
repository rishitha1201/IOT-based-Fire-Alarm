from boltiot import Sms, Bolt
import json, time

SSID = 'YOUR SSID' 
AUTH_TOKEN = 'YOUR TWILIO AUTH TOKEN' 
FROM_NUMBER = 'YOUR TWILIO NUMBER'
TO_NUMBER = 'YOUR PHONE NUMBER'
API_KEY = 'YOUR BOLT IOT API KEY'
DEVICE_ID = 'YOUR BOLT DEVICE ID'


mybolt = Bolt(API_KEY,DEVICE_ID)
sms = Sms(SSID,AUTH_TOKEN,TO_NUMBER,FROM_NUMBER)

while True: 
    print ("Reading sensor value")
    response = mybolt.digitalRead('1') 
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value =  int(data['value'])
        if sensor_value==0:
            mybolt.digitalWrite("3","HIGH")
            mybolt.digitalWrite("4","HIGH")
            time.sleep(5)
            mybolt.digitalWrite("3","LOW")
            mybolt.digitalWrite("4","LOW")
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("Emergency! Flame detected in the room")
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)
