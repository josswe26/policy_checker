from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from policy_manager import PolicyManager
from credit_policy import IncomeCheck, DebtCheck, PaymentRemarksCheck, AgeCheck

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
        return jsonify({"error": "INVALID_JSON"})

    policy_manager = PolicyManager()

    policy_manager.add_policy(IncomeCheck())
    policy_manager.add_policy(DebtCheck())
    policy_manager.add_policy(PaymentRemarksCheck())
    policy_manager.add_policy(AgeCheck())

    return policy_manager.check_all_policies(data)


if __name__ == "__main__":
    app.run(debug=True)
