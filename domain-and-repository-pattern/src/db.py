import sqlite3

class DB:
    def __init__(self, db_path=":memory:"):
        """
        初始化数据库连接

        参数:
            db_path: 数据库文件路径，默认为内存数据库
        """
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        """创建笔记表"""
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_time TIMESTAMP NOT NULL,
            updated_time TIMESTAMP NOT NULL
        )
        ''')
        self.conn.commit()

    def execute(self, query, params=()):
        """
        执行SQL语句

        参数:
            query: SQL语句
            params: SQL参数
        """
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor
