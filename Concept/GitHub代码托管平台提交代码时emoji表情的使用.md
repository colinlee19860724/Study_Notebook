# GitHub 代码托管平台提交代码时 emoji 表情的使用

&emsp;&emsp;日语：絵文字/えもじ emoji，是日本在无线通信中所使用的视觉情感符号，**绘**指图画，**文字**指的则是字符，可用来代表多种表情，如`笑脸`表示笑、`蛋糕`表示食物等。emoji 频繁地出现在我们的聊天记录、朋友圈，甚至很多时候我们都会用 emoji 代替文字来聊天，来传达自己想要表达的一切，作为一名程序员，常用的代码托管平台 GitHub 中也是可以使用 emoji 表情的。  
&emsp;&emsp;执行 git commit 时使用 emoji 为本次提交打上一个 `标签`， 使得此次 commit 的主要工作得以凸现，也能够使得其在整个提交历史中易于区分与查找，添加了 emoji 表情的提交记录真的能包含很多有用信息，阅读体验非常棒。  
&emsp;&emsp;但是，emoji 表情在提交代码的时候也不能乱用，否则容易造成误解。因此开源项目 gitmoji 专门规定了在 GitHub 提交代码时应当遵循的` emoji 规范`。  

## commit 格式

**git commit 时，提交信息遵循以下格式：**  
`:emoji1: :emoji2: 提交信息主体`

**初次提交示例：**  
`git commit -m ":tada: fisrt commit"`

## emoji 指南

emoji | emoji 代码 | commit 说明
:---|:---:|:---
:art: (调色板) | `:art:` | 改进代码结构/代码格式
:zap:(闪电) | `:zap:` | 提高性能
:fire: (火焰) | `:fire:` | 移除代码或文件
:bug: (bug) | `:bug:` | 修复 bug
:ambulance: (急救车) | `:ambulance:` | 重要补丁
:sparkles: (火花) | `:sparkles:` | 引入新功能
:memo: (备忘录) | `:memo:` | 撰写文档
:rocket: (火箭) | `:rocket:` | 部署功能
:lipstick: (口红) | `:lipstick:` | 更新 UI 和样式文件
:tada: (庆祝) | `:tada:` | 初次提交
:white_check_mark: (白色复选框) | `:white_check_mark:` | 增加测试
:lock: (锁) | `:lock:` | 修复安全问题
:apple: (苹果) | `:apple:` | 修复 macOS 下的问题
:penguin: (企鹅) | `:penguin:` | 修复 Linux 下的问题
:checkered_flag: (旗帜) | `:checkered_flag:` | 修复 Windows 下的问题
:bookmark: (书签) | `:bookmark:` | 发行/版本标签
:rotating_light: (警车灯) | `:rotating_light:` | 移除 linter 警告
:construction: (施工) | `:construction:` | 工作进行中
:green_heart: (绿心) | `:green_heart:` | 修复 CI 构建问题
:arrow_down: (下降箭头) | `:arrow_down:` | 降级依赖
:arrow_up: (上升箭头) | `:arrow_up:` | 升级依赖
:construction_worker: (工人) | `:construction_worker:` | 添加 CI 构建系统
:chart_with_upwards_trend: (上升趋势图) | `:chart_with_upwards_trend:` | 添加分析或跟踪代码
:hammer: (锤子) | `:hammer:` | 重大重构
:heavy_minus_sign: (减号) | `:heavy_minus_sign:` | 减少一个依赖
:whale: (鲸鱼) | `:whale:` | Docker 相关工作
:heavy_plus_sign: (加号) | `:heavy_plus_sign:` | 增加一个依赖
:wrench: (扳手) | `:wrench:` | 修改配置文件
:globe_with_meridians: (地球) | `:globe_with_meridians:` | 国际化与本地化
:pencil2: (铅笔) | `:pencil2:` | 修复错别字
:ok_hand: (OK手势) | `:ok_hand:` | 由于代码审查更改而更新代码


一起来使用吧！  