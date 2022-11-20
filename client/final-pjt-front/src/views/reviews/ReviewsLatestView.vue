<template>
  <div>
    <ReviewsList/>
    <!-- :reviews='reviews'/> -->
    <h1>최신순 잘나옵니다.</h1>
  </div>
</template>

<script>
import ReviewsList from '@/components/reviews/ReviewsList'

export default {
  name: 'ReviewsLatestView',
  components: {
    ReviewsList,
  },
  // created: {
  //   latestReviews() {
  //     console.log('실행은 되요')
  //     this.$store.actions.latestReviews
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