import logging
from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Set up logging
LOG_FILE = "/var/log/app.log"  # Path inside the container
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # For debugging (optional)
    ]
)

# Database setup
DATABASE = "/db/analytics.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            api_call TEXT NOT NULL,
            status_code INTEGER NOT NULL
        )
        ''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/math/<operation>', methods=['GET'])
def math_operations(operation):
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    if num1 is None or num2 is None:
        response = {"error": "Both num1 and num2 must be provided"}
        status_code = 400
    else:
        try:
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    raise ValueError("Division by zero")
                result = num1 / num2
            else:
                raise ValueError("Invalid operation")

            response = {"operation": operation, "result": result}
            status_code = 200
        except ValueError as e:
            response = {"error": str(e)}
            status_code = 400

    # Log request details
    logging.info(f"API Call: {operation}, Status Code: {status_code}, Result: {response}")

    # Log to database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO analytics (date, api_call, status_code)
        VALUES (?, ?, ?)
        ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), operation, status_code))
        conn.commit()

    return jsonify(response), status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
