# VEGERTALLE — Flask + gunicorn

Запуск на сервері:

    python3 -m venv venv && . venv/bin/activate
    pip install -r requirements.txt
    gunicorn -c gunicorn.conf.py wsgi:app

За замовчуванням слухає 0.0.0.0:8000 (змінити: `BIND=127.0.0.1:9000`, кількість воркерів: `WEB_CONCURRENCY=3`).
Перевірка: `/healthz` повертає `ok`.

Тексти й контакти — у `app.py` (SITE, SERVICES, PERKS), розмітка — `templates/index.html`,
стилі — `static/css/styles.css`, скрипти — `static/js/main.js`, фото — `static/img/`.

Для nginx: `proxy_pass http://127.0.0.1:8000;` (статику можна віддавати напряму з `static/`).
