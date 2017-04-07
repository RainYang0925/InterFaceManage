## 快速开始

1. 拉取代码后,在`TestTool/settings.py`中配置好数据库
2. 在代码的根目录执行`python manage.py migrate`即可自动生成相关的数据表
3. 在`UserGroup`数据表中插入管理员用户,其中`level`字段输入99(管理员权限)
4. 在根目录执行`python manage.py runserver 0.0.0.0:port`,然后在浏览器访问即可

## InterFaceManage
此项目为接口管理项目代码,负责处理接口相关的功能,包括新增,查询,展示

* errconfig.py

错误码配置文件,可以根据需要修改文案,切忌修改错误代码

* method.py

方法文件,提供数据库的新增接口,更新接口,查询接口的功能

* views.py

web接入层,提供每个url对应的方法,包括页面的方法和Ajax异步的方法

## LogRecord.py

日志记录文件,不提供具体页面,只提供Ajax查询日志的方法

## UserGroup
用户管理项目,包括用户的新增,修改,查询日志等功能

* errconfig.py

错误码配置文件,可以根据需要修改文案,切忌修改错误代码

* method.py

方法文件,提供数据库的新增接口,更新接口,查询接口的功能

* views.py

web接入层,提供每个url对应的方法,包括页面的方法和Ajax异步的方法

## static
前端样式文件,包括css,js,字体等资源文件

## templates
模板文件,根据项目划分

* base.html

所有的html文件都通过继承base.html文件来实现,base.html主要负责全局的资源加载和导航条的统一规范