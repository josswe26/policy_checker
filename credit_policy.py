from flask import jsonify


class CreditPolicy:
    """Base class for Policy classes"""

    def validate(self, data, key, data_type):
        """Validate the data being passed to the API"""

        if key not in data:
            return jsonify({"error": f"MISSING_{key.upper()}"})

        if not isinstance(data[key], data_type):
            return jsonify({"error": f"INVALID_{key.upper()}"})

        return None

    def check(self, data):
        """Make sure method is implemented in child classes"""
        raise NotImplementedError


class IncomeCheck(CreditPolicy):
    """Policy to check the customer income"""

    def check(self, data):
        """Return a rejection message if the income is below the limit"""
        if income_validation_error := self.validate(data, "customer_income", int):
            return income_validation_error

        if data["customer_income"] < 500:
            return jsonify({"message": "REJECT", "reason": "LOW_INCOME"})
        return None


class DebtCheck(CreditPolicy):
    """Policy to check the customer debt"""

    def check(self, data):
        """Return a rejection message if the debt is above the limit"""
        if debt_validation_error := self.validate(data, "customer_debt", int):
            return debt_validation_error

        if data["customer_debt"] > 1000:
            return jsonify({"message": "REJECT", "reason": "HIGH_DEBT"})
        return None


class PaymentRemarksCheck(CreditPolicy):
    """Policy to check the customer payment remarks"""

    def check(self, data):
        """Return a rejection message if the payment remarks are above the limit"""
        if remarks_validation_error := self.validate(data, "payment_remarks", int):
            return remarks_validation_error

        if remarks_12m_validation_error := self.validate(
            data, "payment_remarks_12m", int
        ):
            return remarks_12m_validation_error

        if data["payment_remarks_12m"] > 0:
            return jsonify({"message": "REJECT", "reason": "PAYMENT_REMARKS_12M"})
        if data["payment_remarks"] > 1:
            return jsonify({"message": "REJECT", "reason": "PAYMENT_REMARKS"})
        return None


class AgeCheck(CreditPolicy):
    """Policy to check the customer age"""

    def check(self, data):
        """Return a rejection message if the age is below the limit"""
        if age_validation_error := self.validate(data, "customer_age", int):
            return age_validation_error

        if data["customer_age"] < 18:
            return jsonify({"message": "REJECT", "reason": "UNDERAGE"})
        return None
