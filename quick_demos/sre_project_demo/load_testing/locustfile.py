from locust import HttpUser, task, between

class FlaskAppUser(HttpUser):
    # Simulate a user with a wait time between tasks
    wait_time = between(1, 3)

    # Define the host URL for the Flask app (Docker network name)
    host = "http://flask-app:5000"

    @task
    def add_operation(self):
        # Example: Testing addition endpoint
        self.client.get("/math/add?num1=10&num2=5")

    @task
    def multiply_operation(self):
        # Example: Testing multiplication endpoint
        self.client.get("/math/multiply?num1=7&num2=3")

    @task
    def divide_by_zero(self):
        # Example: Testing divide by zero error
        self.client.get("/math/divide?num1=10&num2=0")
