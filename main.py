import flask
import os
from utils.custom_logger import getLogger
from utils.page import home_html_content
from routes.logger import logger_blueprint

logger = getLogger()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(logger_blueprint)

@app.route('/', methods=['GET', 'POST'])
def home():
    return  home_html_content



if __name__ == "__main__":
    if (os.getenv("environment") == "production"):
        app.run( host="0.0.0.0", port=os.getenv("port") or 3000)
    else:
        print("enviornment variable not found.")
        app.run( host="0.0.0.0", port=os.getenv("port") or 3000, debug= True )

