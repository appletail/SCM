const accountsStore = {
  namespaced: true,
  state: () => ({
    is_login: false,
    username: null,
  }),
  getters: {
  },
  mutations: {
    LOGIN(state, payload) {
      state.is_login = payload.status
      state.username = payload.username
      
    },
  },
  actions: {
    login(context) {
      const token = localStorage.getItem('jwt')
      const status = token ? true : false
      const username = localStorage.getItem('username')
      const payload = {status, username}
      context.commit('LOGIN', payload)
    },
  }
}

export default accountsStore