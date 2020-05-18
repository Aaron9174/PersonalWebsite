
// -------------------------------- //
//              main.js             //
//       Author: Aaron Hebson       //
//        Entry point of Vue        //
// -------------------------------- //

import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router/index';

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  router,
}).$mount('#app');
