import { createSSRApp } from "vue";
import App from "./App.vue";
import uviewPlus, { setConfig } from 'uview-plus';
import * as Pinia from 'pinia';
import 'uno.css';

export function createApp() {
	const app = createSSRApp(App);
	app.use(uviewPlus)
	app.use(Pinia.createPinia());
	return {
		app,
		Pinia
	};
}
