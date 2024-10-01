IAM_TOKEN = 't1.9euelZrKyYqOyIuQipfMk5SbnpXMjO3rnpWanJKQy5iVzJbLj5WcnpGJkc7l8_d0MGZO-e8kVjV-_t3z9zRfY0757yRWNX7-zef1656VmsiempiQzYmSzJ2dmZXJlJzP7_zF656VmsiempiQzYmSzJ2dmZXJlJzPveuelZqQyJONjZWVyJvIlJqPl5uYkLXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.rc5qRVqmUCt0LBiiDP9AsAxSFySFPb20wfZ4GNmb7FyXsU6_SqfJzesg2NUy2utJKU254SzyXynYIJTWI86BAg'

TOKEN = "6778859407:AAFGUrC1_7xAWK29nWQFl4nSVRu9M65jLhk"
FOLDER_ID = "b1gbsjnf6hdvvquf2udv"

params = "&".join([
    "topic=general",  # используем основную версию модели
    f"folderId={FOLDER_ID}",
    "lang=ru-RU"  # распознаём голосовое сообщение на русском языке
])

headers = {
    'Authorization': f'Bearer {IAM_TOKEN}',
}

MAX_USER_STT_BLOCKS = 12  # выделяем на каждого пользователя по 12 аудиоблоков

DB_NAME = 'stt_db.db'
TABLE_NAME = 'stt_table'