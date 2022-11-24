import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import CKEditor from 'ckeditor4-vue';



Vue.use(VueMaterial)
Vue.use( CKEditor );
Vue.config.productionTip = false
Vue.prototype.$axios = axios;
Vue.prototype.$API_URL = 'http://127.0.0.1:8000';

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
