<template>
  <div>
    <ReviewCommentItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
    />
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
  method: {
  }
}
</script>

<style>

</style>