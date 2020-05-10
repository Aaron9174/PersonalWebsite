import Vue from 'vue';
import VueRouter from 'vue-router';
import Ping from '../components/Ping.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  base: process.env.BASE_URL,
  mode: 'history',
  routes: [
    {
      component: Ping,
      name: 'Ping',
      path: '/ping',
    },
  ],
});

export default router;
