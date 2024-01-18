# Policy Checker

## Desing Overview

### Components

#### Flask App: `main.py`
* This is the main entry point for the application.
* Initialized the web server and defines the route for the API endpoint.

#### Policy Manager: `policy_manager.py`
* Manage the list of credit policies to be applied.
* Responsible for checking that the data provided complies with all policies.

#### Credit Policies: `credit_policy.py`
* Host the credit policies to be passed to the Policy Manager.
* Each credit policy defines a set of rules to check compliance.
* Allow to easily accomodate additional credit policies.

### Application Flow

#### Client Request
* The client make the HTTP request to the defined API endpoint.

#### API Endpoint
* Listen for incoming HTTP requests.
* Parse JSON data fron the request.

#### Policy Manager
* Add the credit polices to the list.
* Iterate through the credit policies to check if the data compiles with each policy.

#### Credit Policies
* Validate the incoming data.
* Check if the data complies with each policy based on predefined rules.
* Return a JSON response with the appropiate rejection message and reason.

#### API Endpoint (response)
* Return a response to the client based on the results of the policy check.