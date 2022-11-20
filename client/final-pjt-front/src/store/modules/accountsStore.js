const accountsStore = {
  namespaced: true,
  state: () => ({
    is_login: false,
  }),
  getters: {
  },
  mutations: {
    LOGIN(state, payload) {
      state.is_login = payload.status
      
    },
  },
  actions: {
    login(context) {
      const token = localStorage.getItem('jwt')
      const status = token ? true : false
      const payload = {status}
      context.commit('LOGIN', payload)
    },
  }
}

export default accountsStore