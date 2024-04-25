from utils.dbconfig import dbconfig
import hashlib
import secrets
import string
import random
import sys

from getpass import getpass
from rich import print as printc
from rich.console import Console
from rich.markup import escape
print(escape("this is [literal]"))


console = Console()


def generateDeviceSecret():
    # Generate a secure device secret using the secrets module
    device_secret = secrets.token_urlsafe(16)
    return device_secret

def config():
    #  create Database
    db = dbconfig()
    cursor = db.cursor()

    printc("[green][+] Creating new config [/green]")

    try:
        cursor.execute("CREATE DATABASE pm;")
    except Exception as e:
        printc("[red][!] An error occured while trying to create db.")
        console.print_exception(show_locals=True) 
        sys.exit(0)  
    printc("[green][+][/green] Database 'pm' created ")


    #  Create Tables
    query = "CREATE TABLE pm.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL);"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created ")

    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL);"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created ")


    while 1:
        mp = getpass("Chosse a MASTER PASSWORD: ")
        if mp==getpass("Re-type: ") and mp!="":
            break
        printc("[yellow][-] Please try again.[/yellow]")


    #  Hash the Master Pass
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+] Generated hash of Master Password [/green]" )

    #  Generate a DEVICE SECRET
    ds = generateDeviceSecret()
    printc("[green][+] Device secret Generated [/green]")

    #  Add them to DB
    query = "INSERT INTO pm.secrets (masterkey_hash, device_secret) values (%s, %s);"
    val = (hashed_mp, ds)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+] Added to the DB [/green]")

    printc("[green][+] Configuration Done![/green]")

    db.close()



config()








