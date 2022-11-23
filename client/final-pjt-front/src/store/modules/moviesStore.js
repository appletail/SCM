const moviesStore = {
  namespaced: true,
  state: () => ({
    savedMovies: {},
    completed_movies: []

  }),
  getters: {
  },
  mutations: {
    SAVE_MOVIES(state, movies) {
      state.savedMovies = movies
    },
    COMPLETED_MOVIES(state, completed_movies) {
      state.completed_movies = completed_movies.map(element => Object.values(element)[1])
    }
  },
  actions: {
    saveMovies(context, movies) {
      context.commit('SAVE_MOVIES', movies)
    },
    completedMovies(context, completed_movies) {
      context.commit('COMPLETED_MOVIES',completed_movies)
    }
  }
}

export default moviesStore