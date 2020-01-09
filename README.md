# flask-api-demo
# 1.项目介绍
1.1 本项目基于flask-restful,实现简单的增删改查restful api.

## 1.2 项目目录结构

```python
│——manage.py  # flask启动文件
│——README.md
│——requirements.txt  # 依赖包
│——settings.py  # 配置文件
│          
├─api
│  │  models.py  # 模型类
│  │  __init__.py  # 创建flask_app
│  │  
│  ├─serializer  # 序列化文件
│  │      author.py
│  │      book.py
│  │      publisher.py
│  │      
│  ├─static  # 静态文件夹
│  ├─templates  # 模板文件夹
│  ├─views  # 视图类
│  │  │  api.py  
│  │  │  author.py
│  │  │  book.py
│  │  │  publisher.py
│  │  │  __init__.py  # 创建API实例,添加url对应类
│ 
├─migrations  # 数据库迁移文件夹
```

## 1.3 说明

- 未使用 flask-restful 序列化模型

- 使用序列话模型如下(demo中有示例)(详细见book)

  ```python
  # 序列化使用如下
  # 1.定义序列话字段
  resource_fields = {
      'username': fields.String,
      'age': fields.Integer,
      'school': fields.String,
      'tags': fields.List(fields.String),  # 列表
      'more': fields.Nested({  # 嵌套对象
          'signature': fields.String
      })
  }
  
  # 2.装饰器对应函数
  @marshal_with(resource_fields,envelope="data")
  def get(self):
      user = User(1,"python",12)
      return user
  # 注意字段需要保持一样
  
  # 扩展
  # 一般返回前端是 {"code":"1000","msg":"ok","data":数据库数据}
  resource_firlds = {
      "code": fields.String,
      "msg": fields.String,
      "data": fields.Nestes({  # 可对应一个或多个数据库对象
          "id": field.Integer,
          "name": field.String
      })
  }
  # 外键 多对多详细见book文件,注意fields字段和数据库需要保持一致
  ```

# 2.项目启动
## 2.1 初始化数据库
- 在settings中进行数据库配置
```python
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@127.0.0.1:3306/booktest?charset=utf8"
```
以上表示账户名是root,密码是123456,注意需要先手动建立数据库booktest
- 初始化
```python
# 数据库迁移命名
python manage.py db init  # 表示初始化
python manage.py db migrate # 类似于django makemirations
python manage.py db upgrade # 类似于django migrate
```
## 2.2 安装依赖包
```python
pip -r requirements.txt
```
## 2.3 启动项目

```python
python manager.py runserver
# 访问 127.0.0.1:5000/api/v1/hello
# 返回 {"hello": "world"}
```

# 3.项目注意事项

## 3.1 未使用蓝图,view分模块基于API 类

```python
# 1. 在view __init__ 中实例化 Api()
# 导入类,定义路由关系(模块按路由类进行分类)
# 2.在 api __init__ create_app()中初始化api
# 所有路由关系即在app中进行了定义
```

## 3.1 未进行异常处理

```
对所有参数应该进行判断处理,简单的demo未进行处理
```

