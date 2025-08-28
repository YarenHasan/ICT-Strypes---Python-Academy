# 🌐 Django Course Site – Meetups App

Welcome to Django Course Site, a web application built with Django 3.2 🎯.
It’s a simple but complete project that lets users explore meetups, view details, and register for events.


✨ Features

 * 🗂 Meetups Management: Create, update, and list meetups.

 * 🏢 Locations: Store meetup venue name and address.

 * 👥 Participants: Register for meetups using just an email.

 * 📅 Details View: Each meetup has title, description, image, organizer email, and location.

 * 📧 Email-based Registration: Users sign up with email, automatically stored in DB.

 * 🎨 Responsive UI: Styled with custom CSS.

 * 🔑 Admin Panel: Full CRUD for Meetups, Locations, and Participants.


🛠 Tech Stack

 * ⚡ Backend: Django 3.2 (Python)

 * 🗄 Database: SQLite (default, can be swapped)

 * 🎨 Frontend: Django templates + CSS

 * 🛠 Admin: Django Admin for content management


⚙️ Installation & Setup

1. Clone the repository

        git clone https://github.com/your-username/django_course_site.git
        cd django_course_site


2. Create and activate virtual environment

        python -m venv venv
        source venv/bin/activate   # Linux/Mac
        venv\Scripts\activate      # Windows


3. Install dependencies

        pip install -r requirements.txt


4. Apply migrations


        python manage.py migrate


5. Run the development server

        python manage.py runserver


6. Open 👉 http://127.0.0.1:8000/meetups/ in your browser.


▶️ Usage

 * 🌍 Go to /meetups/ → See all meetups.

 * 🔍 Click a meetup → details page with location, description, and registration form.

 * 📝 Enter your email → Register as a participant.

 * ✅ Redirected to confirmation page.

 * 🔑 Visit /admin/ → Manage meetups, locations, participants.


🖼 Screenshots

📋 All Meetups Page

📄 Meetup Details Page

📝 Registration Form

✅ Registration Success Page
