class CHECKER:

    def __init__(self):
        self.Devices =  {

                "room1":'0',
                "room2":'0',
                "living-room":'0',
                "bathroom":'0',
                "kitchen":'0',
                #"room1":'0',

        }

    def checkStatus(self, device):
        if self.Devices[device] == '0':
            return 0
        elif self.Devices[device] == '1':
            return 1


    def toggleStatus(self, device):
        if self.Devices[device] == '0':
            self.Devices[device] = '1'
        elif self.Devices[device] == '1':
            self.Devices[device] = '0'


    def isOn(self,device):
        if self.Devices[device] == '1':
            return True
        else:
            return False




A = CHECKER()

print(A.checkStatus('room2'))
A.toggleStatus('room2')
A.toggleStatus('kitchen')
print(A.checkStatus('room2'))
print(A.Devices)
print(A.isOn('bathroom'))
print(A.isOn('kitchen'))
