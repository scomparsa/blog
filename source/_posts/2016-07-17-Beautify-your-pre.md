---
title: 美化你的 <pre /> 标签
date: 2016-07-17 10:26:57
categories: 前端技术
tags:
 - html
 - css
---

{% asset_img pre.png %}

今天看到一个比较漂亮的 `<pre />` 样式，记录一下 ^_^

<!-- more -->

```css
pre {
  padding: 22px;
  line-height: 1.6 !important;
  border: 1px solid #dde4e6;
  box-shadow:
    inset 0 1px 0 #fff,
    1px 1px 0 #fff,
    2px 2px 0 #dde4e6,
    3px 3px 0 #fff, 4px 4px 0 #dde4e6;
  background-color: #fff;
  background-image: -webkit-linear-gradient(#EAEEEF .1em, transparent .1em);
  background-image: -o-linear-gradient(#EAEEEF .1em, transparent .1em);
  background-image: linear-gradient(#EAEEEF .1em, transparent .1em);
  background-size: 100% 1.6em;
}
```
