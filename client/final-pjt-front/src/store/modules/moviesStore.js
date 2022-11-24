import axios from 'axios'

const moviesStore = {
  namespaced: true,
  state: () => ({
    completed_movies: [],
    savedMovies: [],
    watchList: [],
    likeMovies: [],
  }),
  getters: {
  },
  mutations: {
    SAVE_MOVIES(state, movies) {
      state.savedMovies = movies
    },
    COMPLETED_MOVIES(state, completed_movies) {
      state.completed_movies = completed_movies.map(element => Object.values(element)[1])
    },
    GET_WATCHLIST(state, movies) {
      state.watchList = movies
    },
    GET_LIKE_MOVIES(state, movies) {
      state.likeMovies = movies
    },
  },
  actions: {
    saveMovies(context, movies) {
      context.commit('SAVE_MOVIES', movies)
    },
    completedMovies(context, completed_movies) {
      context.commit('COMPLETED_MOVIES',completed_movies)
    },
    getWatchlist(context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/watchlist/505642/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`,}
      })
        .then((res) => {
          context.commit('GET_WATCHLIST', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getLikeMovies(context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/likemovie/505642/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`,}
      })
        .then((res) => {
          context.commit('GET_LIKE_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}

export default moviesStore