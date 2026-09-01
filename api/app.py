from flask import Flask, request, jsonify, send_from_directory
from src.predict import recover_payment
import os

app = Flask(__name__)

# Path to the dashboard folder
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DASHBOARD_DIR = os.path.join(
    BASE_DIR,
    "dashboard"
)


# ------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------

@app.route("/")
def dashboard():

    return send_from_directory(
        DASHBOARD_DIR,
        "index.html"
    )


# ------------------------------------------------------------
# PREDICTION API
# ------------------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    result = recover_payment(
        amount=data["amount"],
        payment_method=data["payment_method"],
        failure_reason=data["failure_reason"],
        checkout_time_seconds=data["checkout_time_seconds"],
        previous_transactions=data["previous_transactions"],
        previous_successes=data["previous_successes"],
        previous_failures=data["previous_failures"],
        customer_lifetime_value=data["customer_lifetime_value"],
        previous_success_rate=data["previous_success_rate"]
    )

    return jsonify(result)


# ------------------------------------------------------------
# START SERVER
# ------------------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )