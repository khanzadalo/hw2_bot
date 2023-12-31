CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""
CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_user
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BAN_COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""

INSERT_NEW_BAN_USER_QUERY = """
INSERT INTO ban_user VALUES (?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_user WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_user SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
"""