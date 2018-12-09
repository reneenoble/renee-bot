from flask import Flask, request, session

import requests
import json

import assistant

app = Flask(__name__)

def send_message(text, event_type, channel):
  '''Send a message of a particular type to a slack channel.'''
  if text:
    json_response = {'type': event_type, 'text': text, 'channel': channel}
    headers = {
      # For simplicity I've just pasted in my access token here
      # but this would be a good place to teach about environment variables!
      'Authorization': 'Bearer xoxb-452146303616-498536714417-bA8rJpa2IndhM2SPxES5lXKx',
      'Content-Type': 'application/json',
    }
    requests.post('https://slack.com/api/chat.postMessage', data=json.dumps(json_response), headers=headers)

@app.route('/slack/bot', methods=['GET', 'POST'])
def slack_bot():
  '''The slack bot function handles messages sent to the chatbot and the slack bot verification process.'''
  # This global state is kinda gross, but simplifies teachingp
  # could eventually be replace by a database of some kind
  global state, data 

  # Slack Bot verification
  if request.json['type'] == 'url_verification':
    return request.json['challenge'] 

  # Respond to an event 
  else:
    event_type = request.json['event']['type']
    channel = request.json['event']['channel']

    def read_message():
      '''The message from the user.'''
      return request.json['event']['text']

    def reply(text):
      '''A reply is just a message back to the channel that messaged us.'''
      return send_message(text, event_type, channel)
    
    # Change the conversation state based on the message from the event
    state, data = assistant.on_input(state, data, output=reply, get_input=read_message)
    # Do something based on the new state
    assistant.on_enter(state, data, output=reply)

    return ''

if __name__ == '__main__':
  state = 'START'
  data = None

  app.run()
