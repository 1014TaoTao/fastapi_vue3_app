<div align="center">
   <p align="center">
      <img src="./frontend/static/logo.png" height="150" alt="logo"/>
   </p>
   <h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">Fastapi_Vue3_App</h1>
   <p align="center">
      <a href="https://gitee.com/tao__tao/fastapi_vue3_app.git">
         <img src="https://gitee.com/tao__tao/fastapi_vue3_app/badge/star.svg?theme=dark">
      </a>
      <a href="https://github.com/1014TaoTao/fastapi_vue3_app.git">
         <img src="https://img.shields.io/github/stars/1014TaoTao/fastapi_vue3_app?style=social">
      </a>
      <a href="https://gitee.com/tao__tao/fastapi_vue3_app/blob/master/LICENSE">
         <img src="https://img.shields.io/badge/License-MIT-orange">
      </a>
      <img src="https://img.shields.io/badge/Python-≥3.10-blue">
   </p>
</div>

## FastAPI-Vue3-App 项目简介

### 项目概述

FastAPI-Vue3-App 是一个全栈开源项目，旨在帮助开发者快速搭建基于现代技术栈的移动、小程序和H5应用程序。该项目整合了后端、前端以及跨平台开发所需的多种流行工具和框架，提供了一站式的解决方案。

> 后端技术栈：

- **FastAPI**: 利用异步编程特性，提升应用的并发处理能力。
- **SQLModel**: 简单易用的ORM工具，简化数据库操作。
- **Loguru**: 灵活的日志记录库，提升日志管理效率。
- **Alembic**: 数据库迁移工具，用于管理数据库版本。

> 前端技术栈：

- **Vue3**: 渐进式JavaScript框架，用于构建用户界面。
- **Vite**: 快速的前端构建工具，支持热重载。
- **UniApp**: 跨平台应用开发框架，支持多端开发。
- **Uni-UI**: 基于Vue3的UI组件库，提供丰富的组件。

### 参与和支持

感谢您的关注和支持！如果您觉得这个项目对您有帮助，请给我们点个Star！您的支持是我们前进的动力。同时，也欢迎各位开发者参与贡献，共同完善这个项目。

### 主要特性

- **快速上手**: 提供完整的项目结构和示例代码，减少初期配置时间。
- **模块化设计**: 各个组件独立开发，便于维护和扩展。
- **文档齐全**: 详细的README文档和API文档，方便学习和参考。
- **社区支持**: 完全开源，欢迎提交问题和Pull Request。

### 目录结构

```sh
fastapi_vue3_app/
├─ backend                 # 后端目录
├─ frontend                # 前端目录
└─ README.md               # 项目说明文档
```

### 页面展示

<table>
    <tr>
        <td><img src="./static/img/登录.png"/>登陆</td>
        <td><img src="./static/img/注册.png"/>首页</td>
        <td><img src="./static/img/忘记密码.png"/>首页</td>
   </tr>
   <tr>
        <td><img src="./static/img/首页.png"/>首页</td>
        <td><img src="./static/img/用户页面.png"/>个人中心</td>
   </tr>
</table>

### 快速开始

- 1、克隆项目

  - git clone <https://gitee.com/tao__tao/fastapi_vue3_app.git>

- 2、安装依赖：

  - cd fastapi_vue3_app/backend
  - pip install -r requirements.txt

- 3、启动项目：
  - python3 main.py

- 4、访问项目：
  
  - 前端地址：<http://0.0.0.0:8000/)>
  - 账号：`admin` 密码：`123456`
  - 接口地址：<http://127.0.0.1:8000/docs>

### 特别鸣谢

感谢以下项目的贡献和支持，使本项目得以顺利完成：

- [FastAPI 项目](https://github.com/fastapi/fastapi)
- [SqlModel 项目](https://github.com/fastapi/sqlmodel)
- [Vue3 项目](https://github.com/vuejs/vue)
- [UniApp 项目](https://github.com/dcloudio/uni-app)
- [Uni-UI 项目](https://github.com/dcloudio/uni-ui)

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


```sh

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

