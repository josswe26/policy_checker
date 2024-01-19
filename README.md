# Policy Checker

## Design Overview

### Components

#### Flask App: `main.py`

- This is the main entry point for the application.
- Initialized the web server and defines the route for the API endpoint.

#### Policy Manager: `policy_manager.py`

- Manage the list of credit policies to be applied.
- Responsible for checking that the data provided complies with all policies.

#### Credit Policies: `credit_policy.py`

- Host the credit policies to be passed to the Policy Manager.
- Each credit policy defines a set of rules to check compliance.
- Allow to easily accomodate additional credit policies.

### Application Flow

#### Client Request

- The client make the HTTP request to the defined API endpoint.

#### API Endpoint

- Listen for incoming HTTP requests.
- Parse JSON data fron the request.

#### Policy Manager

- Add the credit polices to the list.
- Iterate through the credit policies to check if the data compiles with each policy.

#### Credit Policies

- Validate the incoming data.
- Check if the data complies with each policy based on predefined rules.
- Return a JSON response with the appropriate rejection message and reason.

#### API Endpoint (response)

- Return a response to the client based on the results of the policy check.

## Set Up the Service

### Clone the Repository

1. Clone the project on your local machine.

```
git clone https://github.com/josswe26/policy_checker.git
cd policy_checker
```

### Build and Run the Service with Docker

1. Build the Docker image.

```
docker build -t policy_checker .
```

2. Run the Docker container.

```
docker run -p 5000:5000 -d policy_checker
```

3. The API Endpoint is now ready to receive requests at `http://127.0.0.1:5000/api/v1/policy_check`

### Set Up a Local Development Environment (Optional)

1. Create and activate a virtual environment.

```
python -m venv venv
```

On macOS/Linux:

```
source venv/bin/activate
```

On Windows:

```
.\venv\Scripts\activate
```

2. Install dependencies.

```
pip install -r requirements.txt
```

3. Run the application locally

```
python main.py
```

## Additional Considerations

### Structure

- Follow a modular structure, with clear separation of concerns.
- Implement good practices, including exception handling and meaningful variables and function names, to ensure code readability.

### Scalability

- Consider the scalability of the service, especially if additional credit policies are planned for the future.

### Error Handling and Logging

- Handle HTTP-related errors during the request.
- Validation errors are being handled to return return an appropriate JSON response with the error message.
- Logs are used to record errors and provide insights for debugging.

### Testing

- Utilize pytest to systematically conduct tests, covering a range of scenarios, including acceptance, rejection, error cases, and handling of invalid data.
- Conducted manual testing to verify the expected behavior of the API. Find examples of the requests sent to the API [here](https://github.com/josswe26/policy_checker/blob/main/TESTING.md).

### Future Implementations

#### API Authentication

- Implement API authentication to ensure that only authorized clients can access the API.

#### Front End Interface

- Add a front end interface to be able to interact with the Policy Checker API.
