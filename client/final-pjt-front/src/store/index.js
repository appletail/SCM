import Vue from 'vue'
import Vuex from 'vuex'
import accountsStore from '@/store/modules/accountsStore'
import reviewsStore from '@/store/modules/reviewsStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accountsStore,
    reviewsStore,
    
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
