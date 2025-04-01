import { defineConfig } from "vite";
import uni from "@dcloudio/vite-plugin-uni";
// https://vitejs.dev/config/
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        api: 'modern-compiler' // 或 "modern"
      }
    }
  },
  plugins: [uni()],
  server: {
    host: "0.0.0.0",
    port: 5180,
    proxy: {
      [process.env.VITE_API_BASE_NAME]: {
        target: process.env.VITE_API_BASE_URL,
        secure: false, // 请求是否为https
        changeOrigin: true, // 是否跨域
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});
