from twilio.rest import Client
from flask import Flask, request, redirect
from twilio import twiml
import MapsApi
def sendText(classes_today):
    # Your Account SID from twilio.com/console
    account_sid = "AC##############################"
    # Your Auth Token from twilio.com/console
    auth_token  = "################################"

    client = Client(account_sid, auth_token)
    # Enter your phone number in the 'to' and enter the twilio number in the 'from_', Leave the body as is.
    message = client.messages.create(
    to="+###########",
    from_="+###########",
    body=("Welcome to One The Go Directions!\nTo get started enter your current location seperating each entity with a space and then followed"+
    "by a dot then your destination with spaces seperating each entity\nFor Example: New York Kats Deli.Toronto Pearson Airport".structuredMessage())
    )
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = twiml.Response()

    # Determine the right reply for this message
    body.strip()
    body.split(".")
    directions = MapsApi(body[0],body[1])

    resp.message()
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)
