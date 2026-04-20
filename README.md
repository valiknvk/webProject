# Basic Web Portfolio

## Introduction
Web application with login functionality, a user profile page, and a template-driven portfolio page.
The repository is sanitized so personal details live outside tracked source files.

## What changed
- Personal profile content moved into JSON-based portfolio templates.
- Deployment samples now use placeholders instead of personal domains, image names, and credentials.
- Application settings load from environment variables instead of hard-coded secrets.

## Technologies
- Python 3 / Flask
- PostgreSQL
- Docker / Docker Compose
- Kubernetes manifests

## Portfolio customization
1. Copy `imageLogin/login/content/portfolio.template.json` to `imageLogin/login/content/portfolio.local.json`.
2. Update the copied file with your own public portfolio data.
3. Optionally set `PORTFOLIO_PROFILE_PATH` to load the file from another private location.

Apply the same pattern for `initApp/login` if you still use that starter app.

## Environment configuration
- Copy `floginDeploy/.env.example` to `floginDeploy/.env` for local compose usage.
- Set `FLASK_SECRET_KEY` and PostgreSQL variables before running in any real environment.
- Replace placeholder container images in Docker/Kubernetes manifests with your own registry paths.

## Project status
The codebase now includes the first privacy-focused refactor. The next logical cleanup is deduplicating `initApp` and `imageLogin` into one reusable Flask package.
