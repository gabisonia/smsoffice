import urllib.parse
import urllib.request

class SmsOfficeClient:
    def __init__(self, key):
        self.key = key
        self.base_url = 'http://smsoffice.ge/api/'

    def show_balance(self):
        with urllib.request.urlopen(self.base_url + 'getBalance?key=' + self.key) as response:
             print(response.read().decode('utf-8'))
    
    def send_message(self, destination, sender, content):
        values = { 'key' : self.key,
                  'destination' : destination,
                  'sender' : sender ,
                  'content' : content + '\n NO 91146' }
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(self.base_url + 'send.aspx', data)
        with urllib.request.urlopen(req) as response:
           print(response.read().decode('utf-8'))


