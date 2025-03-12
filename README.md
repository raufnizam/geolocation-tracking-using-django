# Geolocation Tracking App

A Django-based web application that allows users to register, log in, and save their geographical location securely.

## Features
- **User Authentication**: Register, Login, and Logout functionality.
- **Location Saving**: Users can save their latitude and longitude via JSON requests.
- **Tailwind CSS Integration**: For responsive and modern UI design.
- **Error Handling**: Provides meaningful feedback for issues like invalid JSON data.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/geolocation-app.git
cd geolocation-app
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

## Usage
- Visit `http://127.0.0.1:8000/` to access the home page.
- Register a new user or log in with an existing account.
- After logging in, users can navigate to `/save-location/` and submit valid JSON data (latitude and longitude) to save their location.

## JSON Data Format for Saving Location
When sending a POST request to `/save-location/`, use the following JSON structure:
```json
{
    "latitude": "24.8607",
    "longitude": "67.0011"
}
```

## Important URLs
- **Home:** `/`
- **Login:** `/accounts/login/`
- **Logout:** `/accounts/logout/`
- **Register:** `/accounts/register/`
- **Save Location (POST request required):** `/save-location/`

## Folder Structure
```
.
├── templates
│   ├── base.html
│   ├── index.html
│   └── registration
│       ├── login.html
│       └── register.html
├── views.py
├── urls.py
├── models.py
├── settings.py
├── manage.py
```


## Contributing
Feel free to submit issues or pull requests for improvements and bug fixes.

## License
This project is open-source and available under the [MIT License](LICENSE).

