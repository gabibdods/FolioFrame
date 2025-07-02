# 🌍 FolioFrame — Personal Portfolio Website on a Live Production Django Server

A full-featured personal website for recruiters, collaborators, and visitors to view my portfolio, send me messages, and subscribe to my game development newsletter. Built using Django in **production mode**, integrated with Gunicorn and NGINX for performance, and enriched with HTML, CSS, JavaScript, and PHP for interactive frontend and dynamic backend behavior.

---

## 🔍 Problem Statement

I needed a professional, accessible, and public-facing website to showcase my work to recruiters and potential collaborators. The site needed to be secure, reliable, and production-ready — with a message-sending form and newsletter integration — and accessible via a real public domain URL.

---

## 🎯 Project Goals

- Host a **portfolio website** accessible from anywhere online
- Enable visitors to:
  - View project showcases
  - Learn about my professional background
  - Send direct messages to my email
  - Subscribe to my game's newsletter
- Practice deploying Django in **production mode**
- Resharpen skills in Django and explore PHP for backend versatility

---

## 🛠️ Technologies Used

### 🔧 Backend & Server
- **Django** — Python web framework used for routing and site structure
- **Python** — Used to configure Django settings, routes, and views
- **Gunicorn** — WSGI-compliant HTTP server for production use
- **NGINX** — Reverse proxy and static file server with high efficiency

### 💻 Frontend & Interactivity
- **HTML** — Basic page structure and content layout
- **CSS** — Styling, background imagery, and color schemes
- **JavaScript** — Animations and interactivity
- **PHP** — Handles dynamic form input processing (email and newsletter logic)

---

## 🧩 Design Decisions

- Used **Django + Python** to maintain consistency with earlier experience, and to improve production deployment skills
- Selected **Gunicorn + NGINX** as a robust, common stack for Django-based sites in production
- Integrated **PHP** for greater backend flexibility (form submissions, email routing, etc.)
- Focused on secure deployment best practices: HTTPS, firewall rules, and proper static file routing via NGINX

---

## 🖥️ Architecture Overview

```plaintext
        +------------------+
        |   Web Browser    |
        +--------+---------+
                 |
                 v
        +------------------+
        |     NGINX        |  <- serves static files & acts as reverse proxy
        +--------+---------+
                 |
                 v
        +------------------+
        |    Gunicorn      |  <- WSGI interface to Django
        +--------+---------+
                 |
                 v
        +------------------+
        |     Django       |
        |  + Python + PHP  |  <- backend logic, forms, routing
        +------------------+