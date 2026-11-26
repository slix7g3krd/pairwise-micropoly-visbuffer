# pairwise-micropoly-visbuffer

## 领域

游戏、图形与多媒体

## 主题

微多边形集群软件光栅与可见性缓冲

## 说明

视锥剔除双缓冲、稳定三角形排序、材质页到达重解析。

初始状态下 `graphics/micropoly.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
