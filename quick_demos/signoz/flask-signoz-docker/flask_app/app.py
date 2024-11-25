import logging
import random
from flask import Flask, request, jsonify
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.trace import get_current_span

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# OpenTelemetry setup
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317"))
provider.add_span_processor(processor)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def index():
    # Get current trace information
    span = get_current_span()
    trace_id = span.get_span_context().trace_id
    logger.info(f"Trace sent: Trace ID: {trace_id:#x}, Endpoint: /, Response Code: 200")
    return "Hello, SigNoz!"

@app.route("/random")
def random_number():
    span = get_current_span()
    trace_id = span.get_span_context().trace_id

    try:
        num = random.randint(1, 100)
        if num > 90:
            raise Exception("Random number too high!")
        response = jsonify({"random_number": num})
        response.status_code = 200
        logger.info(f"Trace sent: Trace ID: {trace_id:#x}, Endpoint: /random, Response Code: 200")
        return response
    except Exception as e:
        logger.error(f"Trace sent: Trace ID: {trace_id:#x}, Endpoint: /random, Response Code: 500, Error: {str(e)}")
        response = jsonify({"error": str(e)})
        response.status_code = 500
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
