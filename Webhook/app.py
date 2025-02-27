from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

@app.route('/trigger-call', methods=['GET', 'POST'])
def trigger_call():
    account_sid = '<acc-sid>'
    auth_token = '<acc-auth>'
    client = Client(AC6716340bb8cb65e8db8e61a94bb17a1c, 5deb30089e3d3339768cde347c47f48f)

    # List of numbers to call
    numbers_to_call = ['<number>', '<number>']
    call_sids = []  # To store Call SIDs

    for number in numbers_to_call:
        call = client.calls.create(
                            twim='<Response><Say>"change Alert message here"</Say></Response>',
                            to=number,
                            from_='<twilio-number>'
                        )
        call_sids.append(call.sid)

    # Joining all the Call SIDs to return in response
    call_sids_str = ', 'join(call_sids)
    return f"Call initiated with SIDs: {call_sids_str}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
