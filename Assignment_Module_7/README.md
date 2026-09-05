# My Personal Portfolio (Django)

A simple personal portfolio website built with **Django**, **HTML**, and **CSS**.
This was built as a beginner project to practice the core Django flow:
**Model → View → URL → Template → Admin**.

## Description

This site has a homepage introducing me, an About page, a Projects page that
pulls project data from the database, individual project detail pages, and a
Django Admin panel to manage all the projects (add / edit / delete) without
touching the code.

## Features

- **Home page** – name, profile picture, short intro, skills list, navbar
- **About page** – a bit more about me and what I'm learning
- **Projects page** – shows all projects as cards, pulled live from the database
- **Project detail page** – full info for a single project (`/projects/<id>/`)
- **Django Admin** – add, edit, and delete projects from `/admin/`
- **GitHub button** – each project links out to its GitHub repo
- **Project images** – optional image upload per project (with a placeholder if none is set)
- **Contact section** – simple contact info on the home page
- Custom CSS: navbar, project cards, buttons, footer, and a responsive layout for mobile

## Technologies Used

- Python 3
- Django 6.1
- SQLite (default Django database)
- HTML5 & CSS3
- Pillow (for handling uploaded project images)

## Project Structure

```
portfolio_project/
├── myportfolio/        # Django project settings & main urls.py
├── portfolio/           # The app: models.py, views.py, urls.py, admin.py
├── templates/portfolio/ # HTML templates (base, home, about, projects, detail)
├── static/               # CSS and images
├── media/                # Uploaded project images (created automatically)
├── manage.py
├── requirements.txt
└── README.md
```

## Installation / Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (sets up the database)
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create an admin account** (so you can log into `/admin/`)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open your browser:
   - Website: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

8. Log into `/admin/` with the superuser you created, and add a few projects.
   They'll automatically show up on the Projects page.

## Before You Run It Yourself

- Replace `static/images/profile.jpg` with your own photo.
- Update your name, intro text, and skills in `templates/portfolio/home.html`.
- Update the About page text in `templates/portfolio/about.html`.
- Update the social links in `templates/portfolio/base.html` (footer) and
  `templates/portfolio/home.html` (contact section).

## Screenshots

*(Add your own screenshots here after running the project locally, e.g.)*

| Home Page | Projects Page | Project Detail |
|-----------|----------------|-----------------|
| ![Home](screenshots/home.png) | ![Projects](screenshots/projects.png) | ![Detail](screenshots/detail.png) |

## What I Learned

Building this project helped me understand how Django connects everything
together: a **Model** defines the data, a **View** fetches and prepares it,
a **URL** routes a request to the right view, and a **Template** displays
the final HTML — with the **Admin** panel letting me manage data without
writing any extra code.

## Author

Your Name — feel free to connect with me on [GitHub](https://github.com/yourusername).
