"""Module responsible for managing policies"""
import logging
from flask import jsonify


logger = logging.getLogger(__name__)


class PolicyManager:
    """Class responsible for managing policies"""

    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        """Add policy to the list of policies"""
        logger.info("Adding policy %s", policy.__class__.__name__)
        self.policies.append(policy)

    def check_all_policies(self, data):
        """Check if data is accepted by all policies"""
        for policy in self.policies:
            logger.info("Checking policy: %s", policy.__class__.__name__)
            response = policy.check(data)
            if response:
                return response
        logger.info("All policies passed")
        return jsonify({"message": "ACCEPT"})
