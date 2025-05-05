import sqlite3
from datetime import datetime

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
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL
        )
        ''')
        self.conn.commit()

    def create_note(self, content: str) -> int:
        """
        创建一条新笔记，返回笔记ID

        参数:
            content: 笔记内容

        返回:
            int: 创建的笔记ID
        """

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO notes (content, created_at, updated_at) VALUES (?, ?, ?)",
            (content, now, now)
        )
        self.conn.commit()
        note_id = cursor.lastrowid
        if note_id is None:
            raise RuntimeError("Failed to create note, no ID returned")
        return note_id

    def query_note(self, id: int) -> dict:
        """
        查询笔记，返回笔记详情

        参数:
            id: 笔记ID

        返回:
            dict: 包含笔记详情的字典

        异常:
            ValueError: 当笔记不存在时抛出
        """

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE id = ?", (id,))
        note = cursor.fetchone()

        if not note:
            raise ValueError(f"Note with ID {id} not found")

        return {
            "id": note["id"],
            "content": note["content"],
            "created_at": note["created_at"],
            "updated_at": note["updated_at"]
        }

    def update_note(self, id: int, content: str) -> bool:
        """
        更新笔记内容

        参数:
            id: 笔记ID
            content: 新的笔记内容

        返回:
            bool: 更新成功返回True

        异常:
            ValueError: 当笔记不存在时抛出
        """

        # 先检查笔记是否存在
        self.query_note(id)  # 如果不存在会抛出异常

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE notes SET content = ?, updated_at = ? WHERE id = ?",
            (content, now, id)
        )
        self.conn.commit()
        return True

    def delete_note(self, id: int) -> bool:
        """
        删除笔记

        参数:
            id: 笔记ID

        返回:
            bool: 删除成功返回True

        异常:
            ValueError: 当笔记不存在时抛出
        """

        # 先检查笔记是否存在
        self.query_note(id)  # 如果不存在会抛出异常

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (id,))
        self.conn.commit()
        return True
