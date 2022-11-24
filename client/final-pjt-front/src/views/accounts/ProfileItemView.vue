<template>
    <div>
      <p v-if="watchList?.length">보고 싶은 영화</p>
      <watchListSwiperView
        :watchList="watchList"
      />
      <hr>
      <p v-if="likeMovies?.length">좋아요한 영화</p>
      <likeMoviesSwiperView
        :likeMovies="likeMovies"
      />
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
    watchList: Array,
    likeMovies: Array,
  }
  
}
</script>

<style>

</style>