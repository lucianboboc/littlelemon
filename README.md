## Steps to run the app

### 1. Open the cloned project folder, setup a `virtual environment` and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Replace the `.env` file in the root folder with your db details

```bash
# .env
DB_NAME     = YOUR_DB_NAME
DB_HOST     = localhost
DB_PORT     = 3306
DB_USER     = YOUR_DB_USER
DB_PASSWORD = YOUR_DB_PASSWORD
```

### 4. Make migrations

```bash
python3 manage.py makemigrations
```

### 5. Migrate

```bash
python3 manage.py migrate
```

### 6. Run the app

```bash
python3 manage.py runserver
```

### To run tests

```bash
python3 manage.py test tests
```
