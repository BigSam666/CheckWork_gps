系统名称：云围栏打卡系统
项目描述：本web系统主要技术通过百度鹰眼的云围栏来设置打卡的坐标点及半径，用户在此围栏半径内通过手机浏览器gps定位实现坐标点上传至百度鹰眼，并通过后台判断用户坐标是否在云围栏范围内，从而实现用户打卡功能。
系统设计：本系统采用restful设计风格，前端框架使用bootstrap，后端使用python的轻量型框架flask。数据库使用mysql存储员工数据，缓存数据库使用redis存储用户登录token。部署时使用nginx服务器进行文件缓存,压缩,反向代理及负载均衡等。
主要功能：
    员工：上下班打卡，本人考勤数据查看/导出
    管理员：云围栏坐标点及半径设置，员工考勤数据查看/导出
    其他：登录，注册，忘记密码，个人中心信息修改
硬件需求：PC,智能手机
软件需求：火狐浏览器，手机端使用火狐浏览器中文版
系统优点：相对于指纹打卡，刷脸打卡，虹膜打卡等，本系统不再过分依赖硬件设备，减少硬件维修成本。
系统缺点：由于本系统使用手机浏览器进行定位，目前定位技术尚不成熟，存在一定的误差性。并且本系统在员工通过接口上传坐标点时，可能通过其他作弊手段上传坐标，造成虚假打卡。
