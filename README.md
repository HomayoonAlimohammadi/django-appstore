# Django Appstore Project

This project is a sample Django application for an Appstore service. It demonstrates essential functionality such as user signup/login, app creation with admin verification, REST API endpoints, API documentation, unit testing, and Docker containerization. Additionally, it includes a design document for a Dashboard service to aggregate and display statistics from the Appstore.

## Project Structure

```
.
├── django_appstore_project
|   ├── Dockerfile.py
|   ├── docker-compose.yml
|   ├── requirements.txt
│   ├── manage.py
│   └── django_appstore_project
│       └── ...
├── appstore
│   └── ...
├── docs
|   └── ...
└── README.md
```

## Setup Instructions

### Running Locally Without Docker

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**

    ```bash
    source venv/bin/activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r django_appstore_project/requirements.txt
    ```

4. **Run Migrations:**

   ```bash
   cd django_appstore_project
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional, for Admin Access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**

   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Running with Docker

1. **Run Docker containers:**

   ```bash
   docker compose up --build 
   ```

3. **Run Migrations:**

   In a new terminal, execute:

   ```bash
   docker exec -it django-appstore-container python manage.py migrate
   ```

4. **Create a Superuser (Optional):**

   ```bash
   docker exec -it django-appstore-container python manage.py createsuperuser
   ```

5. **Access the Application:**

   Open your browser and navigate to [http://localhost:8000](http://localhost:8000).

## API Documentation

API documentation is generated using **drf-yasg**. You can access the interactive documentation at:

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Running Tests

To run the tests, execute:

```bash
python manage.py test
```

Or, if you're running within Docker:

```bash
docker exec -it django-appstore-container python manage.py test
```

## Dashboard Design

See the [dashboard_design.md](./dashboard_design.md) file for a detailed description of the proposed Dashboard service design, including data transfer, data aggregation, and scalability considerations.

## Assumptions and Limitations

- The project implements only the essential functionality as per the test requirements.
- Endpoints for signup, login, and purchase are currently mocked and return placeholder responses.
- The Dashboard service is documented in detail but not implemented.
- Production-level considerations (e.g., enhanced security, performance optimizations) are beyond the scope of this demonstration.

## Known Issues

- Currently, there are no known issues. Please report any bugs or suggestions.
