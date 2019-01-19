---
title: 探究 Webpack Tree Shaking
date: 2018-01-21 21:23:59
categories: 前端技术
tags:
 - webpack
---

借着给手头一个项目重构的契机，倒腾了下从 Webpack2 开始支持的 Tree-Shaking 技术，即去除代码中没有用到的 ES6 代码，缩减打包后的文件体积。

>「Tree-Shaking」- 可以将应用程序想象成一棵树。绿色表示实际用到的源码和 library，是树上活的树叶。灰色表示无用的代码，是秋天树上枯萎的树叶。为了除去死去的树叶，必须摇动这棵树，使它们落下。

首先，需要配置 Babel 让其保留 ES6 模块化语句，修改 `.babelrc` 文件为如下：
```js
{
  "presets": [
    ["env", { "modules": false }]
  ]
}
```
*p.s 如果使用了诸如 [`babel-plugin-add-module-exports`](https://github.com/59naga/babel-plugin-add-module-exports) 的插件，会由于上述的设置导致不起作用，要寻找别的替代方案。后来我改用了 [`babel-plugin-es2015-modules-umd`](https://www.npmjs.com/package/babel-plugin-transform-es2015-modules-umd)。

webpack 本身并不会执行 tree-shaking。它需要依赖于像 `UglifyJS` 这样的第三方工具来执行实际的未引用代码(dead code)删除工作。