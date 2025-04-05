This guide walks you through setting up and running the project on your local machine.

---

### 1 Clone the Repository

```
(bash)
git clone https://github.com/Hyrysake/IPL_2
cd IPL_2
```

---

### 2 Create a .env File

```
APP_ENV=development

POSTGRES_DB=your_postgres_db
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_PORT=5432

SQLALCHEMY_DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${POSTGRES_PORT}/${POSTGRES_DB}

SECRET_KEY=your_secret_key
ALGORITHM=HS256

MAIL_USERNAME=your_mail_username
MAIL_PASSWORD=your_mail_password
MAIL_FROM=your_mail_from
MAIL_PORT=your_mail_port
MAIL_SERVER=your_mail_server

REDIS_HOST=localhost
REDIS_PORT=6379

CLD_NAME=your_cloudinary_name
CLD_API_KEY=your_cloudinary_api_key
CLD_API_SECRET=your_cloudinary_api_secret
```

### 3 Install Tesseract-OCR (System Dependency)

```
Linux (bash):
sudo apt update
sudo apt install tesseract-ocr

MacOS (bash):
brew install tesseract

Windows:
Download from: https://github.com/tesseract-ocr/tesseract
Add the installation path (e.g., C:\Program Files\Tesseract-OCR) ///
to your system's PATH environment variable.
```

### 4 Install Project Dependencies

```
(bash)
poetry install
poetry shell
```

### 5 Start Docker

```
(bash)
sudo docker compose up -d
```

### 6 Run Database Migrations

```
(bash)
alembic upgrade head
```

### 7 Launch the Application

```
(bash)
uvicorn main:app --reload
```

### 9 Access the API

```
http://127.0.0.1:8000/
```



