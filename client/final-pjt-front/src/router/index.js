import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import accountsRouter from './accountsRouter.js'
import detailRouter from './detailRouter.js'
import reviewsRouter from './reviewsRouter.js'


Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'home',
    component: HomeView
  },

  ...accountsRouter,
  ...reviewsRouter,
  ...detailRouter,
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
