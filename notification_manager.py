from twilio.rest import Client

TWILIO_SID = "ACe618ac1601343b5ad994795ce121be75"
TWILIO_AUTH_TOKEN = "8ef4c9118f7c9b2f29c29170c5b06e8c"
TWILIO_VIRTUAL_NUMBER = "+18597109613"
TWILIO_VERIFIED_NUMBER = "+93706625153"


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