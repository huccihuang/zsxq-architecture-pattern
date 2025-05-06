from datetime import datetime

class Note:
    def __init__(self, id:int, content: str, created_time: datetime | None = None, updated_time: datetime | None = None):
        self.id = id
        self.content = content
        self.created_time = created_time or datetime.now()
        self.updated_time = updated_time or datetime.now()
        self._validate_content()
        self._validate_id()

    def update_content(self, new_content: str):
        """
        更新笔记内容。

        参数:
            new_content: 新的笔记内容，不能为空。

        返回:
            Note: 更新后的笔记对象

        异常:
            ValueError: 如果内容为空则抛出
        """
        self._validate_content()
        self.content = new_content
        self.updated_time = datetime.now()


    def _validate_content(self):
        """
        校验内容不能为空。

        异常:
            ValueError: 如果内容为空则抛出
        """
        if not self.content:
            raise ValueError("Content cannot be empty")

    def _validate_id(self):
        """
        校验ID是否合法。

        异常:
            ValueError: 如果ID为空或小于0则抛出
        """
        if not self.id or self.id < 0:
            raise ValueError("ID cannot be empty")