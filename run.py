from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'ACb9817596a7a3dee337f4d96ee423f85f'
auth_token = '3a6bfeb337dc3c3b2342ff2e08e1c6f1'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a message
message = client.messages.create(
    body="Hello from Twilio!",
    from_='+15736724768',  # Twilio-issued number
    to='+254741882520'      # Your mobile number
)

print(f"Message sent with SID: {message.sid}")
