# Atiqul Islam Rahad Portfolio

Modern professional portfolio website for a Junior Backend Developer / Django Developer.

## Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT authentication with Simple JWT
- Swagger UI with drf-yasg
- Bootstrap 5
- HTML5, CSS3, JavaScript

## Features

- Full-screen responsive hero section
- Professional profile image placeholder
- Animated typing effect
- CTA buttons, social icons, and resume download
- About, education, objective, and experience sections
- Skills with progress bars
- Projects with Bootstrap cards and CRUD REST APIs
- Blogs with website display and CRUD REST APIs
- Contact form that stores messages in the database
- Resume PDF upload through Django admin and public download endpoint
- Customized Django admin for Projects, Blogs, Contacts, and Resume
- JWT login and registration APIs
- Swagger and ReDoc API documentation
- Dark mode toggle and smooth scrolling

## Project Structure

```text
portfolio/
├── accounts/
├── projects/
├── blogs/
├── contacts/
├── portfolio/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── projects.html
│   ├── blog.html
│   └── contact.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
├── requirements.txt
└── manage.py
```

## Local Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a `.env` file from `.env.example`.

```bash
copy .env.example .env
```

4. Create PostgreSQL database.

```sql
CREATE DATABASE portfolio_db;
```

5. Update `.env` with your PostgreSQL username, password, host, and port.

6. Run migrations.

```bash
python manage.py migrate
```

7. Create an admin user.

```bash
python manage.py createsuperuser
```

8. Run the development server.

```bash
python manage.py runserver
```

## Important URLs

- Website: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- Swagger: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## API Endpoints

### Authentication

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/token/refresh/`

### Projects

- `GET /api/projects/`
- `POST /api/projects/`
- `PUT /api/projects/<id>/`
- `DELETE /api/projects/<id>/`

Write operations require JWT authentication.

### Blogs

- `GET /api/blogs/`
- `POST /api/blogs/`
- `PUT /api/blogs/<id>/`
- `DELETE /api/blogs/<id>/`

Write operations require JWT authentication.

### Contact

- `POST /api/contact/`

## JWT Usage

Login with:

```json
{
  "username": "admin",
  "password": "your-password"
}
```

Use the returned access token in protected API requests:

```text
Authorization: Bearer your_access_token
```

## Resume Upload

Upload a PDF resume from:

```text
/admin/projects/resume/
```

Keep one active resume. The public download button uses:

```text
/resume/download/
```

## Profile Image

The project includes a placeholder at:

```text
static/images/profile-placeholder.svg
```

Replace it with a real professional image and update the image path in `templates/home.html` if needed.

## Production Notes

- Set `DEBUG=False`
- Use a strong `SECRET_KEY`
- Set strict `ALLOWED_HOSTS`
- Configure a production PostgreSQL database
- Serve media files from object storage or a web server
- Run `python manage.py collectstatic`
- Use Gunicorn plus Nginx or a managed platform
