import sqlite3

mConnetion= sqlite3.connect("ProductStore")

mCursor= mConnetion.cursor()


# mCursor.execute(''' CREATE TABLE ProductStore (ID INTEGER PRIMARY KEY AUTOINCREMENT,
# NOMBRE_ARTICULO VARCHAR(50) UNIQUE, PRICE INTEGER,
# SECTION VARCHAR(20))
#  ''')

# products=[

#     ("trousers",15,"outfit"),
#     ("hdmi cable",25,"tecno"),
#     ("plate",45,"items"),
#     ("pelota",20,"toystore"),
#     ("jeans",35, "outfit")
# ]


# mCursor.executemany("INSERT INTO ProductStore VALUES (NULL,?,?,?)", products)

# mCursor.execute("INSERT INTO PRODUCTSTORE VALUES (`'AR05','tren', 15, 'transport')")



# mCursor.execute("UPDATE PRODUCTSTORE SET PRICE= 35 WHERE NOMBRE_ARTICULO='pelota'")

mCursor.execute("DELETE FROM PRODUCTSTORE WHERE ID=5")


# products= mCursor.fetchall()

# print(products)




mConnetion.commit()



mConnetion.close()