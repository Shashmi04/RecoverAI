# ============================================================
# RecoverAI - Prediction Engine
# ============================================================

# Import pandas
# Used to create the input DataFrame
import pandas as pd

# Import joblib
# Used to load our saved ML model
import joblib

# Import os
# Used to create the correct model file path
import os


# ------------------------------------------------------------
# LOAD THE TRAINED MODEL
# ------------------------------------------------------------

# Find the RecoverAI project folder
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Create the path to our saved model
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "gradient_boosting_pipeline.pkl"
)

# Load the trained Gradient Boosting pipeline
model = joblib.load(MODEL_PATH)


# ------------------------------------------------------------
# RECOVER PAYMENT FUNCTION
# ------------------------------------------------------------

def recover_payment(
    amount,
    payment_method,
    failure_reason,
    checkout_time_seconds,
    previous_transactions,
    previous_successes,
    previous_failures,
    customer_lifetime_value,
    previous_success_rate
):

    # Create a DataFrame containing the new transaction
    transaction = pd.DataFrame({
        "amount": [amount],
        "payment_method": [payment_method],
        "failure_reason": [failure_reason],
        "checkout_time_seconds": [checkout_time_seconds],
        "previous_transactions": [previous_transactions],
        "previous_successes": [previous_successes],
        "previous_failures": [previous_failures],
        "customer_lifetime_value": [customer_lifetime_value],
        "previous_success_rate": [previous_success_rate]
    })


    # --------------------------------------------------------
    # PREDICT RECOVERY PROBABILITY
    # --------------------------------------------------------

    # Get probability of successful recovery
    recovery_probability = model.predict_proba(
        transaction
    )[0, 1]


    # --------------------------------------------------------
    # ASSIGN PRIORITY
    # --------------------------------------------------------

    if recovery_probability >= 0.70:

        priority = "High"

    elif recovery_probability >= 0.40:

        priority = "Medium"

    else:

        priority = "Low"


    # --------------------------------------------------------
    # RECOMMEND RECOVERY ACTION
    # --------------------------------------------------------

    if failure_reason == "Checkout Abandoned":

        if recovery_probability >= 0.70:
            recommended_action = (
                "Send Urgent Checkout Reminder"
            )
        else:
            recommended_action = (
                "Send Checkout Reminder"
            )

    elif failure_reason == "Card Declined":

        recommended_action = (
            "Suggest Alternative Payment Method"
        )

    elif failure_reason == "Insufficient Balance":

        recommended_action = (
            "Send Payment Reminder"
        )

    elif failure_reason in [
        "Network Error",
        "Bank Timeout",
        "Technical Error"
    ]:

        if recovery_probability >= 0.70:
            recommended_action = "Retry Payment"
        else:
            recommended_action = "Retry After Delay"

    else:

        recommended_action = "Retry After Delay"


    # --------------------------------------------------------
    # ESTIMATE RECOVERY VALUE
    # --------------------------------------------------------

    estimated_recovery_value = (
        amount * recovery_probability
    )


    # --------------------------------------------------------
    # RETURN RESULTS
    # --------------------------------------------------------

    return {
        "recovery_probability": round(
            recovery_probability * 100,
            2
        ),

        "recovery_priority": priority,

        "recommended_action": recommended_action,

        "estimated_recovery_value": round(
            estimated_recovery_value,
            2
        )
    }