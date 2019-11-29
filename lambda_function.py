import json
import logging
import os
from urllib2 import Request, urlopen, URLError, HTTPError

# Read all the environment variables
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
DSSC_URL = "https://" + os.environ['DSSC_URL']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # Read message posted on SNS Topic
    print(event)
    flag = False
    if 'body' in event:
        jsonBody = json.loads(event['body'])
    else:
        jsonBody = event

    message = jsonBody['scan']['findings']['vulnerabilities']
    # logger.info("Message: " + str(message))
    notification_output = "I have found "

    # detect vulnerability and render dynamic message output in slack
    if 'high' in message['total']:
        notification_output += str(message['total']['high']) + " high vulnerabilities, "
        flag = True
    if 'medium' in message['total']:
        notification_output += str(message['total']['medium']) + " medium vulnerabilities, "
        flag = True
    if 'low' in message['total']:
        notification_output += str(message['total']['low']) + " Low vulnerabilities "
        flag = True
    if 'unknown' in message['total']:
        notification_output += ", " + str(message['total']['unknown']) + " unknown vulnerabilities "
        flag = True
    if 'negligible' in message['total']:
        notification_output += ", " + str(message['total']['negligible']) + " negligible vulnerabilities "
        flag = True
    if 'defcon1' in message['total']:
        notification_output += ", " + str(message['total']['defcon1']) + " Critical vulnerabilities that requires your immidiate attention to fix. "
        flag = True
    if not flag:
        notification_output += " no vulnerabilities. "

    # Detect malware and render dynamic message output in slack
    if 'malware' in jsonBody['scan']['findings']:
        if int(jsonBody['scan']['findings']['malware']) > 0:
            notification_output += str(jsonBody['scan']['findings']['malware']) + " potential malicious payload "
            flag = True

    # Detect secrets stored in scanned image and render text message output
    if 'contents' in jsonBody['scan']['findings']:
        if 'high' in jsonBody['scan']['findings']['contents']['total']:
            notification_output += str(
                jsonBody['scan']['findings']['contents']['total']['high']) + " high risk content or secrets "
            flag = True
    # Identify PCI-DSS, HIPPA, and NIST compliance violations
    if 'checklists' in jsonBody['scan']['findings']:
        total_violation = 0
        if 'high' in jsonBody['scan']['findings']['checklists']['total']:
            total_violation += int(jsonBody['scan']['findings']['checklists']['total']['high'])

        if 'medium' in jsonBody['scan']['findings']['checklists']['total']:
            total_violation += int(jsonBody['scan']['findings']['checklists']['total']['medium'])

        if 'low' in jsonBody['scan']['findings']['checklists']['total']:
            total_violation += int(jsonBody['scan']['findings']['checklists']['total']['low'])

        if total_violation != 0:
            flag = True
            notification_output += "and, " + str(
                total_violation) + " total compliance checklist violations in PCI-DSS, HIPPA, and NIST"

    scan_ui_path = DSSC_URL + str(jsonBody['scan']['href']).replace('/api/', '/')
    notification_output += " in " + str(
        jsonBody['scan']['name']) + " image scan. For more details log in to DSSC console by visiting " + scan_ui_path
    if flag:
        # Construct a new slack message
        slack_message = {
            'channel': SLACK_CHANNEL,
            'text': "%s" % (notification_output),
            "icon_url": "https://aws-code-bucket-tejas.s3.us-east-2.amazonaws.com/Picture1.png"
        }
        # Post message on SLACK_WEBHOOK_URL

        req = Request(SLACK_WEBHOOK_URL, json.dumps(slack_message))
        try:
            response = urlopen(req)
            response.read()
            logger.info("Message posted to %s", slack_message['channel'])
        except HTTPError as e:
            logger.error("Request failed: %d %s", e.code, e.reason)
        except URLError as e:
            logger.error("Server connection failed: %s", e.reason)
