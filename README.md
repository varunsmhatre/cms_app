# ContentManagementApp
Content Management App APIs where in users could create content, register, login, search content


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python [3.10.7]
- Install the project dependencies: 
```
pip install -r requirements.txt
```

### Installation
1. Clone the repository:

```
   git clone https://github.com/varunsmhatre/cms_app.git
```

2. Change to the project directory:

```
    cd your-django-app
```

3. Create and activate a virtual environment:

```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. To run the development server, use the following command:

```
    python manage.py runserver
```

Finally hit the url "http://127.0.0.1:8000/swagger/" in browser to view all the API Docs
APIs are not working from the Swagger UI, but they can be called from Postman
The Swagger UI helps for getting json body details for the request