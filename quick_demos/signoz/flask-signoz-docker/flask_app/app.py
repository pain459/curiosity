from flask import Flask
import random
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

app = Flask(__name__)

# Set up tracing
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://otel-collector:4317"))
provider.add_span_processor(processor)

# Instrument the Flask app
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def index():
    return "Hello, SigNoz!"

@app.route("/random")
def random_number():
    num = random.randint(1, 100)
    if num > 90:
        raise Exception("Random number too high!")
    return f"Your random number is: {num}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
