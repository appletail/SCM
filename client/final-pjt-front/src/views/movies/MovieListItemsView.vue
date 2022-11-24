<template>
  <div>
    <div class="container-fluid">
      <div class="list row row-cols-4 d-flex justify-content-center" @scroll="loadPage">
        <MovieListItem
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
          :is_watchlist="watchlist().includes(movie.id)"
          :is_like="likeMovies().includes(movie.id)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem'

export default {
  name: 'MovieListItemsView',
  components: {
    MovieListItem,
  },
  data() {
    return {
      listName: null,

      movies: [],
      page: 0,
    }
  },
  methods: {
    getMovieList() {
      this.page += 1
      this.$axios({
        method: 'get',
        url: `${this.$API_URL}/movies/${this.listName}/${this.page}/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`,},
      })
        .then((res) => {
          if (res.data.pick) {
            alert(res.data.pick)
            this.$router.push({ name : 'MovieListItems', params: { movieListName: 'popular' } })
            console.log(123)
            return
          }
          if (this.page === 1) {
            this.movies = res.data
          } else {
            this.movies = this.movies.concat(res.data)
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadPage(e) {
      const { scrollHeight, scrollTop, clientHeight } = e.target;
      const isAtTheBottom = scrollHeight === scrollTop + clientHeight;
      // 일정 이상 밑으로 내려오면 함수 실행 / 반복된 호출을 막기위해 1초마다 스크롤 감지 후 실행
      if(isAtTheBottom) {
        setTimeout(() => this.handleLoadMore(), 300)
      }
    },
    // 내려오면 api를 호출하여 아래에 더 추가,
    handleLoadMore() {
      // api를 호출하여 리스트 추가하면 됨, 현재는 pushList에 1개의 index 추가
      this.getMovieList()
    },
    watchlist() {
      return this.$store.state.moviesStore.watchList.map((elem) => {
        return elem.id
      })
    },
    likeMovies() {
      return this.$store.state.moviesStore.likeMovies.map((elem) => {
        return elem.id
      })
    },
  },
  computed: {
    loginUser() {
      return localStorage.getItem('username')
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.listName = to.params.movieListName
    this.page = 0
    this.$store.dispatch('moviesStore/getWatchlist')
    this.$store.dispatch('moviesStore/getLikeMovies')
    this.getMovieList()
    next()
  },
  created() {
    this.listName = this.$route.params.movieListName
    this.page = 0
    this.$store.dispatch('moviesStore/getWatchlist')
    this.$store.dispatch('moviesStore/getLikeMovies')
    this.getMovieList()
  },
}
</script>

<style>
.list{
  height: calc(100vh - 70px);
  overflow-y: scroll;

  -ms-overflow-style: none; /* 인터넷 익스플로러 */
  scrollbar-width: none; /* 파이어폭스 */
}

.list::-webkit-scrollbar {
    display: none; /* 크롬, 사파리, 오페라, 엣지 */
}
</style>