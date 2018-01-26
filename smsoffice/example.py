import smsofficeclient

key = 'your-key'

client = smsofficeclient.SmsOfficeClient(key)

client.send_message('597933199','yyy ','test')
client.show_balance()