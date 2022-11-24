<template>
  <div>
    <div>
      <h1>자기소개</h1>
      {{ introduce }}
    </div>
    <hr>
    <div>
      <p>보고 싶은 영화</p>
      <watchListSwiperView
        :watchList="watchList"
      />
      <hr>
      <p>좋아요한 영화</p>
      <likeMoviesSwiperView
        :likeMovies="likeMovies"
      />
    </div>
  </div>
</template>

<script>
import watchListSwiperView from '@/components/Swiper/watchListSwiperView.vue'
import likeMoviesSwiperView from '@/components/Swiper/likeMoviesSwiperView.vue'

export default {
  name: "ProfileItemView",
  components: {
    watchListSwiperView,
    likeMoviesSwiperView,
  },
  props: {
    introduce: String,
    watchList: Array,
    likeMovies: Array,
  }
  
}
</script>

<style>

</style>