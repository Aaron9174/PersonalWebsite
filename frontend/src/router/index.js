// -------------------------------- //	
//              index.js            //	
//       Author: Aaron Hebson       //	
//  Defines all the routes for app  //	
// -------------------------------- //

import Vue from 'vue';
import VueRouter from 'vue-router';
import Ping from '../components/Ping.vue';
import Sections from '../components/Sections.vue';

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
    {
      component: Sections,
      name: 'Sections',
      path: '/sections',
    },
  ],
});

export default router;
