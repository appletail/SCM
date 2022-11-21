<template>
  <div>
    <ReviewCommentItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
    @delete-review-comment="deleteReviewComment"
    />

    <!-- <p
    v-for="comment in comments"
    :key="comment.id">

    </p> -->
  
  </div>
</template>

<script>
import ReviewCommentItem from '@/components/reviews/ReviewCommentItem.vue'

export default {
  name:'ReviewComment',
  components:{
    ReviewCommentItem
  },
  props : {
    comments : Array,
  },
  methods: {
    deleteReviewComment(comment) {
      this.$emit('delete-review-comment', comment)
    },
    readReview() {
      this.$emit('read-Review')
    }
  }
}
</script>

<style>

</style>