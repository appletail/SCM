<template>
  <div class="backimage">
    <div class="back">
      <div class="d-flex p-5">
        <img :src="movie.img_url" alt="" style="width:16em;">
        <div>
          <span class="p-3" style="display: flex;">
            
            <h1>{{movie.title}}</h1>
            <div class="d-flex">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" fill="yellow" style="width: 40px; content: 40px 40px;"><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"/>
              </svg>
              <h3>{{movie.vote_average}}</h3>
            </div>
          </span>
          <div>
            <p>{{movie.release_date}}</p>
            <p>{{movie.popularity}}</p>
          </div>
          <div style="border: solid 1px black;">
            <h5>{{movie.description}}</h5>
          </div>
        </div>
      </div>
      <hr>
      <div>
        <p>출연진</p>
        <MovieCrewSwiperView
        :crews="movie.crews"/>
      </div>
      <br>
      <div>
        <p>비슷한 장르 영화</p>
        
      </div>

      {{movie.genres}}
    </div>
  </div>
</template>

<script>
import MovieCrewSwiperView from "@/components/Swiper/MovieCrewSwiperView.vue"

export default {
  name: "MovieDetail",
  data() {
    return {
      movie: null,
    }
  },
  components : {
    MovieCrewSwiperView
  },
  created() {
    this.ReadMovie()
  },
  methods : {
    ReadMovie() {
      this.$axios({
        method: 'get',
        url: `${this.$API_URL}/movies/${this.$route.params.id}/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`},
      })
        .then((res) => {
          this.movie = res.data
          // console.log(this.movie)
        })
        .catch((err) => {
          console.log(err.response.data)
        })
    },
  }
}

// const backdrop_img_url = document.querySelector("element");
// backdrop_img_url.style.setPropertyValue(`${this.movie.backdrop_img_url}`)
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

  .backimage{
    background-image: url("https://image.tmdb.org/t/p/w500/pFlaoHTZeyNkG83vxsAJiGzfSsa.jpg");
  }
</style>