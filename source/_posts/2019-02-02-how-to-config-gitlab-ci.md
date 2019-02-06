---
title: 如何配置 GitLab CI 
date: 2019-02-02 14:06:00
categories: git
tags:
  - gitlab
  - ci
---

最近在折腾 GitLab CI，想把之前用 Jenkins 执行的 Pipeline 迁移过来（Jenkins 界面实在是。。。），期间遇到一些问题，加上官方文档是纯英文，查询解决的时候花了一些功夫，最后总算满足了项目的持续集成需求。

<!-- more -->

### GitLab CI 的配置文件
> 新建一个 `.gitlab-ci.yml` 文件并进行相应的配置，即可触发 CI 的执行

### 如何配置
#### Stages
> 定义 CI Pipeline 中需要的每个阶段

我这里总共用到了四个阶段：
- `setup` 初始化、安装依赖
- `test` 执行测试
- `build` 生产构建
- `publish` 发布（公司自建的 NPM）

```yml
# .gitlab-ci.yml
stages:
  - setup
  - test
  - build
  - publish
```

#### cache
> 设置对 `node_modules/` 目录的缓存来提速后续 job 的执行。每个 job 执行时，会重置 *.gitignore* 中的文件或目录，设置缓存可避免再次安装。

```yml
# .gitlab-ci.yml
cache:
  # 在各个 job 之间共享该缓存
  key: "$CI_PIPELINE_ID"
  # 缓存即使被 .gitignore 的文件或目录
  untracked: true
  paths:
    - node_modules/
```

#### setup
> 主要是做一些初始化的工作，项目语言是 NodeJS，所以要用 npm 安装 `node_modules/`

```yml
# .gitlab-ci.yml
setup:
  stage: setup
  script:
    # npm-prune 用来移除无关的 packages
    - npm prune
    - npm install
  only:
    - master
```

- `stage` 声明该 job 对应到 stages 中的哪个阶段，名称必须保持一致
- `script` 执行的脚本，多个命令按顺序依次执行
- `only` 尽在当前分支下触发 job 执行

#### test
> 执行测试用例

```yml
# .gitlab-ci.yml
test:
  stage: test
  script:
    - npm test
  # Extract jest coverage result
  coverage: /All files\s*\|\s*([\d\.]+)/
  only:
    - master
```

`coverage`
用于跟踪查找匹配测试覆盖率输出的正则表达式，项目中测试框架用的 jest，输出的测试覆盖率表格如下所示：
```bash
--------------|----------|----------|----------|----------|-------------------|
File          |  % Stmts | % Branch |  % Funcs |  % Lines | Uncovered Line #s |
--------------|----------|----------|----------|----------|-------------------|
All files     |      100 |      100 |      100 |      100 |                   |
 constants.ts |      100 |      100 |      100 |      100 |                   |
 index.ts     |      100 |      100 |      100 |      100 |                   |
--------------|----------|----------|----------|----------|-------------------|
```

所以要保证是 100% 的覆盖率才能继续 pipeline 到下个阶段。

#### build
> 编译构建生产代码

```yml
# .gitlab-ci.yml
build:
  stage: build
  script:
    - npm run build
  artifacts:
    expire_in: 1 min
    paths:
      - dist/*
  only:
    - master
```

`artifacts`
因为后续的 job 依赖本次构建生成的临时文件（或目录），所以通过设置该项，可在该 job 执行成功后，将文件或目录保留至下个阶段，*expire_in* 可设置过期时间。

#### publish
> 发布至 npm

```yml
# .gitlab-ci.yml
publish:
  stage: publish
  script:
    - bnpm publish
  only:
    - master
```

`bnpm` 是公司自建的 npm 仓库

### 环境变量别名的问题
执行 `publish` job 时，报错说找不到命令 `bnpm not found`，但是明明在机器上安装了。bnpm 是基于 cnpm 搭建的，使用方式采用的 `bash alias` 的形式，在环境变量里进行设置：

```bash
# .bashrc 或 .zshrc
alias bnpm="cnpm --registry=http://xxx \
--disturl=http://xxx \
--registryweb=http://xxx \
--cache=$HOME/.bnpm/.cache \
--userconfig=$HOME/.bnpmrc"
```

但是 non-interactive 模式下不支持 bash alias，执行 `man bash` 其中有段说明：
```bash
Aliases are not expanded when the shell is not interactive, 
unless the expand_aliases shell option is set using shopt 
(see the description of shopt under SHELL BUILTIN COMMANDS below).
```

#### before_script
> 在 job 执行前，通过 `shopt` 来扩展别名从而支持 bnpm 命令

```yml
# .gitlab-ci.yml
before_script:
  - shopt -s expand_aliases
  - alias bnpm='cnpm
      --registry=http://xxx
      --disturl=http://xxx
      --registryweb=http://xxx
      --cache=$HOME/.bnpm/.cache
      --userconfig=$HOME/.bnpmrc'
```

至此，一个完整的 Pipeline 就顺利执行了。
{% asset_img pipeline.png %}
