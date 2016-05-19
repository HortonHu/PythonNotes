包结构
```
│  config.py                      配置选项
│  manage.py                      启动程序  
│  requirements.txt
├─app/                           保存程序的所有代码、模板和静态文件
│  │  __init__.py                工厂函数
│  │  email.py                   Email支持函数
│  │  models.py                  数据库模型
│  ├─main/                      子程序包 蓝本
│  │      __init__.py            创建蓝本 导入views.py和errors.py
│  │      errors.py              错误处理程序
│  │      forms.py               表单类
│  │      views.py               程序的路由
│  ├─static/                    存放静态文件
│  └─templates/                 存放模板
│      │  404.html
│      │  base.html
│      │  form.html
│      │  form_test.html
│      │  home.html
│      │  signin-ok.html
│      │  user.html
│      └─mail
├─migrations/                    数据库迁移脚本
│  │  alembic.ini
│  │  env.py
│  │  README
│  │  script.py.mako
│  └─versions
└─tests/                        单元测试
    │  __init__.py
    └─test_basics.py
```        

