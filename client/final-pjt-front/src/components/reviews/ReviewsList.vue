<template>
  <div>
    <h3>Review List</h3>
    <ReviewsListItem
    v-for="review in reviews"
      :key="review.id"
      :review="review"
      />
  </div>
</template>

<script>
import ReviewsListItem from '@/components/reviews/ReviewsListItem.vue'

export default {
  name: 'ReviewsList',
  components : {
    ReviewsListItem,
  },
  // computed: {
  //   reviews() {
  //     return this.$store.state.reviews
  //   }
  // },
  props: {
    reviews: Array,
  }

}
</script>

<style>

</style>