from app import app  # gunicorn wsgi:app

if __name__ == "__main__":
    app.run()
