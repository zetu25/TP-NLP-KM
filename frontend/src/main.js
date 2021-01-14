import { createApp } from 'vue';
import App from './App.vue';
import router from "./router/router";
import store from "./store/storage";
import '@/assets/css/tailwind.css';



const app = createApp(App);

app.use(router);
app.use(store);

app.mount("#app");
