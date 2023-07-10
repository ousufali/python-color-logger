from flask import Blueprint
from utils.page import html_content, home_html_content
from utils.custom_logger import getLogger
logger = getLogger()
logger_blueprint = Blueprint('logger', __name__, url_prefix='/logger')
import os


@logger_blueprint.route('/')
def index():
    
    logger.critical(f"SECRET_MESSAGE:  {os.getenv('SECRET_MESSAGE')}")
    return home_html_content


@logger_blueprint.route('/debug', methods=['GET', 'POST'])
def debug():
    logger.debug('This is a debug-level message')

    return html_content.format(color="white")

@logger_blueprint.route('/info', methods=['GET', 'POST'])
def info():
    logger.info('This is an info-level message')

    return html_content.format(color="blue")

@logger_blueprint.route('/warning', methods=['GET', 'POST'])
def warning():
    logger.warning('This is a warning-level message,This is a warning-level message,This is a warning-level message,This is a warning-level message,This is a warning-level message')

    return html_content.format(color="yellow")

@logger_blueprint.route('/error', methods=['GET', 'POST'])
def error():
    logger.error('This is an error-level message')
    return html_content.format(color="red")
