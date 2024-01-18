"""Test check policy endpoint."""
from flask import json
from ..main import app


def test_index_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_check_policy_accept():
    client = app.test_client()
    data = {
        "customer_income": 2000,
        "customer_debt": 500,
        "payment_remarks": 1,
        "payment_remarks_12m": 0,
        "customer_age": 22,
    }

    response = client.post("/api/v1/policy_check", json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "ACCEPT"}


def test_check_policy_reject_low_income():
    client = app.test_client()
    data = {
        "customer_income": 400,
        "customer_debt": 500,
        "payment_remarks": 1,
        "payment_remarks_12m": 0,
        "customer_age": 25,
    }

    response = client.post("/api/v1/policy_check", json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "REJECT", "reason": "LOW_INCOME"}


def test_check_policy_reject_high_debt():
    client = app.test_client()
    data = {
        "customer_income": 1000,
        "customer_debt": 1500,
        "payment_remarks": 0,
        "payment_remarks_12m": 1,
        "customer_age": 25,
    }

    response = client.post("/api/v1/policy_check", json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "REJECT", "reason": "HIGH_DEBT"}


def test_check_policy_reject_payment_remarks():
    client = app.test_client()
    data = {
        "customer_income": 1000,
        "customer_debt": 500,
        "payment_remarks": 2,
        "payment_remarks_12m": 0,
        "customer_age": 25,
    }

    response = client.post("/api/v1/policy_check", json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "message": "REJECT",
        "reason": "PAYMENT_REMARKS",
    }


def test_check_policy_reject_payment_remarks_12m():
    client = app.test_client()
    data = {
        "customer_income": 1000,
        "customer_debt": 500,
        "payment_remarks": 0,
        "payment_remarks_12m": 1,
        "customer_age": 25,
    }

    response = client.post("/api/v1/policy_check", json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "message": "REJECT",
        "reason": "PAYMENT_REMARKS_12M",
    }


def test_check_policy_reject_underage():
    client = app.test_client()
    data = {
        "customer_income": 1000,
        "customer_debt": 500,
        "payment_remarks": 0,
        "payment_remarks_12m": 0,
        "customer_age": 17,
    }

    response = client.post("/api/v1/policy_check", json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "message": "REJECT",
        "reason": "UNDERAGE",
    }


def test_invalid_value():
    client = app.test_client()
    data = {
        "customer_income": 1000,
        "customer_debt": 500,
        "payment_remarks": "0",
        "payment_remarks_12m": 0,
        "customer_age": 17,
    }

    response = client.post("/api/v1/policy_check", json=data)
    assert response.status_code == 400
    assert json.loads(response.data) == {
        "error": "INVALID_PAYMENT_REMARKS",
    }


def test_missing_key():
    client = app.test_client()
    data = {
        "customer_income": 1000,
        "customer_debt": 500,
        "payment_remarks": 0,
        "customer_age": 17,
    }

    response = client.post("/api/v1/policy_check", json=data)
    print(f"RESPONSE: {response.data}")
    assert response.status_code == 400
    assert json.loads(response.data) == {
        "error": "MISSING_PAYMENT_REMARKS_12M",
    }


def test_unsupported_media_type():
    client = app.test_client()

    response = client.post("/api/v1/policy_check", data="unsupported data")
    assert response.status_code == 415
    assert json.loads(response.data) == {
        "error": "UNSUPPORTED_MEDIA_TYPE",
    }


def test_invalid_json_error():
    client = app.test_client()
    response = client.post(
        "/api/v1/policy_check",
        data="invalid json",
        content_type="application/json",
    )
    assert response.status_code == 400
    assert json.loads(response.data) == {
        "error": "INVALID_JSON",
    }
