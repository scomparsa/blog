---
title: Jest, 令人愉快的 React 测试
date: 2018-05-20 19:42:31
tags:
  - 单元测试
  - React
  - Redux
  - Jest
  - Facebook
---

提到前端的代码测试，第一印象大家都会觉得是枯燥的，认为是可有可无的部分，这也是为什么很多人乐于去编写 React 应用而不想编写测试的部分。其实不然！完备的测试可以在开发阶段规避很多潜在的风险，提升代码整体的健壮性。

### 什么是 Jest

> [Jest](https://facebook.github.io/jest) 是由 Facebook 开发，用来测试包括 React 在内的所有 JavaScript 代码的测试工具。

它拥有：

- 零配置
- 高速测试和沙盒支持
- 内置的代码测试覆盖率报告
- 功能强大的模拟库
- 支持 TypsScript

等很多特性与 React 技术栈可以说是完美契合。其中的「快照测试」可以记录 React 结构树来简化 UI 测试，并分析 state 如何变化。

### 安装与配置

```bash
npm i -D jest eslint-plugin-jest
```

#### 这里有几点注意

如果在 `.babelrc` 文件中用 `{ "modules": false }` 关闭了 ES6 模块的转译（这样做，经常是为了启用 webpack tree shaking），就必须确保在测试环境 `NODE_ENV=test` 中开启转译

```bash
# .babelrc
{
  "presets": [["env", {"modules": false}], "react"],
  "env": {
    "test": {
      "presets": [["env"], "react"]
    }
  }
}
```
