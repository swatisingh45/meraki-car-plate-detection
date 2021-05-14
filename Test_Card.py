from WebEx_Bot_Notification import *
from flask import Flask, request, Response

## Sample Data
snapResponse = [{'url': "https://www.webex.com/content/dam/wbx/us/images/hp/webexone/10x.png"}]
searchOrder = ['Ham Sandwhich']
detectedPlate = ['123-VWE']


app = Flask(__name__)


@app.route("/webhooks", methods=["POST"])
def webhook_received():
    webhook = Webhook(request.json)
    print(request.json)
    respond_to_button_press(webhook)

    return Response(status=200)
    

if __name__ == "__main__":
    send_detected_notification(snapResponse, searchOrder, detectedPlate)
    app.run()
    

