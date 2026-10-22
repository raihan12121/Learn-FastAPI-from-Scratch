# 🚀 Learn FastAPI from Scratch - Course Management API

Welcome to my **FastAPI** learning repository! 👋

I started learning FastAPI from the ground up to master modern backend development in Python. In the process of learning, I designed and built this RESTful Course Management API project to put core backend concepts into practice — including database modeling, user authentication, security, authorization, pagination, and API testing.

---

## 🛠️ Technologies & Tools Used

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - High performance, easy to learn, fast to code Python web framework.
- **Server**: [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server implementation.
- **Database**: [PostgreSQL](https://www.postgresql.org/) - Relational database management system.
- **Database Management**: **pgAdmin 4** - Used for managing and inspecting the local PostgreSQL database server, tables, schemas, and queries.
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) - Object Relational Mapper for handling database models, queries, relationships, and foreign keys (`CASCADE` delete).
- **Data Validation & Settings**: [Pydantic v2](https://docs.pydantic.dev/) & `pydantic-settings` - Robust schema validation, response serialization, and environment variable management via `.env`.
- **Authentication & Security**:
  - **OAuth2 with Password Bearer**: Secure token-based authentication flow.
  - **JWT (JSON Web Tokens)**: `PyJWT` for issuing and validating access tokens.
  - **Password Hashing**: `pwdlib` with `Argon2` for secure one-way password hashing.
- **API Testing & Verification**:
  - **Postman**: Used extensively to test, debug, and verify all API endpoints, request payloads, headers, query parameters, authentication flows, and status codes.
  - **Interactive Swagger UI (`/docs`)**: Interactive OpenAPI documentation for quick exploration.

---

## ✨ Features Implemented

- 🔐 **User Authentication & Authorization**:
  - User registration (`POST /users/`) with email uniqueness check and password hashing.
  - User login (`POST /login`) via OAuth2 form returning a signed JWT access token.
  - Dependency-based protected routes (`get_current_user`) to guard endpoints.
- 📚 **Course Management (CRUD)**:
  - **Create**: Add new courses linked to the authenticated user (`creator_id`).
  - **Read**: Fetch individual courses or list all courses created by the user.
  - **Update**: Modify course details with ownership validation.
  - **Delete**: Remove courses with strict ownership checks (only creator can delete).
- 🔍 **Pagination & Filtering**:
  - Query parameters for pagination (`limit`, `skip`).
  - Search filter (`search`) using case-insensitive SQL matching.
- ⚙️ **Configuration Management**:
  - Fully environment-driven configuration via `.env` and `pydantic-settings`.
  - Secure defaults with sensitive keys excluded from version control via `.gitignore`.

---

## 📋 API Endpoints

### 🔑 Authentication
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/login` | Authenticate user and return JWT bearer token | ❌ |

### 👤 Users
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/users/` | Register a new user | ❌ |

### 📖 Courses
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/course/` | Create a new course | ✅ |
| `GET` | `/course/` | Get all courses (supports `limit`, `skip`, `search`) | ✅ |
| `GET` | `/course/{id}` | Get course by ID | ✅ |
| `PUT` | `/course/{id}` | Update course by ID (owner only) | ✅ |
| `DELETE` | `/course/{id}` | Delete course by ID (owner only) | ✅ |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- PostgreSQL installed and running locally
- pgAdmin (optional, for visual DB inspection)
- Postman (optional, for testing)

### 2. Clone the Repository
```bash
git clone https://github.com/raihan12121/Learn-FastAPI-from-Scratch.git
cd "Learn-FastAPI-from-Scratch"
```

### 3. Set Up Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy `.env.example` to create your `.env` file:
```bash
cp .env.example .env
```
Update the `.env` file with your PostgreSQL credentials:
```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_postgres_password
DATABASE_NAME=your_database_name
DATABASE_USERNAME=postgres
SECRET_KEY=your_generated_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 6. Create the Database in PostgreSQL / pgAdmin
Open pgAdmin or `psql` and create the database corresponding to `DATABASE_NAME` in your `.env`:
```sql
CREATE DATABASE "Raihan";
```
*Note: SQLAlchemy will automatically generate the required tables on the first startup.*

### 7. Run the Application
```bash
fastapi dev app/main.py
```
Or with Uvicorn:
```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation & Testing

Once the server is running, you can test and explore the API:
- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **Postman**: Import endpoints and test the full registration ➔ login ➔ token bearer flow.

---

## 👤 Author

- **Muhammad Raihan Molla** - [GitHub Profile](https://github.com/raihan12121)
