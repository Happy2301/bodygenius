
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def base_route():
    student_id = "S23-02-LastNameFirstName"
    return jsonify({"200616452": "Harpreet Singh"})

@app.route('/webhook', methods=['POST'])
def webhook_route():
    req = request.get_json()
    fulfillment_text = generate_fulfillment_text(req)
    return jsonify({"fulfillmentText": fulfillment_text})

def generate_fulfillment_text(req):
    intent = req['queryResult']['intent']['displayName']

    if intent == 'Default Welcome Intent':
        fulfillment_text = "Welcome to the chatbot! How can I assist you today? Here are the available options:\n\n1. Intent 1: [Description of intent 1]\n\n2. Intent 2: [Description of intent 2]\n\n3. Intent 3: [Description of intent 3]"
    elif intent == 'Intent 1':
        fulfillment_text = "This is the response for Intent 1."
    elif intent == 'Intent 2':
        fulfillment_text = "This is the response for Intent 2."
    elif intent == 'Intent 3':
        fulfillment_text = "This is the response for Intent 3."
    elif intent == 'Fulfillment Intent':
        fulfillment_text = "This is the fulfillment response."
    else:
        fulfillment_text = "I'm sorry, I couldn't understand your request. Please try again."

    return fulfillment_text

if __name__ == '__main__':
    app.run()