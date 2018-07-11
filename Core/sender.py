import paho.mqtt.client as mqtt
import time




class Sender:

    def Conect(self,cName):
        client = cName
        try:
            self.client = mqtt.Client()
            self.client.username_pw_set("incmrvjk","EUVFYnYcv0Qv")
            self.client.connect("m14.cloudmqtt.com", 11652, 60)
            print("Conected")
        except:
            print("error")


    def send(self,cName,topic,data):
        client = cName
        self.client.publish(topic, data)
        print("Sended")


    def disconnect(self,cName):
        client = cName
        self.client.disconnect()
        print("end")
