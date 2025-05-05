def validate_content(content: str):
    """
    验证笔记内容是否有效

    参数:
        content: 笔记内容

    异常:
        ValueError: 当内容为空时抛出
    """
    if not content:
        raise ValueError("Content cannot be empty")


def validate_id(id: int):
    """
    验证笔记ID是否有效

    参数:
        id: 笔记ID

    异常:
        ValueError: 当ID小于0时抛出
    """
    if id < 0:
        raise ValueError("ID must be a positive integer")


class Service:
    def __init__(self, db):
        self.db = db

    def create_note(self, content: str) -> int:
        """
        创建笔记，返回笔记ID

        参数:
            content: 笔记内容，不能为空

        返回:
            int: 创建的笔记ID

        异常:
            ValueError: 当内容为空时抛出
        """
        validate_content(content)
        return self.db.create_note(content)

    def query_note(self, id: int) -> dict:
        """
        查询笔记，返回笔记详情

        参数:
            id: 笔记ID，不能小于0

        返回:
            dict: 包含笔记详情的字典

        异常:
            ValueError: 当ID小于0或笔记不存在时抛出
        """
        validate_id(id)
        return self.db.query_note(id)

    def update_note(self, id: int, content: str) -> bool:
        """
        更新笔记，返回是否成功

        参数:
            id: 笔记ID，不能小于0
            content: 新的笔记内容，不能为空

        返回:
            bool: 更新成功返回True

        异常:
            ValueError: 当ID小于0、内容为空或笔记不存在时抛出
        """
        validate_id(id)
        validate_content(content)
        return self.db.update_note(id, content)

    def delete_note(self, id: int) -> bool:
        """
        删除笔记，返回是否成功

        参数:
            id: 笔记ID，不能小于0

        返回:
            bool: 删除成功返回True

        异常:
            ValueError: 当ID小于0或笔记不存在时抛出
        """
        validate_id(id)
        return self.db.delete_note(id)
