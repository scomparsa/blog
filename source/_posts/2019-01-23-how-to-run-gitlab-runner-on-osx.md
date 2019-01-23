---
title: 如何在 OSX 上运行 GitLab Runner
date: 2019-01-23 10:21:35
categories: git
tags: gitlab
---

搭建 GitLab Pages 时用到了 GitLab CI/CD 持续集成，需要一个 Runner 来执行任务。
尽管按照官方文档搭建，还是遇到了一些坑。。。

<!-- more -->

## 安装 [gitlab-ci-multi-runner](https://github.com/ayufan/gitlab-ci-multi-runner)

如果安装[文档](https://github.com/ayufan/gitlab-ci-multi-runner/blob/master/docs/install/osx.md)进行安装，会默认安装最新版本的 runner，但现在的私建 GitLab 版本是 8.x，两者不匹配，要指定安装版本。

### 安装 1.11.2 版本

[GiLab Runnder Release for 1.11.2](https://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/v1.11.2/index.html)

从上面的网站里下载 `binaries/gitlab-ci-multi-runner-darwin-amd64` 到本地，然后执行
```bash
$ cp gitlab-ci-multi-runner-darwin-amd64  /usr/local/bin/gitlab-ci-multi-runner
$ chmod +x /usr/local/bin/gitlab-ci-multi-runner
```

### 注册一个 Runner
执行 `gitlab-ci-multi-runner register` 然后根据提示输入即可完成注册
```bash
Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com )
Please enter the gitlab-ci token for this runner
```
上述两个问题的答案，从项目的 runners 配置里找
{% asset_img runners.png %}
{% asset_img url-token.png %}

到了选择 executor 这步
```bash
Please enter the executor:
```
因为是搭建静态网站服务器，选择 `shell` 即可，一切从简，其他选项还需要额外的配置。
注册以后，刷新刚才的页面，一个 runner 被关联了进来。
{% asset_img active.png %}

### 将 Runner 安装到服务列表
执行 `gitlab-ci-multi-runner install`

### 启动服务
执行 `gitlab-ci-multi-runner start`

至此，一个 GitLab runner 就运行起来了，更多用法可参考[官方文档](https://github.com/ayufan/gitlab-ci-multi-runner/blob/master/docs/commands/README.md)。