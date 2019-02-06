---
title: 如何支持 Gitalk 评论功能
date: 2019-02-06 13:15:00
categories: git
tags:
  - gitalk
  - comments
---

之前博客的评论系统一直用的是 [disqus](https://disqus.com/)，但是需要翻墙，尤其是移动端访问的时候，根本就加载不了（除非开了 VPN）。国内的一些评论系统： duoshuo、uyan 也都挂了，仅存的一些不知道哪天说不准也关了。既然是技术博客，用 [Gitalk](https://gitalk.github.io/) 自然是最相符的。基于 GitHub issue 和 Preact 实现：首先，有大厂保证稳定性；其次，是喜欢 Gitalk 点击评论页面的动效，最后，使用 GitHub ID 登录，可以拜访各位大佬的主页😊

<!-- more -->

### 申请 GitHub Application
> 因为通过 GitHub 应用鉴权，所以需要 [申请开通](https://github.com/settings/applications/new) 一个 application

{% asset_img github-application-new.png %}

- `Application name` 应用名称，如：xxx 的博客
- `Homepage URL` 博客的地址
- `Application description` 描述，可不填
- `Authorization callback URL` **重要！用来接收鉴权回调的 token，一般和博客的地址保持一致就好**

#### 注册完成之后，会得到 Client ID 和 Client Secret，等会儿用到。

{% asset_img github-oauth.png %}

### 初始化 Gitalk
> 我的博客模板语言用的 [Jade](http://jade-lang.com/)，在适当的地方引入 CSS 和 JS

```jade
// xxx.jade
link(rel="stylesheet", href="https://unpkg.com/gitalk/dist/gitalk.css")
script(src='https://unpkg.com/gitalk/dist/gitalk.min.js')
script.
    (function() {
      var gitalk = new Gitalk({
        clientID: '#{theme.gitalk.clientId}',
        clientSecret: '#{theme.gitalk.clientSecret}',
        repo: '#{theme.gitalk.repo}',
        owner: '#{theme.gitalk.owner}',
        admin: ['#{theme.gitalk.admin}'],
        labels: ['#{theme.gitalk.labels}'],
      })

      gitalk.render('xxx')
    })();
```

- `clientID`, `clientSecret` 填写上一步申请得到的
- `repo` 对应到一个 GitHub repo，建议单独创建一个项目，例如：gitalk
- `owner` Repo 拥有者的用户名，也可以是组织
- `admin` Repo 拥有者或协作者，和 `owner` 填一样即可
- `labels` 对应 Repo issue 的 labels，默认是 ['Gitalk']

*更多 Gitalk 的详细配置，可参考 [官方文档](https://github.com/gitalk/gitalk#options)*

> `gitalk.render('xxx')` 将挂载到 id="xxx" 的 DOM 上

hexo 相关的配置示例：
```yml
#_config.yml
gitalk:
  clientId: xxx
  clientSecret: xxx
  repo: gitalk
  owner: xxx
  admin: xxx
  labels: gitalk
```

### Gitalk ID 的问题

该选项默认值是 `location.href`，用来指定页面的唯一 id，但是有长度限制，不能超过 50。显然，博客地址很容易超过这个长度。这里的解决办法是引入一个 [md5](https://www.npmjs.com/package/blueimp-md5) 库，对 href 加密处理。另外，`location.href` 可能会被分享平台改写（微信分享时会附带一堆 querystring），改用 `location.pathname` 最稳妥。

更新模版配置：

```jade
// xxx.jade
script(src='https://cdn.bootcss.com/blueimp-md5/2.10.0/js/md5.min.js')
...
script.
    (function() {
      var gitalk = new Gitalk({
        clientID: '#{theme.gitalk.clientId}',
        clientSecret: '#{theme.gitalk.clientSecret}',
        id: md5(#theme.gitalk.id)
        ...
      });
    })();
...
```

更新项目配置：

```yml
# _config.yml
gitalk:
  ...
  id: location.pathname
```

### 记得关联 issue

经过上述的操作，已经接入了 Gitalk 来当作评论系统使用。

{% asset_img issue-init.png %}

文章评论对应 repo 里的某条 issue，需要初始化进行关联。当然，如果这篇文章你不希望支持评论，就不用关联了。
最终评论的样子

{% asset_img comments-demo.png %}

完结，撒花 🎉