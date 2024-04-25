import mysql.connector
from rich.console import Console
console = Console()

def dbconfig():
    db = None
    try:
        db = mysql.connector.connect(
              host='localhost',
              user='PasswordManager',
              passwd='password')
        

    except Exception as e:
        console.print_exception(show_locals=True)
    

    return db
    
