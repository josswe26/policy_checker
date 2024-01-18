"""Main module for the API"""
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, UnsupportedMediaType
from .policy_manager import PolicyManager
from .credit_policy import IncomeCheck, DebtCheck, PaymentRemarksCheck, AgeCheck

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def index():
    """Index page for the API"""
    return "Policy Checker API"


@app.route("/api/v1/policy_check", methods=["POST"])
def check_policy():
    """API endpoint to check the policies"""

    try:
        data = request.get_json()
    except BadRequest:
        logger.error("Invalid JSON received")
        return jsonify({"error": "INVALID_JSON"}), 400
    except UnsupportedMediaType:
        logger.error("Invalid Content-Type received")
        return jsonify({"error": "UNSUPPORTED_MEDIA_TYPE"}), 415
    except Exception as error:
        logger.error("Unknown error: %s", error)
        return jsonify({"error": "UNKNOWN_ERROR"}), 500

    logger.info("Request received successfully")
    logger.debug("Request data: %s", data)

    policy_manager = PolicyManager()

    policy_manager.add_policy(IncomeCheck())
    policy_manager.add_policy(DebtCheck())
    policy_manager.add_policy(PaymentRemarksCheck())
    policy_manager.add_policy(AgeCheck())

    return policy_manager.check_all_policies(data)


if __name__ == "__main__":
    app.run(debug=True)
