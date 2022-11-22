<template>
  <div class="home">
    <div class="p-5">

    <!-- carousel -->
      <div style="width : 400px; margin-bottom : 20px;">
        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active"
              v-for="movie in carouselMovies"
              :key="movie.id">
              <img :src="movie.img_url" class="d-block w-100" alt="...">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>

      <!-- 목록별 5개 영화 -->
      <div class="card mb-3">
        <div class="row g-0">
          <div class="col-md-10">
            <div class="recommend_div">
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
            <h3>맞춤 영화</h3>
            <p>고객님의 맞춤영화를 제공합니다!</p>
            <i class="bi bi-arrow-right"></i>
            <md-button class="md-icon-button">
              <md-icon>thumb_up</md-icon>
            </md-button>
          </div>
        </div>
      </div>

      <div class="card mb-3">
        <div class="row g-0">
          <div class="col-md-10">
            <div class="recommend_div">
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
            <i class="bi bi-arrow-right"></i>
            <md-button class="md-icon-button">
              <md-icon>thumb_up</md-icon>
            </md-button>
          </div>
        </div>
      </div>

      <!-- 인기 리뷰 -->

      <md-card>
        <md-card-header>
          <h4>인기 리뷰</h4>
          <!-- <p class="category">New employees on 15th September, 2016</p> -->
        </md-card-header>
        <md-table>
          <!-- <md-table-row>
            <md-table-head md-numeric>제목</md-table-head>
            <md-table-head>영화 제목</md-table-head>
            <md-table-head>작성자</md-table-head>
            <md-table-head>작성일자</md-table-head>
            <md-table-head>조회수</md-table-head>
          </md-table-row> -->
          <div
            v-for="review in popular_reviews"
            :key="review.id">
            <md-table-row @click="reviewDetail" class="d-flex justify-content-around">
              <md-table-cell md-label="ID">{{ review.title }}</md-table-cell>
              <md-table-cell md-label="Name">{{ review.movie }}</md-table-cell>
              <md-table-cell md-label="Salary">{{ review.username }}</md-table-cell>
            </md-table-row>
          </div>
        </md-table>
      </md-card>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      movies: [],
      carouselMovies : null,
      popular_reviews : null,
      // review1_created_at : this.review.created_at.substr(0,10)
    }
  },
  created() {
    this.popularMovies()
    this.popularReviews()
  },

  methods: {
    popularMovies() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/movies/popular/`,
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
    reviewDetail() {
      this.$router.push({ name: 'detailview', params: { id: this.review.id } })
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



</style>
