<template>
  <div class="home">
    <div class="p-5">
      <SwiperView style="padding: 20px 0px;"/>

      <!-- 목록별 5개 영화 -->
      <div class="card mb-3 movie-list">
        <div class="row g-0">
          <div class="col-md-10">
            <div class="recommend_div movie-list">
              <div class="row row-cols-5 row-cols-md-5 g-3">
                <div class="col"
                  v-for="movie in carouselMovies"
                  :key="movie.id">
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
            <h3>맞춤 영화</h3>
            <p>고객님의 맞춤영화를 제공합니다!</p>
            <i class="bi bi-arrow-right"></i>
            <md-button class="md-icon-button md-accent">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" style="width:30px;" fill='red'><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/>
              </svg>
            </md-button>
          </div>
        </div>
      </div>

      <div class="card mb-3 movie-list">
        <div class="row g-0">
          <div class="col-md-10">
            <div class="recommend_div movie-list">
              <div class="row row-cols-5 row-cols-md-5 g-3">
                <div class="col"
                  v-for="movie in carouselMovies"
                  :key="movie.id">
                  <div class="card" style="height: 100%">
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
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" style="width:30px;" fill='red'><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/>
              </svg>
            </md-button>
            
          </div>
        </div>
      </div>

      <!-- 인기 리뷰 -->

        <div class="back">
          <h4>인기 리뷰</h4>
          <div>
            <div style="display: flex; justify-content: space-around;">
              <p>제목</p>
              <p>영화 제목</p>
              <p> 작성자 </p>
            </div>
            <div
            v-for="review in popular_reviews"
            :key="review.id" 
            class="reviewList"
            >
            <hr style="margin: 0px">
            <div>
              <div  style="display: flex; justify-content: space-around; cursor: pointer ;" @click="reviewDetail(review)" >
                <p>{{ review.title }}</p>
                <p>{{ review.movie.title }}</p>
                <p>{{ review.username }}</p>
              </div>
            </div>
          </div>

        </div>
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
      carouselMovies : null,
      popular_reviews : null,
    }
  },
  components : {
    SwiperView
  },
  created() {
    this.popularMovies()
    this.popularReviews()
  },

  methods: {
    popularMovies() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/movies/savemovies/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then((res) => {
          this.movies = res.data
          this.carouselMovies = res.data.slice(0,5)
          // console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    popularReviews() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/reviews/popular/`, // 임시방편 게시글 좋아요 확인 후 해보자.
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
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
    }

  }
}
</script>

<style scoped>
 .recommend_div{
  background-color: #C30F24; 
  padding: 1rem;
  /* margin-top: 10px; */
  /* margin-bottom: 10px; */
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


