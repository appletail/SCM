<template>
  <div>
    <ReviewsList
    :reviews='reviews'/>
    <h1>인기순 잘나옵니다.</h1>
  </div>
</template>

<script>
import ReviewsList from '@/components/reviews/ReviewsList'

export default {
  name : 'ReviewsPopularView',
  components: {
    ReviewsList
  },
//   created: {
//     popularReviews() {
//       this.$store.actions.popularReviews
//     }
//   },
//   computed: {
//     reviews() {
//       return this.$store.state.reviews
//     }
//   }
}
</script>

<style>

</style>
