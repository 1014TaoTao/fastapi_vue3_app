# 项目介绍

fastapi + sqlmodel
vue3 + vite + uniapp + uni-ui

pip install -r requirements.txt 

python3 main.py

ai大模型技术栈
一、编程语言与工具
    Python为核心语言。
    使用Milvus进行向量数据管理。
    利用Dify、Ollama、vLLM、Xinference等工具进行大模型推理和部署。
    使用Langchain、Langflow构建大模型应用。
    对ChatBI进行调优以提升对话式商业智能的效果。
二、深度学习框架
    主流框架：TensorFlow、PyTorch。
三、大模型基础架构
    知识领域包括RAG、NL2SQL、ChatBI、NL2API、Agent。
    基础架构主要依赖RAG和Agent。
四、模型微调与优化
    微调技术：Fine-tuning、Prompt Engineering。
    优化技术：模型压缩（量化、剪枝、蒸馏）、分布式训练与推理（Data Parallelism, Model Parallelism）。
    具体优化方法：Pretrain、PEFT、SFT、RLHF。
五、自然语言处理（NLP）
    文本预处理：分词、Embedding、序列化。
    常见任务：文本分类、命名实体识别、机器翻译、问答系统。
    评估指标：BLEU、ROUGE、Perplexity。
六、核心技术能力
    熟悉Attention机制和Transformer及其变型。
    能熟练使用PEFT、SFT、RLHF等技术优化大模型效果。

使用正式版（对应HBuilderX最新正式版）
vue create -p dcloudio/uni-preset-vue my-vue3-project
使用Vue3/Vite版:
npx degit dcloudio/uni-preset-vue#vite my-vue3-project


<div align="center">
   <p align="center">
      <img src="./static/favicon.png" height="150" alt="logo"/>
   </p>
   <h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">Fastapi_Jinja2</h1>
   <p align="center">
      <a href="https://gitee.com/tao__tao/fastapi_jinja2.git">
         <img src="https://gitee.com/tao__tao/fastapi_jinja2/badge/star.svg?theme=dark">
      </a>
      <a href="https://github.com/1014TaoTao/fastapi_jinja2.git">
         <img src="https://img.shields.io/github/stars/1014TaoTao/fastapi_jinja2?style=social">
      </a>
      <a href="https://gitee.com/tao__tao/fastapi_jinja2/blob/master/LICENSE">
         <img src="https://img.shields.io/badge/License-MIT-orange">
      </a>
      <img src="https://img.shields.io/badge/Python-≥3.10-blue">
   </p>
</div>

## FastAPI-Jinja2 项目简介

### 项目概述

FastAPI-Jinja2 是一个整合了多个流行技术栈的开源项目，旨在帮助开发者迅速启动并运行基于以下技术的Web应用程序：

- **FastAPI**: 高性能的Web框架，支持异步编程。
- **Jinja2**: 强大的模板引擎，用于生成HTML页面。
- **SQLModel**: 简单易用的ORM工具，简化数据库操作。
- **Loguru**: 灵活的日志记录库，提升日志管理效率。
- **Alembic**: 数据库迁移工具，用于管理数据库版本。

### 参与和支持

感谢您的关注和支持！如果您觉得这个项目对您有帮助，请给我们点个Star！您的支持是我们前进的动力。同时，也欢迎各位开发者参与贡献，共同完善这个项目。

### 主要特性

- **快速上手**: 提供完整的项目结构和示例代码，减少初期配置时间。
- **模块化设计**: 各个组件独立开发，便于维护和扩展。
- **文档齐全**: 详细的README文档和API文档，方便学习和参考。
- **社区支持**: 完全开源，欢迎提交问题和Pull Request。

### 目录结构

```sh
fastapi_jinja2
├─ app
│  ├─ alembic              # 数据库迁移目录
│  ├─ core                 # 核心层模块
│  ├─ model                # 数据层模块
│  ├─ config               # 配置层模块
│  └─ view                 # 视图层模块
├─ logs                    # 日志目录
├─ static                  # 静态目录
├─ templates               # 模板目录
├─ .env                    # 项目环境配置文件
├─ .gitignore              # git 忽略文件
├─ alembic.ini             # alembic 配置文件
├─ main.py                 # 项目启动文件
├─ requirements.txt        # 项目依赖文件
├─ sqlite.db               # 项目数据库文件
└─ README.md               # 项目说明文档
```

### 页面展示

<table>
    <tr>
        <td><img src="./static/img/登录.png"/>登陆</td>
        <td><img src="./static/img/首页.png"/>首页</td>
   </tr>
   <tr>
        <td><img src="./static/img/用户页面.png"/>用户管理</td>
        <td><img src="./static/img/新增页.png"/>用户新增</td>
   </tr>
   <tr>
        <td><img src="./static/img/编辑页.png"/>用户编辑</td>
        <td><img src="./static/img/删除页.png"/>用户删除</td>
   </tr>
   <tr>
        <td><img src="./static/img/详情.png"/>用户详情</td>
   </tr>
</table>

### 快速开始

- 1、克隆项目

  - git clone <https://gitee.com/tao__tao/fastapi_jinja2.git>

- 2、安装依赖：

  - cd fastapi_jinja2
  - pip install -r requirements.txt
  - alembic init app/alembic
  <!-- 生成迁移 -->
  - alembic revision --autogenerate -m "初始化迁移"
  <!-- 应用迁移 -->
  - alembic upgrade head

- 3、启动项目：
  - python3 main.py revision 初始化迁移
  - python3 main.py upgrade
  - python3 main.py run

- 4、访问项目：
  
  - 前端地址：<http://0.0.0.0:8000/)>
  - 账号：`admin` 密码：`123456`
  - 接口地址：<http://127.0.0.1:8000/docs>

### 特别鸣谢

感谢以下项目的贡献和支持，使本项目得以顺利完成：

- [FastAPI 项目](https://fastapi.tiangolo.com/)
- [Jinja2 项目](https://jinja.palletsprojects.com/en/stable/)
- [Bootstrap 项目](https://github.com/twbs/bootstrap)

## 🎨 微信群

在下方为群二维码，可以用于技术交流，也可以一起讨论在项目使用过程中遇到的各种问题。真心希望大家一起优化该项目，积极讨论，让我们一起抱团取暖！

### 群二维码

<table>
    <tr>
      <td><img src="https://github.com/1014TaoTao/fastapi_vue3_admin/blob/master/mkdocs/docs/resources/images/微信.jpg"/></td>
      <td><img src="https://github.com/1014TaoTao/fastapi_vue3_admin/blob/master/mkdocs/docs/resources/images/微信群.jpg"/></td>
      <td><img src="https://github.com/1014TaoTao/fastapi_vue3_admin/blob/master/mkdocs/docs/resources/images/wechatPay.jpg"/></td>
    </tr>
</table>
