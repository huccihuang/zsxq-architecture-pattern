# 架构模式示例项目

这个项目用于展示和对比不同的软件架构模式，帮助开发者理解各种架构模式的实现方式和应用场景。每个架构模式都通过一个相同的笔记应用来演示，方便进行横向对比。

## 已实现的架构模式

### 分层架构 (Layered Architecture)

位于 `layered_architecture/` 目录，展示了经典的三层架构实现。

```
layered_architecture/
├── src/              # 源代码
│   ├── ui/          # 用户界面层
│   ├── service/     # 业务逻辑层
│   └── infra/       # 基础设施层
└── tests/           # 测试代码
```

[查看分层架构具体说明](layered_architecture/README.md)

### 领域模型和仓储模式 (Domain Model and Repository Pattern)

位于 `domain-and-repository-pattern/` 目录，展示了领域驱动设计中的领域模型和仓储模式实现。

```
domain-and-repository-pattern/
├── src/              # 源代码
│   ├── model.py     # 领域模型
│   ├── repository.py # 仓储层
│   ├── service.py   # 服务层
│   ├── ui.py        # 用户界面层
│   ├── db.py        # 数据库访问
│   └── main.py      # 应用入口
```

这种架构模式的特点：
- 领域模型包含业务规则和逻辑
- 仓储模式封装数据访问细节
- UI层使用内置类型而非领域模型，实现关注点分离
- 服务层协调领域模型和仓储层

[查看领域模型和仓储模式具体说明](domain-and-repository-pattern/README.md)

## 环境要求

- Python 3.11 或以上
- uv（非必需，但使用 `uv sync` 可以快速安装依赖）

## 许可证

本项目使用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件
