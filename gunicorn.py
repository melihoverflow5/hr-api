import multiprocessing

pidfile = "/tmp/gunicorn.pid"
errorlog = "/tmp/error.log"
accesslog = "/tmp/access.log"
loglevel = "DEBUG"
bind = "0.0.0.0:5000"
daemon= False
timeout = 30
workers = multiprocessing.cpu_count() * 2 + 1