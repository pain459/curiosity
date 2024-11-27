from flask import Flask
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home endpoint was hit.")
    return "Welcome to the Monitoring and Alerting System!"

@app.route("/error")
def error():
    app.logger.error("An error occurred!")
    return "Simulated error occurred.", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
