from flask import jsonify


class PolicyManager:
    """Class responsible for managing policies"""

    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        """Add policy to the list of policies"""
        self.policies.append(policy)

    def check_all_policies(self, data):
        """Check if data is accepted by all policies"""
        for policy in self.policies:
            response = policy.check(data)
            if response:
                return response
        return jsonify({"message": "ACCEPT"})
