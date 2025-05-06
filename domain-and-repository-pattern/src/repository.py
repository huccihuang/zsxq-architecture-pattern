from model import Note

class NoteRepository:
    def __init__(self, db):
        self.db = db

    def create_note(self, note: Note) -> None:
        """
        创建一条新笔记。

        参数:
            note: 笔记对象
        """
        query = "INSERT INTO notes (id, content, created_time, updated_time) VALUES (?, ?, ?, ?)"
        self.db.execute(query, (note.id, note.content, note.created_time, note.updated_time))

    def query_note(self, id: int) -> Note:
        """
        根据ID查询笔记。

        参数:
            id: 笔记ID

        返回:
            Note: 查询到的笔记对象
        """
        query = "SELECT id, content, created_time, updated_time FROM notes WHERE id = ?"
        cursor = self.db.execute(query, (id,))
        row = cursor.fetchone()
        if row is None:
            raise ValueError("笔记未找到")
        note = Note(id=row[0],
                   content=row[1],
                   created_time=row[2],
                   updated_time=row[3])
        return note

    def update_note(self, note: Note) -> None:
        query = "UPDATE notes SET content = ?, updated_time = ? WHERE id = ?"
        self.db.execute(query, (note.content, note.updated_time, note.id))

    def delete_note(self, id: int) -> None:
        """
        删除笔记。

        参数:
            id: 笔记ID
        """
        query = "DELETE FROM notes WHERE id = ?"
        self.db.execute(query, (id,))


