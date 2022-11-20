<template>
  <div>
    <ReviewsList
    :reviews='reviews'/>
    <h1>최신순 잘나옵니다.</h1>
  </div>
</template>

<script>
import ReviewsList from '@/components/reviews/ReviewsList'

export default {
  name : 'ReviewsViewsView',
  components: {
    ReviewsList
  },
  // created: {
  //   viewsReviews() {
  //     this.$store.actions.viewsReviews
  //   }
  // },
  // computed: {
  //   reviews() {
  //     return this.$store.state.reviews
  //   }
  // }
}
</script>

<style>

</style>