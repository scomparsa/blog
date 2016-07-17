---
title: Hexo deploy fail?
date: 2016-07-17 11:33:16
tags: hexo
categories: hexo
---

# Hexo 部署失败？

今天在运行 `hexo deploy` 的时候总是提示失败。查了一些 [相关资料](https://github.com/hexojs/hexo/issues/1154)，发现是 `_config.yml` 配置文件里的 `deploy:` 冒号后面缺少一个空格，我用的 Atom IDE，文件保存的时候会自动 trim 掉这个空格！找个文本编辑器重新编辑一下就可以了。如果还是不行，建议重新安装 hexo-deployer-git 这个插件。

坑！坑！坑！
