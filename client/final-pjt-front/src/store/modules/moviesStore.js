const moviesStore = {
  namespaced: true,
  state: () => ({
    savedMovies: {},
  }),
  getters: {
  },
  mutations: {
    SAVE_MOVIES(state, movies) {
      state.savedMovies = movies
    },
  },
  actions: {
    saveMovies(context, movies) {
      context.commit('SAVE_MOVIES', movies)
    },
  }
}

export default moviesStore