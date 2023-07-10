import flask
import os
from utils.custom_logger import getLogger

logger = getLogger()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
html_content = '''
<body     style="background-color: gray;">
    <div style="text-align: center;">
        <h1 style="color: {color};"> Colored Logger Application ( info/warning/debug/error )</h1>
        <p style="color: {color};">Hello, how you doing I'm Yousuf the owner of this fucking collored logger application.
        </p>
    </div>
</body>
'''
home_html_content = '''
<body
    style="background-color: gray;">
    <div style="text-align: center;">
        '<p style="font-size: 180px; color: pink;">Chala Ja bsdk</p>'
    </div>
</body>
'''

@app.route('/debug', methods=['GET', 'POST'])
def debug():
    logger.debug('This is a debug-level message')

    return html_content.format(color="white")

@app.route('/info', methods=['GET', 'POST'])
def info():
    logger.info('This is an info-level message')

    return html_content.format(color="blue")

@app.route('/warning', methods=['GET', 'POST'])
def warning():
    logger.warning('This is a warning-level message,This is a warning-level message,This is a warning-level message,This is a warning-level message,This is a warning-level message')

    return html_content.format(color="yellow")

@app.route('/error', methods=['GET', 'POST'])
def error():
    logger.error('This is an error-level message')
    return html_content.format(color="red")


@app.route('/', methods=['GET', 'POST'])
def home():
    return  home_html_content


if __name__ == "__main__":
    if (os.getenv("environment") == "production"):
        app.run( host="0.0.0.0", port=os.getenv("port") or 3000)
    else:
        print("enviornment variable not found.")
        app.run( host="0.0.0.0", port=os.getenv("port") or 3000, debug= True )

