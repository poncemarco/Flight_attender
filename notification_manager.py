from twilio.rest import Client

TWILIO_SID = "ACfd29b672d9cc0de2320979fd76db73a9"
TWILIO_AUTH_TOKEN = "fdf2202581d9fd9d2be64d047c9646d6"
TWILIO_VIRTUAL_NUMBER = "+19402896137"
TWILIO_VERIFIED_NUMBER = "+525546476943"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
