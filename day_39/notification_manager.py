#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
TWILIO_SID = 'ACeecbfacc5d11ecd74802889f5557d576'
TWILIO_AUTH_TOKEN = "18cc5ca512054d46d69e4735c69811fd"


class NotificationManager:
    def __init__(self, messasge):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        for date in flight_date:
            self.message = self.client.messages.create(
                from_='+15417033646',
                to='+821088987615',
                body=messasge
            )