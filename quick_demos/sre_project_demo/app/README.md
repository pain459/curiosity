Here are some sample API calls for the Flask app. These requests use HTTP methods and parameters to interact with the application.

### Base URL
Assuming the app is running locally on port `5000`, the base URL is:

```
http://localhost:5000
```

---

### 1. **Addition**
**Endpoint:**
```
GET /math/add
```

**Example Request:**
```bash
curl "http://localhost:5000/math/add?num1=5&num2=3"
```

**Response:**
```json
{
    "operation": "add",
    "result": 8
}
```

---

### 2. **Subtraction**
**Endpoint:**
```
GET /math/subtract
```

**Example Request:**
```bash
curl "http://localhost:5000/math/subtract?num1=10&num2=4"
```

**Response:**
```json
{
    "operation": "subtract",
    "result": 6
}
```

---

### 3. **Multiplication**
**Endpoint:**
```
GET /math/multiply
```

**Example Request:**
```bash
curl "http://localhost:5000/math/multiply?num1=7&num2=6"
```

**Response:**
```json
{
    "operation": "multiply",
    "result": 42
}
```

---

### 4. **Division**
**Endpoint:**
```
GET /math/divide
```

**Example Request:**
```bash
curl "http://localhost:5000/math/divide?num1=15&num2=3"
```

**Response:**
```json
{
    "operation": "divide",
    "result": 5.0
}
```

---

### 5. **Division by Zero (Error Handling)**
**Endpoint:**
```
GET /math/divide
```

**Example Request:**
```bash
curl "http://localhost:5000/math/divide?num1=15&num2=0"
```

**Response:**
```json
{
    "error": "Division by zero"
}
```

---

### 6. **Invalid Operation**
**Endpoint:**
```
GET /math/modulus
```

**Example Request:**
```bash
curl "http://localhost:5000/math/modulus?num1=10&num2=3"
```

**Response:**
```json
{
    "error": "Invalid operation"
}
```

---

### 7. **Missing Parameters**
**Endpoint:**
```
GET /math/add
```

**Example Request:**
```bash
curl "http://localhost:5000/math/add?num1=10"
```

**Response:**
```json
{
    "error": "Both num1 and num2 must be provided"
}
```

---

These examples demonstrate how the API can handle various use cases, including valid calculations, error handling for invalid operations, and missing parameters. Let me know if you'd like to add more endpoints or features!