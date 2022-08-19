# Stop Now!

[![](https://img.shields.io/badge/for-mcdr2-9cf?style=for-the-badge&labelColor=blue)](https://github.com/Fallen-Breath/MCDReforged)

匹配到指定表达式并等待几秒钟，若服务端未关闭则强制杀死。

用于解决 Fabric 服务端关闭时的玄学问题，详见 [Fallen-Breath/MCDReforged#150](https://github.com/Fallen-Breath/MCDReforged/issues/150)。

## 🚪 前置

```plain
MCDReforged >= 2.2.0
```

## 📄 配置文件

第一次运行时，插件会生成配置文件 **config/stop_now/config.json**。配置项如下：

| 配置项 | 类型 | 说明 |
| - | - | - |
| timeout | `int` | 等待时间 |
| pattern | `str` | 要匹配的正则表达式 |

### 例子
这里提供两种典型用法作为例子。

- 若服务端关闭时存档保存后 5 秒进程仍未结束，则杀死
```json
{
    "timeout": 5,
    "pattern": "All dimensions are saved$"
}
```

- 若服务端关闭过程开始后 5 分钟进程仍未结束，则杀死
```json
{
    "timeout": 300,
    "pattern": "Stopping( the)? server"
}
```
> :warning: 世界保存时杀死服务器可能导致不可挽回的问题。
