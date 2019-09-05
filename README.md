# OriginDing

## 📣 简介
OriginDing是一个基于钉钉机器人，自定义消息即时推送到钉钉的Python SDK,适用于消息提示，监控报警等场景

## ✨ 特性
1. 教程齐全，上手容易，调用简单
2. 支持设置级别输出

## ⏳ 版本
当前版本V0.0.0（原始测试版本）

支持 Python2.7，3.4+

## 🔰 安装
目前仅支持git clone到本地，以package形式导入

## 📝 使用

### 在要使用推送功能的群创建机器人，并获取相应的access_token

![](https://raw.githubusercontent.com/zk0601/OriginDing/master/images/step1.jpg)

![](https://raw.githubusercontent.com/zk0601/OriginDing/master/images/step2.jpg)

![](https://raw.githubusercontent.com/zk0601/OriginDing/master/images/step3.jpg)

![](https://raw.githubusercontent.com/zk0601/OriginDing/master/images/step4.png)

![](https://raw.githubusercontent.com/zk0601/OriginDing/master/images/step5.png)

### 在代码中调用

```
# 将package路径添加到PATH
from OriginDing import Dingserver

# 根据上面得到的accsee_token生成对应群的自定义机器人的实例
robot1 = Dingserver(access_token='xxxx')
robot2 = Dingserver(access_token='yyyy')

# 对robot实例进行全局设置，不设置则全采用默认值
"""
level: 推送的消息级别，ERROR、WARN、INFO、DEBUG，ERROR>WARN>INFO>DEBUG, 默认INFO
type: 推送消息类型，目前支持text， markdown，默认text
at_all：是否@所有人，是：True，否：FALSE，默认FALSE
at_users: 需要@的人电话号码，支持多个，List[int], 默认空
"""
robot1.config(level='DEBUG', type='text', at_all=False, at_users=[15927260404, 15927260505])

# 向群里发送消息
robot1.info('这是一条通知信息')
robot1.error('####这是一条严重的错误信息！', type='markdown', at_all=True) # 在单条消息中传入关键字参数可仅在该条信息中覆盖全局设置
robot2.debug('这是一条调试信息')  # 因为robot2的level设置为默认的INFO，所以这条不会发出
```




