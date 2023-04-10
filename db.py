import aiosqlite 
from aiogram import types
import sqlite3

async def conn():
    return await aiosqlite.connect('base.db')

con = sqlite3.connect("base.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   tg_id INT,
   data TEXT,
   balance INT,
   TON_wallet,
   quantity_ref,
   UNIQUE ("tg_id") ON CONFLICT IGNORE
   );
""")
conn.commit()

async def checkUser(user_id, user_name, balance, date, number_of_purch):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM users WHERE user_id = ?, user_name = ?, balance = ?, date = ?, number_of_purch = ?", (user_id, user_name, balance, date, number_of_purch,))
    result = await sql.fetchone()
    if result == None:
        _return = 0
    else:
        _return = 1
    await db.close()
    return _return

async def insertUser(user_id, user_name, balance, date, number_of_purch):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("INSERT INTO users VALUES (?)", (user_id, user_name, balance, date, number_of_purch,))
    await db.commit()
    await db.close()
    return 1