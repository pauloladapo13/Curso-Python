import sqlite3

mConnetion= sqlite3.connect("ProductStore")

mCursor= mConnetion.cursor()


mCursor.execute(''' CREATE TABLE ProductStore (ITEM_CODE VARCHAR(4) PRIMARY KEY,
ITEM_NAME VARCHAR(50), PRICE INTEGER,
SECTION VARCHAR(20))
 ''')

products=[

    ("AR01", "trousers",15,"outfit"),
    ("AR02", "hdmi cable",25,"tecno"),
    ("AR03", "plate",45,"items"),
    ("AR04", "pelota",20,"toystore"),

]

mCursor.executemany("INSERT INTO ProductStore VALUES (?,?,?,?)", products)

mConnetion.commit()



mConnetion.close()