<template>
  <div class="p-3">
    <div>
      <SwiperView style="padding: 20px 0px;"/>

      <!-- 최신 영화 5개 -->
      <div class="card mb-3 movie-list">
        <div class="row g-0">
          <div class="col-md-10">
            <div class="recommend_div movie-list">
              <div class="row row-cols-5 row-cols-md-5 g-3">
                <div class="col"
                  v-for="movie in latest_movies"
                  :key="movie.id"
                  style="cursor: pointer;"
                  >
                  <div class="card" style="height: 100%"
                  @click='moveMovieDetail(movie)'>
                    <img :src="movie.img_url" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">{{movie.title}}</h5>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-2" style="height : 100%; margin-top: auto; margin-bottom: auto;">
            <h3>최신 영화</h3>
            <p>최신 영화를 소개합니다!</p>
            <i class="bi bi-arrow-right"></i>
            <md-button class="md-icon-button md-accent" @click="moveLatestMovie">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" style="width:30px;" fill='red'><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/>
              </svg>
            </md-button>
          </div>
        </div>
      </div>

      <!-- 인기 영화 5개 -->
      <div class="card mb-3 movie-list">
        <div class="row g-0">
          <div class="col-md-10">
            <div class="recommend_div movie-list">
              <div class="row row-cols-5 row-cols-md-5 g-3">
                <div class="col"
                  v-for="movie in popular_movies"
                  :key="movie.id"
                  style="cursor: pointer;"
                  >
                  <div class="card" style="height: 100%"
                  @click='moveMovieDetail(movie)'>
                    <img :src="movie.img_url" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">{{movie.title}}</h5>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-2" style="height : 100%; margin-top: auto; margin-bottom: auto;">
            <h3>인기 영화</h3>
            <p>최근 인기영화를 소개합니다!</p>
            <md-button class="md-icon-button md-accent" @click="movePopularMovie">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" style="width:30px;" fill='red'><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/>
              </svg>
            </md-button>
          </div>
        </div>
      </div>


      <!-- 인기 리뷰 -->
        <div>
          <md-table class="back p-3">
            <h4>인기 리뷰</h4>
            <md-table-row style="text-align: center">
              <md-table-head md-numeric style="text-align: center">제목</md-table-head>
              <md-table-head style="text-align: center">영화제목</md-table-head>
              <md-table-head style="text-align: center">작성자</md-table-head>
              <md-table-head style="text-align: center">작성일자</md-table-head>
              <md-table-head style="text-align: center">조회수</md-table-head>
            </md-table-row>

            <md-table-row
            v-for="review in popular_reviews"
            :key="review.id"
            @click="reviewDetail(review)"
            style="cursor: pointer;"
            >
              <md-table-cell md-numeric style="text-align: center">{{ review.title }}</md-table-cell>
              <md-table-cell style="text-align: center">{{ review.movie.title }}</md-table-cell>
              <md-table-cell style="text-align: center">{{ review.username }}</md-table-cell>
              <md-table-cell style="text-align: center">{{ review.created_at.substr(0,10) }}</md-table-cell>
              <md-table-cell style="text-align: center">{{ review.Lookup_cnt }}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
    </div>
  </div>
</template>

<script>
import SwiperView from '@/components/Swiper/SwiperView.vue'

export default {
  name: 'HomeView',
  data() {
    return {
      movies: [],
      latest_movies: [],
      popular_movies : [],
      popular_reviews : [],
    }
  },
  components : {
    SwiperView
  },
  created() {
    this.LatestMovies()
    this.popularMovies()
    this.popularReviews()
  },

  methods: {
    LatestMovies() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/movies/latest/1/`,
      })
        .then((res) => {
          this.movies = res.data
          this.latest_movies = res.data.slice(0,5)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    popularMovies() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/movies/popular/1/`,
      })
        .then((res) => {
          this.movies = res.data
          this.popular_movies = res.data.slice(0,5)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    popularReviews() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/reviews/popular/`,
      })
        .then((res) => {
          this.popular_reviews = res.data.slice(0,5)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    reviewDetail(review) {
      this.$router.push({ name: 'detailview', params: { id: review.id } })
    },
    moveMovieDetail(movie) {
      this.$router.push({ name : 'moviedetail', params: {id: movie.id}})
    },
    movePopularMovie() {
      this.$router.push({ name : 'MovieListItems', params: { movieListName: 'popular' }} )
    },
    moveLatestMovie() {
      this.$router.push({ name : 'MovieListItems', params: { movieListName: 'latest' }} )
    },

  }
}
</script>

<style scoped>
 .recommend_div{
  background-color: #C30F24; 
  padding: 1rem;
 }

.movie-list{
  border-radius: 1rem;
}
        
.reviewList :hover {
  background-color : gray;
}

.back {
    background-color : white ;
    border-radius: 10px;
  };
</style>


