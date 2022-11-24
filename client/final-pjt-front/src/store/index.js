import Vue from 'vue'
import Vuex from 'vuex'
import accountsStore from '@/store/modules/accountsStore'
import reviewsStore from '@/store/modules/reviewsStore'
import moviesStore from '@/store/modules/moviesStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accountsStore,
    reviewsStore,
    moviesStore,
    
  },
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
})
