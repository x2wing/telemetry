import getpass
import logging
from datetime import datetime

import psutil
from logstash_async.handler import AsynchronousLogstashHandler

host = '192.168.88.174'
port = 5000

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(AsynchronousLogstashHandler(
        host, port, database_path='logstash.db'))

extra = {
        'timestamp':datetime.now(),
        'cpu_count':psutil.cpu_count(),
        'user'     :getpass.getuser(),
}
test_logger.info('python-logstash: test extra fields', extra=extra)
