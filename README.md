# KPA API  – Bhavesh Motghare

This is a backend assignment for the **KPA API** challenge. The project demonstrates the implementation of two selected APIs from the provided Swagger documentation using **FastAPI** and **PostgreSQL**.

## 🚀 Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.11
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Testing Tool**: Postman
- **Environment Management**: dotenv

---

## 📌 Implemented APIs

Based on the Swagger docs: [https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0)

### ✅ 1. Create Form Data  
- **Endpoint**: `POST /api/formData`
- **Function**: Adds new form data entry.
- **Fields**: `full_name`, `phone`, `address`
- **Response**: JSON with newly created entry.

### ✅ 2. Get All Form Data  
- **Endpoint**: `GET /api/formData`
- **Function**: Fetches all submitted form entries.
- **Response**: JSON list of form entries.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/bhavesh/kpa_api_assignment.git
cd kpa_api_assignment

### 2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

---
### 3. Install Requirements

pip install -r requirements.txt

### 4. Set Up PostgreSQL
Create a PostgreSQL database named kpa_db.

Update the .env file at the root level with your credentials:

DATABASE_URL=postgresql://username:password@localhost:5432/kpa_db

### 5. Run the Server
uvicorn app.main:app --reload

---
Open your browser at: http://127.0.0.1:8000/docs


### ✨ Key Features Implemented
✅ POST /api/formData
Create and store form submission data with fields: full_name, phone, address.

✅ GET /api/formData
Retrieve all stored form entries.

🔁 Modular FastAPI structure with routing, models, schemas, and DB config split cleanly.

🔐 Input validation using Pydantic.

⚙️ Environment-based config using .env and python-dotenv.

📜 Auto-generated Swagger docs at /docs.

⚠️ Limitations & Assumptions
❌ No authentication or login system is implemented.

❌ No pagination or filtering on the GET endpoint (basic list fetch).

✅ Assumes phone field is unique for each form submission.

🧪 Manual testing only (no automated test suite provided).

🔒 Data validation includes required fields and types but not advanced logic.
