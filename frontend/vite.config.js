import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from "vite";
import uni from "@dcloudio/vite-plugin-uni";
import UnoCSS from 'unocss/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    uni(),
    UnoCSS(),
  ],
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
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
});
