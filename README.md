# FolioFrame

# Personal Portfolio Website on a Live Production Django Server

### Description

- A full-stack portfolio website designed to present professional projects, accept contact messages, and promote ongoing work.
- Built with Django in production mode, deployed via Gunicorn and NGINX, and supported by CI/CD automation using GitLab Runner and Ansible.
- Cloudflare Tunnel enables secure, global access via public domain without traditional port forwarding.

---

## NOTICE

- Please read through this `README.md` to better understand the project's source code and setup instructions.
- Also, make sure to review the contents of the `License/` directory.
- Your attention to these details is appreciated — enjoy exploring the project!

## Problem Statement

- I needed a public-facing website to present my portfolio, receive contact messages, and support newsletter subscriptions. The solution had to be stable, secure, production-ready, and accessible via a real domain.

---

## Project Goals

### Deploy a Django-powered personal portfolio

- Build and launch a Django website accessible from anywhere using a secure tunnel to a real domain.

### Enable messaging, subscriptions, and project showcasing

- Provide an interactive UI for users to send messages, learn about my work, and subscribe to updates.

---

## Tools, Materials & Resources

### Django + Python Backend

- Django framework used for routing, form handling, and backend logic, written in Python.

### Gunicorn + NGINX + Cloudflare Tunnel

- Gunicorn serves the Django app as WSGI, reverse-proxied by NGINX, with secure tunneling via Cloudflare.

### GitLab CI/CD + Ansible

- GitLab Runner triggers deployments, executes Ansible tasks for DB migrations, media collection, and system updates.

---

## Design Decision

### Gunicorn and NGINX production stack

- Selected for stability, reverse proxy performance, and production-grade deployment compatibility.

### Ansible-powered deployment pipeline

- Ensures repeatable, automated deployment steps for updates and configuration changes.

### Security-first development

- Employed Cloudflare Zero Trust, Django middleware, and multi-layer bot prevention for form endpoints.

---

## Features

### Project Portfolio Showcases

- Visitors can view categorized, documented projects with descriptions, links, and visuals.

### Contact Form and Newsletter

- reCAPTCHA-secured contact form allows direct messaging; optional subscription to future project newsletters.

### Full CI/CD Deployment Pipeline

- GitLab Runner + Ansible script push the latest project version with media sync and database migrations to production.

---

## Block Diagram

```plaintext
        +------------------+
        |  Web Environment |
        +--------+---------+
                 |
                 v
        +------------------+
        |    Gunicorn      |  <- WSGI interface to Django on dedicated port
        +--------+---------+
                 |
                 v
        +------------------+
        |     NGINX        |  <- Serves static files from Gunicorn's port & acts as reverse proxy
        +--------+---------+
                 |
                 v
        +------------------+
        |   Cloudflare     |  <- Connects the outside to Nginx's port
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
```

---

## Functional Overview

- Gunicorn serves the Django app as a WSGI service.
- NGINX proxies requests to Gunicorn and handles static file delivery.
- Cloudflare Tunnel connects external users securely to the private server.
- Django provides page routing, project display, reCAPTCHA validation, and secure form handling.

---

## Challenges & Solutions

### Deploying Django in a true production environment

- Solved via Gunicorn + NGINX reverse proxy and managed process hosting.

### Preventing spam and bots on contact forms

- Integrated Google reCAPTCHA v3, honeypot fields, rate limiting, and user-agent detection via middleware.

---

## Lessons Learned

### Technical Field

- CI/CD workflows with GitLab Runner and Ansible.
- Secure production deployment using Cloudflare Tunnels, Gunicorn, and NGINX.

### Web Security Practices

- Built layered defenses against bots and spam, combining rate limiting, CAPTCHA, honeypots, and custom middleware.

---

## Project Structure

```plaintext
root/
├── License/
│   ├── LICENSE.md
│   └── NOTICE.md
│
├── .gitattributes
│
├── .gitignore
│
├── README.md
│
├── folioframe/
│   ├── bip/
│   │   └── BeforeItsPrinted app
│   │
│   ├── foliofin/
│   │   └── FolioFin app
│   │
│   ├── folioframe/
│   │   └── FolioFrame project
│   │
│   ├── foliogate/
│   │   └── FolioGate app
│   │
│   ├── foliohome/
│   │   └── FolioHome app
│   │
│   ├── static/
│   │   └── static files
│   │
│   ├── templates
│   │   └── page templates
│   │
│   └── manage.py
│
├── inventory/
│   └── hosts.ini
│
├── .gitlab-ci.yml
│
├── .gitmodules
│
├── ansible.cfg
│
├── deploy.yml
│
├── folioframe.gunicorn
│
├── folioframe.nginx
│
├── register.sh
│
└── requirements.txt
```

---

## Future Enhancements

- Add project search and filtering system.
- Build an analytics dashboard for traffic and form submission insights.
- Integrate comment/discussion widgets on showcased projects.
- Expand newsletter into a subscriber-focused content feed.
