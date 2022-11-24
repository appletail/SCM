<template>
  <div>
    <md-table md-card style = "border: solid 1px black; ">
      <md-table-toolbar>
        <h1 class="md-title">Comment</h1>
      </md-table-toolbar>
      <ReviewCommentItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      @delete-review-comment="deleteReviewComment"
      />

    </md-table>
  
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