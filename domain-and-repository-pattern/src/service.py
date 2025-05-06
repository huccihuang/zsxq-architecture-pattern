import random
from model import Note

class Service:
    def __init__(self, repository):
        self.repository = repository

    def create_note(self, content: str) -> Note:
        """
        创建一条新笔记。

        参数:
            content: 笔记内容，不能为空。

        返回:
            Note: 创建的笔记对象

        异常:
            ValueError: 如果内容为空则抛出
        """
        note = Note(id=random.randint(1, 1000000), content=content)
        self.repository.create_note(note)
        return note

    def query_note(self, id: int) -> Note:
        """
        根据ID查询笔记。

        参数:
            id: 笔记ID

        返回:
            Note: 查询到的笔记对象

        异常:
            ValueError: 如果ID无效或未找到笔记则抛出
        """
        note = self.repository.query_note(id)
        return note

    def update_note(self, id: int, content: str) -> Note:
        """
        更新笔记，返回是否成功

        参数:
            id: 笔记ID，不能小于0
            content: 新的笔记内容，不能为空

        返回:
            Note: 更新完成的note

        异常:
            ValueError: 当ID小于0、内容为空或笔记不存在时抛出
        """
        note = self.repository.query_note(id)
        note.update_content(content)
        self.repository.update_note(note)
        return note

    def delete_note(self, id: int) -> None:
        """
        删除笔记，返回是否成功

        参数:
            id: 笔记ID，不能小于0

        异常:
            ValueError: 当ID小于0或笔记不存在时抛出
        """
        return self.repository.delete_note(id)
