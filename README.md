# Movie Recommendation App

This is a Django-based web application that recommends movies to users based on collaborative filtering techniques. The application allows users to log in, view movies, and receive personalized movie recommendations.

## Features

- User authentication (login/logout)
- Movie listing by genre
- Display of the most rated movies
- Personalized movie recommendations based on user ratings
- Admin interface for managing movies and ratings

## Project Structure

```
movie-recommendation-app/
├── movie_recommendation/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── recommendations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── recommendations/
│           ├── index.html
│           ├── login.html
│           ├── movie_list.html
│           ├── recommendations.html
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd movie-recommendation-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the application.
- Users can log in to view personalized movie recommendations and explore the movie database.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.