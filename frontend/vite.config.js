import {defineConfig} from 'vite';
import uni from '@dcloudio/vite-plugin-uni';


export default defineConfig({
	plugins: [
		uni(),
	],
	server: {
		host: "localhost",
		port: 5180,
		proxy: {
			[process.env.VITE_APP_BASE_API]: {
				target: process.env.VITE_API_BASE_URL,
				secure: false, // 请求是否为https
				changeOrigin: true, // 是否跨域
				rewrite: (path) => path.replace(/^\/api/, '')
			},
		},
	}
});