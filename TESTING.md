# Test Examples

### Test Policy Acceptance

Request:

```
{
    "customer_income": 2500,
    "customer_debt": 600,
    "payment_remarks": 0,
    "payment_remarks_12m": 0,
    "customer_age": 18
}
```

Response:

```
{"message":"ACCEPT"}
```

### Test Policy Rejection: Low Income

Request:

```
{
    "customer_income": 400,
    "customer_debt": 500,
    "payment_remarks": 1,
    "payment_remarks_12m": 0,
    "customer_age": 25
}
```

Response:

```
{"message":"REJECT","reason":"LOW_INCOME"}
```

### Test Policy Rejection: High Debt

Request:

```
{
    "customer_income": 1200,
    "customer_debt": 800,
    "payment_remarks": 0,
    "payment_remarks_12m": 0,
    "customer_age": 35
}
```

Response:

```
{"message": "REJECT","reason": "HIGH_DEBT"}
```

### Test Policy Rejection: Payment Remarks

Request:

```
{
    "customer_income": 1500,
    "customer_debt": 700,
    "payment_remarks": 2,
    "payment_remarks_12m": 0,
    "customer_age": 30
}
```

Response:

```
{"message":"REJECT","reason":"PAYMENT_REMARKS"}
```

### Test Policy Rejection: Payment Remarks 12M

Request:

```
{
    "customer_income": 1800,
    "customer_debt": 900,
    "payment_remarks": 0,
    "payment_remarks_12m": 2,
    "customer_age": 40
}
```

Response:

```
{"message":"REJECT","reason":"PAYMENT_REMARKS_12M"}
```

### Test Policy Rejection: Underage

Request:

```
{
    "customer_income": 1200,
    "customer_debt": 500,
    "payment_remarks": 0,
    "payment_remarks_12m": 0,
    "customer_age": 17
}
```

Response:

```
{"message":"REJECT","reason":"UNDERAGE"}
```

### Test Invalid Value

Request:

```
{
    "customer_income": 1000,
    "customer_debt": 500,
    "payment_remarks": "invalid",
    "payment_remarks_12m": 0,
    "customer_age": 25
}
```

Response:

```
{"error":"INVALID_PAYMENT_REMARKS"}
```

### Test Missing Key:

Request:

```
{
    "customer_income": 1500,
    "payment_remarks": 0,
    "payment_remarks_12m": 0,
    "customer_age": 30
}
```

Response:

```
{"error":"MISSING_CUSTOMER_DEBT"}
```

### Test Unsupported Media Type

Request:

Sent a curl call without specifying the Content-Type HTTP header

```
curl -X POST -H -d 'data' http://127.0.0.1:5000/api/v1/policy_check
```

Response:

```
{"error":"UNSUPPORTED_MEDIA_TYPE"}
```

### Test Invalid JSON

Request:

```
curl -X POST -H 'Content-Type: application/json' -d 'data' http://127.0.0.1:5000/api/v1/policy_check
```

Response:

```
{"error":"INVALID_JSON"}
```
