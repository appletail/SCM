<template>
  
  <div>
    <swiper ref="filterSwiper" :options="swiperOption" role="tablist">
    <swiper-slide role="tab" style="width: 200px;"
    v-for="crew in crews"
    :key="crew.id">
      <div class="card"
      @click="moveCrew(crew)">
        <img :src="crew.profile_img_path" alt="">
        <div class="card-body">
          <p class="card-text" style="color: black;">{{crew.name}}</p>
        </div>
      </div>
    </swiper-slide>  
    </swiper>
  </div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'

const move_url =  'https://www.themoviedb.org/person/'
export default {
  name: 'MovieCrewSwiperView',
  components: {
    swiper,
    swiperSlide
  },
  props : {
    crews : Array
  },
  data () {
    return {
      swiperOption: {
        slidesPerView: 'auto',
        spaceBetween: 6, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
      },
      popmovies : null
    }
  },
  created() {
    // console.log(this.crews)
  },
  computed: {
  },
  methods: {
    moveCrew(crew) {
      location.href=move_url+`${crew.id}+${crew.name}?language=ko`;
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