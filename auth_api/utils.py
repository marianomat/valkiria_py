from django.db import connection

def get_cursor():
    return connection.cursor()
    