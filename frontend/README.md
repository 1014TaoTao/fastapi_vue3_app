# frontend

```sh
frontend/
├─ src                  # 前端源码目录
│  ├─ api               # API目录
│  ├─ components        # 组件目录
│  ├─ pages             # 页面目录
│  ├─ static            # 静态资源目录
│  ├─ utils             # 工具目录
│  ├─ App.vue           # 主组件
│  ├─ main.ts           # 入口文件
│  ├─ manifest.json     # 应用配置文件
│  ├─ pages.json        # 页面配置文件
│  ├─ shims-uni.d.ts    # 类型声明文件
│  └─ uni.scss          # 全局样式文件
├─ .env                 # 前端目录
├─ .gitignore           # git忽略文件
├─ .env                 # 环境变量
├─ index.html           # 首页
├─ package.json         # 项目依赖
├─ shims-uni.d.ts       # 类型声明文件
├─ vite.config.js       # vite配置文件
└─ README.md            # 文档说明
```

## 项目初始化

```sh
npm install
```

### 项目启动

```sh
npm run dev:h5
```

### 项目构建

```sh
npm run build
```

### 注意

在sass1.8.0以上版本报错Deprecation Warning: Sass @import rules are deprecated and will be removed in Dart Sass 3.0.0. 因为新版本Sass的@use语法较为激进，如果升级为@use将会是破坏式更新，所以推荐将sass固定在以下版本结局报警。
"uview-plus": "^3.3.74", 版本不要升级
"unocss": "^0.58.9", 版本不要升级
"sass": "1.63.2",    //sass版本不要升级
"sass-loader": "10.4.1",  //sass-loader版本不要升级
