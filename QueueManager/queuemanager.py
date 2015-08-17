from flask import Flask
from flask import Response
import datetime
import json

app = Flask(__name__)


@app.route("/read/")
def readFromQueue():
    # 1: Receive the POST Request from an internal micro service
    # --> Log incoming message
    # --> Grab Component Name
    # --> Grab Queue Name

    # 2: Inspect the URL
    # --> Lookup Queue Name
    # --> If not found then return error message body with error status code 404

    # 3: Read in Priority and Time Stamp
    # More research is needed with this step as to how redis handles priorities and FIFO conditions.
    # An idea is to have a priority and timestamp column in redis you can sort and process by.
    # For now we will read in a message from redis and worry about the "first msg" priority later

    # 4: Read Message from Queue
    # --> Retrieve last Message from designated queue
    # --> Get JSON Content from Message
    # --> Get Queue Message ID
    # --> Get Priority
    # --> Get TimeStamp
    # --> Get Component Name
    # --> Get Queue Name
    # --> Package the Queue Message ID, Priority, TimeStamp, Component Name, Queue Name with the Message Body

    msgID = 1
    data = {
        'version': '0.1',
        'requestGUID': '1828291jdju1',
        'profileId': '1893291',
        'request': {'subject': 'vpc', 'verb': 'create'},
        'service': {'name': 'RequestIntakeManager', 'ipAddress': '127.0.0.1', 'timestamp': datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}
    }




    #9: Respond with retrieved JSON and Message ID
    res = Response(json.dumps(data), status=200, mimetype='application/json')
    res.headers["API-KEY"] = "lkajeflkajelfkjlj2lejlr"
    return res


@app.route("/write/")
def writeToQueue():
    # 1: Receive the POST Request from an internal micro service
    # --> Log incoming message
    # --> Grab Message Body
    # --> Translate External JSON in Message Body to python object
    # --> Parse the Message Body
    # --> Grab Component Name
    # --> Grab Queue Name
    # --> Grab Priority Level

    data = {
        'version': '0.1',
        'requestGUID': '1828291jdju1',
        'profileId': '1893291',
        'request': {'subject': 'vpc', 'verb': 'create'},
        'service': {'name': 'RequestIntakeManager', 'ipAddress': '127.0.0.1', 'priority': 'high', 'timestamp': datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}
    }

    # 2: Inspect the URL
    # --> Lookup Queue Name
    # --> If not found then return error message body with error status code 404

    # 3: Generate Queue Message ID
    # --> Create Queue Message ID from Priority level and TimeStamp
    # --> Error out if Priority level or Timestamp is not available in JSON message. Return error message body with error status code 404.

    # 4: Create Redis Message
    # --> Create a Redis Message from the JSON and the Queue Message ID

    # 5: Write Redis Message to Queue
    # --> Write to queue
    # --> If queue write failed then return error message body with error status code 404

    # 6: Respond with status 200
    res = Response(json.dumps(data), status=200, mimetype='application/json')
    res.headers["API-KEY"] = "lkajeflkajelfkjlj2lejlr"
    return res

@app.route("/delete/")
def deleteFromQueue():
    # 1: Receive the POST Request from an internal micro service
    # --> Log incoming message
    # --> Grab Component Name
    # --> Grab Queue Name
    # --> Grab Message ID

    data = "Delete Successful!"

    # 2: Inspect the URL
    # --> Lookup Queue Name
    # --> If not found then return error message body with error status code 404

    # 3: Delete Message
    # --> Remove the Message from Redis identified by the message id
    # --> Throw error if message id does not exist and return error message body with error status code 404

    # 4: Respond with status 200
    res = Response(json.dumps(data), status=200, mimetype='application/json')
    res.headers["API-KEY"] = "lkajeflkajelfkjlj2lejlr"
    return res

if __name__ == "__main__":
    # Run App
    app.run()
