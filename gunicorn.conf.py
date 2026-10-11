import multiprocessing, os

bind = os.getenv("BIND", "0.0.0.0:8000")
workers = int(os.getenv("WEB_CONCURRENCY", min(multiprocessing.cpu_count() * 2 + 1, 4)))
threads = 2
timeout = 30
keepalive = 5
accesslog = "-"
errorlog = "-"
