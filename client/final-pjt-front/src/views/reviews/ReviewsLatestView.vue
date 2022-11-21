<template>
  <div>
    <ReviewsList
    :reviews='reviews'/>
    <!-- {{latestreviews}} -->

  </div>
</template>

<script>
import ReviewsList from '@/components/reviews/ReviewsList'

export default {
  name: 'ReviewsLatestView',
  components: {
    ReviewsList,
  },
  data() {
    return {
      reviews: []
    }
  },
  created() {
    this.latestReviews()
  },

  methods: {
    latestReviews() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/reviews/latest/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then((res) => {
          this.reviews = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>