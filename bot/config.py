from os import getenv

IS_PROD = bool(getenv('IS_PROD', False))

BOT_TOKEN = getenv('BOT_TOKEN')
WEBHOOK_PATH = getenv('WEBHOOK_PATH', '/zmanim')

METRICS_DSN = getenv('METRICS_DSN')
METRICS_TABLE_NAME = getenv('METRICS_TABLE_NAME')
