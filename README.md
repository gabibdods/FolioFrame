# 🌍 FolioFrame — Personal Portfolio Website on a Live Production Django Server

A full-featured personal website for recruiters, collaborators, and visitors to view my portfolio, explore my experience and send me messages. Built using Django in **production mode**, integrated with **Gunicorn** and **NGINX** for performance, and enriched with **HTML**, **CSS**, and **JavaScript** for interactive frontend and dynamic backend behavior. A CI/CD pipeline connects my work environment to the web server using **GitLab Runner** and SSH, leveraging **Ansible** for tasks like database migration, static/media file collection, and package updates. Updates appear in minutes on the live public URL via **Cloudflare Tunnels**, a safer alternative to traditional port forwarding.

---

## 🔍 Problem Statement

I needed a professional, accessible, and public-facing website to showcase my work to recruiters and potential collaborators. The site needed to be secure, reliable, and production-ready — with a message-sending form — and accessible via a real public domain URL.

---

## 🎯 Project Goals

- Host a **portfolio website** accessible from anywhere online
- Enable visitors to:
  - View project showcases
  - Learn about my professional background
  - Send direct messages to my email
  - Subscribe to my game's newsletter
- Practice deploying Django in **production mode**
- Implement strong **anti-bot and anti-spam** protection for all public forms

---

## 🛡️ Anti-Bot & Security Measures

To protect the site from automated attacks, spam, and abuse, I implemented multiple layers of bot protection:

- ✅ **Google reCAPTCHA v3** — integrated into contact and newsletter forms to block automated submissions
- ✅ **Django Ratelimit** — throttles repeated form requests to prevent brute-force abuse
- ✅ **Custom Django Middleware** — user-agent filtering, and suspicious pattern detection
- ✅ **Honeypot Traps** — invisible form fields to trap bots that fill all inputs blindly
- 🧪 **More security features to come**, including IP-based lockouts, behavioral analysis, and spam signature detection

These measures help keep contact forms, newsletter subscriptions, and login routes clean, responsive, and resilient under traffic.

---

## 🛠️ Technologies Used

### 🔧 Backend & Server
- **Django** — Python web framework used for routing and site structure
- **Python** — Used to configure Django settings, routes, views, and logic
- **Gunicorn** — WSGI-compliant HTTP server for production use
- **NGINX** — Reverse proxy and static file server with high efficiency

### 💻 Frontend & Interactivity
- **HTML** — Core structure of the website
- **CSS** — Visual design and responsiveness
- **JavaScript** — Interactive frontend behavior
- **Google reCAPTCHA** — Integrated in key input forms

---

## 🧩 Design Decisions

- Used **Django + Python** to leverage previous experience and take advantage of Django’s form system and security features
- Chose **Gunicorn + NGINX** for production deployment due to their proven performance and reliability
- Emphasized security, with **Cloudflare ZeroTrust** and strong form validation
- Prioritized **user input safety**, **anti-bot protection**, and **web hardening** through middleware and IP control

---

## 🖥️ Architecture Overview

```plaintext
        +------------------+
        |  Web Environment |
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
        |   Cloudflare     |  <- Safer alternative to port forwarding
        +--------+---------+
                 |
                 v
        +----------------------------+
        |      Django (Python)       |
        |                            |
        | - Routing & Views          |
        | - reCAPTCHA Validation     |
        | - Honeypot & Middleware    |
        | - Rate Limiting Logic      |
        +----------------------------+
