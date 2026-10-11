"""VEGERTALLE — сайт ательє на Flask. Запуск: gunicorn wsgi:app"""
from flask import Flask, render_template

app = Flask(__name__, static_folder="static", static_url_path="")

SITE = {
    "name": "VEGERTALLE",
    "tagline": "ательє-майстерня",
    "slogan": "Якість у кожному стібку!",
    "phone_display": "068 808 06 88",
    "phone_href": "tel:+380688080688",
    "address": "Київ, вул. Олександра Архипенка, 8Б",
    "hours_week": "Пн-Пт: 10:00–19:00",
    "hours_sat": "Сб: 12:00–16:00",
    "instagram": "https://instagram.com/",
    "telegram": "https://t.me/",
    "lat": 50.4953529,
    "lng": 30.5149203,
    "zoom": 19,
    "map_open": "https://maps.app.goo.gl/MS83dTwKLL1C3ciC8",
}
SITE["map_embed"] = (
    f"https://www.google.com/maps?q={SITE['lat']},{SITE['lng']}"
    f"&ll={SITE['lat']},{SITE['lng']}&z={SITE['zoom']}&hl=uk&output=embed"
)
SITE["map_dir"] = (
    f"https://www.google.com/maps/dir/?api=1&destination={SITE['lat']},{SITE['lng']}"
)

NAV = [
    ("#home", "Головна"),
    ("#services", "Послуги"),
    ("#works", "Наші роботи"),
    ("#why", "Про нас"),
    ("#contacts", "Контакти"),
]

SEWING = [
    ("/img/sew-coat.jpg", "Пальто з поясом"),
    ("/img/sew-shirt.jpg", "Сорочка з мереживом"),
    ("/img/sew-top.jpg", "Топ із вузлом"),
    ("/img/sew-denim.jpg", "Джинсова куртка"),
]
REPAIRS = [
    ("/img/leather-before.jpg", "Шкіряна куртка: плече до ремонту", "Шкіряна куртка", "До"),
    ("/img/leather-after.jpg", "Шкіряна куртка: плече після ремонту", "Шкіряна куртка", "Після"),
    ("/img/denim-before.jpg", "Джинсова куртка: шкіряний рукав до ремонту", "Джинсова куртка", "До"),
    ("/img/denim-after.jpg", "Джинсова куртка: шкіряний рукав після ремонту", "Джинсова куртка", "Після"),
]

SERVICES = [
    ("M16 8h16l3 34h-8l-3-22-3 22h-8z M16 8l1 6h14l1-6",
     "Вкоротити штани / сукню", "Акуратно, швидко,<br>з ідеальною посадкою."),
    ("M24 6v36M20 10h8M20 16h8M20 22h8M20 28h8M20 34h8",
     "Заміна блискавок<br>та підкладки", "Якісні матеріали<br>та надійна фурнітура."),
    ("M16 17c4-2 12-2 16 0l-2 12 2 15H16l2-15z M20 9a4 4 0 108 0 4 4 0 10-8 0",
     "Підгонка по фігурі", "З урахуванням ваших<br>побажань та особливостей силуету."),
    ("M18 8l-8 6-3 22 7 2V20M30 8l8 6 3 22-7 2V20M18 8c2 4 10 4 12 0M24 14v28",
     "Робота зі шкірою<br>та хутром", "Делікатний підхід<br>та професійне обладнання."),
]
PERKS = [
    ("M16 3l11 4v8c0 7-5 12-11 14C10 27 5 22 5 15V7z M11 16l4 4 6-8",
     "Досвід та професіоналізм", "Багаторічний досвід у сфері пошиву та ремонту одягу."),
    ("M9 5h14l5 7-12 16L4 12zM4 12h24M12 12l4 16 4-16M12 12l-3-7M20 12l3-7",
     "Якісні матеріали", "Працюємо з перевіреними фурнітурами та тканинами."),
    ("M4 16a12 12 0 1024 0 12 12 0 10-24 0 M16 8v8l5 3",
     "Дотримуємося термінів", "Цінуємо ваш час і виконуємо замовлення вчасно."),
    ("M16 28S4 20 4 12a6 6 0 0112-2 6 6 0 0112 2c0 8-12 16-12 16z",
     "Індивідуальний підхід", "Кожен клієнт для нас — важливий."),
]


@app.route("/")
def index():
    return render_template(
        "index.html", site=SITE, nav=NAV, sewing=SEWING, repairs=REPAIRS,
        services=SERVICES, perks=PERKS,
    )


@app.route("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
