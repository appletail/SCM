const reviewsStore = {
  namespaced: true,
  state: () => ({
    reviews : [],
    token : null
  }),
  getters: {
  },
  mutations: {
    // LATEST_REVIEWS(state, latestReviews) {
    //   state.reviews = latestReviews
    // },
    // POPULAR_REVIEWS(state, popularReviews) {
    //   state.reviews = popularReviews
    // },
    // VIEW_REVIEWS(state, viewReviews) {
    //   state.reviews = viewReviews
    // }
  },
  actions: {
    // latestReviews(context) {
    //   this.$axios({
    //     method:'get',
    //     url: `${this.$API_URL}/reviews/latest/`,
    //     headers: {
    //       Authorization: `Bearer ${localStorage.getItem('jwt')}`
    //     }
    //   })
    //     .then((res) => {
    //       console.log(res)
    //       context.commit('LATEST_REVIEWS',res.data)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    // popularReviews(context) {
    //   this.$axios({
    //     method:'get',
    //     url: `${this.$API_URL}/reviews/popular/`
    //   })
    //     .then((res) => {
    //       console.log(res)
    //       context.commit('POPULAR_REVIEWS',res.data)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    // viewsReviews(context) {
    //   this.$axios({
    //     method:'get',
    //     url: `${this.$API_URL}/reviews/view/`
    //   })
    //     .then((res) => {
    //       console.log(res)
    //       context.commit('VIEW_REVIEWS',res.data)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // }
  }
}

export default reviewsStore