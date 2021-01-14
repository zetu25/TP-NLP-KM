
import { createWebHistory, createRouter } from "vue-router";
import Collection from "@/components/Collection";
import Home from "@/components/Home";

const history = createWebHistory();

const router = createRouter({
    history,
    routes: [
        {
            path: "/results",
            component: Collection
        },
        {
            path: "/",
            component: Home
        }
    ]
})

export default router; 



