from flask import Flask, jsonify
import logging
from logging.handlers import RotatingFileHandler
import time

app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('flask_app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)

# Create a logging format with timestamp
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)  # Set the logger level to INFO

@app.route('/hello')
def hello():
    app.logger.info("Hello World endpoint was reached")
    return jsonify(message="Hello World!")

if __name__ == '__main__':
    app.logger.info('Starting Flask app')
    try:
        # Run the app on port 3000
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        app.logger.info('Flask app was stopped with Ctrl+C')
        raise
    except Exception as e:
        app.logger.error('An error occurred: %s', e)
    finally:
        app.logger.info('Flask app has stopped')