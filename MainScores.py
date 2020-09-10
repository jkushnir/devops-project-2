#!/usr/bin/env python3

from flask import Flask
import Utils

app = Flask(__name__)

#function to respond to GET methods, try to get score from Scores file referenced in Utils. If successful, display the score, if not, show the relevant exception message prefixed with error message specified in Utils.
@app.route('/')
def score_server():
    try:
        score = open(Utils.SCORES_FILE_NAME, "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.ERROR_MESSAGE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""


# initiate the webserver
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8777)
