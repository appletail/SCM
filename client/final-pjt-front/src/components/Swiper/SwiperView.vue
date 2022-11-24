<template>
  <div>
    <swiper ref="filterSwiper" :options="swiperOption" role="tablist">
    <swiper-slide role="tab" style="width: 30rem; height: 40rem;"
    v-for="movie in popmovies"
    :key="movie.id">
      <img :src="movie.img_url" @click="moveMovie(movie)">
      <p></p>
    </swiper-slide>  
    </swiper>
  </div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import _ from 'lodash'

export default {
  name: 'SwiperView',
  components: {
    swiper,
    swiperSlide
  },
  data () {
    return {
      swiperOption: {
        slidesPerView: 'auto',
        spaceBetween: 6, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: false, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
        autoplay: {
          disableOnInteraction: true,
        },
      },
      popmovies : null
    }
  },
  computed: {
  },
  created() {
    this.popMovies()
  },
  methods: {
    popMovies() {
      const page = _.random(1, 100)
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/movies/popular/${page}/`,
      })
        .then((res) => {
          this.popmovies = res.data.slice(0,10)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    moveMovie(movie) {
      this.$router.push({ name: 'moviedetail', params: { id: movie.id } })
    }
  },
  
}
</script>

<style lang="scss" scoped>
  .swiper-container {
    .swiper-wrapper {
      .swiper-slide {
        width: auto; 
        min-width: 56px; 
        padding: 0px 14px;
        font-size: 14px;
        line-height: 36px;
        text-align: center;
        color: #84868c;
        border: 0;
        border-radius: 18px;
        background: #f3f4f7;
        appearance: none;
        
        cursor: pointer;
      }
    }
  }
</style>