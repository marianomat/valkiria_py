

from auth_api.utils import get_cursor


def RunLoginValidations(args):
    cursor = get_cursor()
    cursor.execute('EXEC RunLoginValidations @username="mariano", @password="password", @applicationID=1, @companyID=1, @maxFailedAccessAttemptsBeforeLockout=0, @signInMode=0,@newSessionID="hola",@loginProvider="hola",@providerKey="hola" ')
    return cursor.fetchall()[0]
