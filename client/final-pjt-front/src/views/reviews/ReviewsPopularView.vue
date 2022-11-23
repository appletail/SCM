<template>
  <div>
    <ReviewsList
    :reviews='reviews'/>

  </div>
</template>

<script>
import ReviewsList from '@/components/reviews/ReviewsList'

export default {
  name : 'ReviewsPopularView',
  components: {
    ReviewsList
  },
  data() {
    return {
      reviews: []
    }
  },
  created() {
    this.popularReviews()
  },

  methods: {
    popularReviews() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/reviews/popular/`, // 임시방편 게시글 좋아요 확인 후 해보자.
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
