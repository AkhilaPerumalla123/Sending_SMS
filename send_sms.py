from twilio.rest import Client
		
def send_sms(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = '***********************'
    auth_token = '***********************'

    client = Client(twilio_sid, auth_token)

    message = client.messages \
    .create(
         from_= '+1111111111',
         body = 'Hey you got a message!!!!',
         to = '+1111111111'
     )

    print(message.sid)
		
send_sms()

