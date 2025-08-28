# 🌐 Django Course Site – Meetups App

Welcome to Django Course Site, a web application built with Django 3.2 🎯.
It’s a simple but complete project that lets users explore meetups, view details, and register for events.

<br> 
✨ Features

 * 🗂 Meetups Management: Create, update, and list meetups.

 * 🏢 Locations: Store meetup venue name and address.

 * 👥 Participants: Register for meetups using just an email.

 * 📅 Details View: Each meetup has title, description, image, organizer email, and location.

 * 📧 Email-based Registration: Users sign up with email, automatically stored in DB.

 * 🎨 Responsive UI: Styled with custom CSS.

 * 🔑 Admin Panel: Full CRUD for Meetups, Locations, and Participants.

<br> 
🛠 Tech Stack

 * ⚡ Backend: Django 3.2 (Python)

 * 🗄 Database: SQLite (default, can be swapped)

 * 🎨 Frontend: Django templates + CSS

 * 🛠 Admin: Django Admin for content management

<br> 
⚙️ Installation & Setup

1. Clone the repository

        git clone https://github.com/your-username/django_course_site.git
        cd django_course_site


2. Create and activate virtual environment

        python -m venv venv
        source venv/bin/activate   # Linux/Mac
        venv\Scripts\activate      # Windows


3. Apply migrations


        python manage.py migrate


4. Run the development server

        python manage.py runserver


5. Open 👉 http://127.0.0.1:8000/meetups/ in your browser.

<br> 
▶️ Usage

 * 🌍 Go to /meetups/ → See all meetups.

 * 🔍 Click a meetup → details page with location, description, and registration form.

 * 📝 Enter your email → Register as a participant.

 * ✅ Redirected to confirmation page.

 * 🔑 Visit /admin/ → Manage meetups, locations, participants.

<br> 
🖼 Screenshots

* All Meetups Page
<img width="933" height="893" alt="Screenshot 2025-08-28 163249" src="https://github.com/user-attachments/assets/ea3caa0c-b857-45cf-820f-79c874d8cfd1" />

* Meetup Details Page
<img width="937" height="889" alt="Screenshot 2025-08-28 163347" src="https://github.com/user-attachments/assets/7e7a7760-c216-409c-a6c3-577f1e4c3132" />

* Registration Form
<img width="562" height="206" alt="Screenshot 2025-08-28 163409" src="https://github.com/user-attachments/assets/79f66f2b-fb0c-4775-b293-b905d19f4f7c" />

* Registration Success Page
<img width="952" height="776" alt="Screenshot 2025-08-28 163442" src="https://github.com/user-attachments/assets/07b696a5-c824-4854-a5dd-c639d2e6a276" />


