<template>
  <div class="p-2">
    <div class="back">
      <div class="d-flex p-5">
        <img :src="movie?.img_url" alt="" style="width:16em; border-radius: 1rem;">
        <div>
          <span class="p-3 d-flex justify-content-start align-content-start">
            <div class="d-flex flex-column align-items-start">
              <h1>{{movie?.title}}</h1>
              <p>{{movie?.release_date}}</p>
            </div>
            <div class="d-flex mx-3">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" fill="rgb(245, 224, 39)" style="width: 40px; content: 40px 40px;	position: relative; bottom: 2.2rem; right: 0.1rem;"><path d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"/>
              </svg>
              <h3>{{movie?.vote_average}}</h3>
            </div>
          </span>
          <div class="m-3 d-flex flex-column justify-content-between" style="text-align: start;">
            <div><h5>{{movie?.description}}</h5></div>
            <div>fasjkhklasd</div>
          </div>
        </div>
      </div>
      <hr>
      <div>
        <h2>출연진</h2>
        <MovieCrewSwiperView
        :crews="movie?.crews"/>
      </div>
      <br>
      <div>
        <h2>비슷한 장르 인기 영화</h2>
        <SimilarMovieSwiperView
        :movies="similar_movies"/>
      </div>
      <br>
    </div>
    <md-table class="reviews back p-3">
      <h4>이 영화의 리뷰</h4>
      <md-table-row style="text-align: center">
        <md-table-head md-numeric style="text-align: center">제목</md-table-head>
        <md-table-head style="text-align: center">영화제목</md-table-head>
        <md-table-head style="text-align: center">작성자</md-table-head>
        <md-table-head style="text-align: center">작성일자</md-table-head>
        <md-table-head style="text-align: center">조회수</md-table-head>
      </md-table-row>

      <md-table-row
      v-for="review in movie?.review_set"
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
</template>

<script>
import MovieCrewSwiperView from "@/components/Swiper/MovieCrewSwiperView.vue"
import SimilarMovieSwiperView from "@/components/Swiper/SimilarMovieSwiperView.vue"

export default {
  name: "MovieDetail",
  data() {
    return {
      movie: null,
      similar_movies : [],
      movie_id : null,
    }
  },
  components : {
    MovieCrewSwiperView,
    SimilarMovieSwiperView
  },
  created() {
    this.movie_id = this.$route.params.id
    this.ReadMovie()
  },
  beforeRouteUpdate(to, from, next) {
    this.movie_id = to.params.id;
    this.ReadMovie()
    next();
  },
  methods : {
    ReadMovie() {
      this.$axios({
        method: 'get',
        url: `${this.$API_URL}/movies/${this.movie_id}/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`},
      })
      .then((res) => {
        this.movie = res.data
        this.ReadSimilar()
      })
      .catch((err) => {
        console.log(err.response.data)
      })
    },
    ReadSimilar() {
      for (const element of this.movie.genres) {
        this.$axios({
          method: 'get',
          url: `${this.$API_URL}/movies/genre/${element.id}/`,
          headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`},
        })
        .then((res) => {
          const append_data = res.data.slice(0,10)
          for (const movie of append_data) {
            if (this.similar_movies.indexOf(movie) === -1) {
              this.similar_movies.push(movie)
            }
          }
        })
        .catch((err) => {
          console.log(err.response.data)
        })
      }
    },
    reviewDetail(review) {
      this.$router.push({ name: 'detailview', params: { id: review.id } })
    },
  }
}

</script>

<style scoped>
  element {
    --url_path: null;
  }

 .back {
    margin: 20px;
    background-color : white ;
    border-radius: 20px;
  };

.reviewList{
  border-radius: 1rem;
}
        
.reviewList :hover {
  border-bottom-left-radius: 1rem;
  border-bottom-right-radius: 1rem;
  background-color : gray;
}

</style>