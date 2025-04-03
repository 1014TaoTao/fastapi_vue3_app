<div align="center">
   <p align="center">
      <img src="./frontend/src/static//logo.png" height="150" alt="logo"/>
   </p>
   <h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">Fastapi_Vue3_App</h1>
   <h4 align="center">A rapid development framework for mobile, mini-program, and H5 applications with separated front - end and back - end, based on Fastapi - Vue3 - App.</h4>
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

English | [Chinese](./README.md)

## Introduction to the FastAPI-Vue3-App Project

### Project Overview

FastAPI-Vue3-App is a full-stack open-source project designed to assist developers in quickly building mobile, mini-program, and H5 applications. The backend uses FastAPI for asynchronous programming to enhance the application's concurrent processing capabilities, SQLModel to simplify database operations, Alembic to manage database versions, and JWT for authentication and authorization. The frontend utilizes Vue3 to build user interfaces, combines with Vite for rapid construction, leverages UniApp for cross-platform development, and pairs with uView-plus to enrich components. It provides a one-stop development solution, which is efficient and convenient.

> Backend Technology Stack:

- **FastAPI**: Utilizes asynchronous programming features to enhance the application's concurrent processing capabilities.
- **SQLModel**: A simple and easy-to-use ORM tool that simplifies database operations.
- **Alembic**: A database migration tool for managing database versions.
- **JWT**: Used for authentication and authorization.

> Frontend Technology Stack:

- **Vue3**: A progressive JavaScript framework for building user interfaces.
- **Vite**: A fast frontend build tool that supports hot reloading.
- **UniApp**: A cross-platform application development framework that supports multi-terminal development.
- **uView-plus**: A Vue3-based UI component library that provides a rich set of components.

### Main Features

- **Easy to Get Started**: Provides a complete project structure and sample code to reduce initial configuration time.
- **Modular Design**: Each component is developed independently for easy maintenance and expansion.
- **Comprehensive Documentation**: Detailed README and API documentation for easy learning and reference.
- **Community Support**: Completely open source. Welcome to submit issues and pull requests.

### Directory Structure

```sh
fastapi_vue3_app/
├─ backend        # Backend directory
├─ frontend       # Frontend directory
├─ README.en.md   # English documentation
└─ README.md      # Chinese documentation
```

### Page Display

<table>
    <tr>
        <td><img src="./frontend/public/登录.jpeg"/>登陆</td>
        <td><img src="./frontend/public/注册.jpeg"/>注册</td>
   </tr>
   <tr>
        <td><img src="./frontend/public/忘记密码.jpeg"/>忘记密码</td>
        <td><img src="./frontend/public/首页.jpeg"/>首页</td>
   </tr>
    <tr>
        <td><img src="./frontend/public/个人中心.jpeg"/>个人中心</td>
   </tr>
</table>

### Quick Start

- 1. Clone the project

  - git clone <https://gitee.com/tao__tao/fastapi_vue3_app.git>

- 2. Install dependencies:

  - cd fastapi_vue3_app/backend
  - pip install -r requirements.txt

- 3. Start the project: (1. Generate migrations 2. Upgrade migrations 3. Run the project)

  - python3 main.py revision
  - python3 main.py upgrade
  - python3 main.py run

- 4. Access the project:
  
  - 前端地址：<http://127.0.0.1:5180>
  - 账号：`admin` 密码：`123456`
  - 接口地址：<http://127.0.0.1:8000/docs>

### Special Thanks

Thanks to the contributions and support of the following projects, which have enabled the successful completion of this project:

- [FastAPI 项目](https://github.com/fastapi/fastapi)
- [SqlModel 项目](https://github.com/fastapi/sqlmodel)
- [Alembic 项目](https://github.com/sqlalchemy/alembic)
- [PyJWT 项目](https://github.com/jpadilla/pyjwt)
- [Vue3 项目](https://github.com/vuejs/vue)
- [Vite 项目](https://github.com/vitejs/vite)
- [UniApp 项目](https://github.com/dcloudio/uni-app)
- [uView-plus 项目](https://uiadmin.net/uview-plus)

### Participation and Support

Thank you for your attention and support! If you find this project helpful, please give us a Star! Your support is our driving force. At the same time, all developers are welcome to contribute and jointly improve this project.

## 🎨 WeChat Group

Below are the group QR codes, which can be used for technical exchanges and discussions on various issues encountered during the project usage. We sincerely hope that everyone can work together to optimize the project, actively discuss, and support each other!

### Group QR Codes

<table>
    <tr>
      <td><img src="https://github.com/1014TaoTao/fastapi_vue3_admin/blob/master/mkdocs/docs/resources/images/微信.jpg"/></td>
      <td><img src="https://github.com/1014TaoTao/fastapi_vue3_admin/blob/master/mkdocs/docs/resources/images/微信群.jpg"/></td>
      <td><img src="https://github.com/1014TaoTao/fastapi_vue3_admin/blob/master/mkdocs/docs/resources/images/wechatPay.jpg"/></td>
    </tr>
</table>
