## Requirements
- Flask (https://flask.palletsprojects.com/en/1.1.x/installation/)
- python-dotenv (https://pypi.org/project/python-dotenv/)
- JSON-server (https://github.com/typicode/json-server)
- ngrok (https://ngrok.com/download)
- Meraki Dashboard API (https://pypi.org/project/meraki/)

## Setup Google Cloud Vision API
- OCR guide (https://cloud.google.com/vision/docs/ocr)
- Python setup instruction (https://cloud.google.com/vision/docs/quickstart-client-libraries)

## Workflow
![Image of workflow](https://github.com/mfakbar/meraki-car-plate-detection/blob/main/workflow-diagram.jpg)

## Instructions
1. Clone the repository.
2. Setup and install all the requirements - optionally, use venv to isolate the project.
3. Complete the setup of Google Cloud Vision API.
4. In local repository folder, create a file named *.env* where we define environment variables. This .env file must contain:
   1. MV_SHARED_KEY = 'YOUR MERAKI SHARED SECRET KEY' > we set this up in Meraki webhook alert setting. We will touch on this in step 7.
   2. MV_API_KEY = 'YOUR MERAKI API KEY' > from Meraki profile setting.
   3. DB_HOST = 'JSON-SERVER LOCALHOST ADDRESS' > local address+port where the JSON-server is running (e.g., 'http://localhost:3000'). To find out what local address our machine use, we will touch on this in step 8.
   4. GOOGLE_APPLICATION_CREDENTIALS = 'GOOGLE SERVICE ACCOUNT JSON' > service account json file path. The file is generated when we setup the Google Vision API (e.g., 'service-account-file.json').
5. Run flask server > *python flask_server.py*
   1. Once completed, we should be able to see the localhost address+port where the Flask app is running (e.g. "Running on http://127.0.0.1:5000/")
6. Run ngrok server > *ngrok http 5000*
   1. This is based on which port the Flask server is running in step 5.1. In this example it's port 5000.
   2. Once completed, we should be able to see publicly available link that translates the localhost address in step 5.1 to a publicly available https link (e.g., https://XXXXXXXXXXXX.ngrok.io).
7. In Meraki dashboard > Alerts > Webhook setting, insert the ngrok link from step 6.2 as webhook endpoint, with */webhook* appended into the link (e.g., https://XXXXXXXXXXXX.ngrok.io/webhook).
   1. Choose a shared secret key and update the MV_SHARED_KEY in *.env* file with the correct one.
   2. Add this new webhook profile to the custom recipient for motion alerts.
8. Run JSON-server database > *json-server db_server.json*
   1. Once completed, we should be able to see the localhost address where the database server is running (e.g., 'http://localhost:3000'). Update the DB_HOST in *.env* file with this address.
9. Optionally, edit and/or use *user_input_dummy.py* to mimic json data from customer input, on a mobile app for example, that will be sent to the order database in JSON-server. Or use Postman for this.
10. Test if the Flask server is ready to receive a Meraki motion alert webhook, and trigger the plate detection process.