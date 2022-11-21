<template>
  <div>
    {{review}}
    <!-- <div>
      리뷰 제목 : {{review.title}}
    </div>
    <div>
      리뷰 내용 : {{review.content}}
    </div> -->

    
    <div>
      <!-- <p>좋아요 갯수 : {{review.like_users.length}}</p> -->
      <button @click="LikeReview()">좋아요</button>
      <button @click="MoveUpdate()">Update</button>
      <button @click="DeleteReview()">DELETE</button>
    </div>  
    <form @submit.prevent="CreateReviewComment">
      <div>
        <label for="reviewcomment"> 댓글 작성: </label>
        <input type="text" id="reviewcomment" v-model.trim="reviewcomment"><br>
        <input type="submit" id="submit">
      </div>

    </form>
    <ReviewComment
    :comments="review?.reviewcomment_set"
    @delete-review-comment="deleteReviewComment"
    />
  </div>
</template>

<script>
import ReviewComment from '@/components/reviews/ReviewComment.vue'

export default {
  name: 'ReviewDetailView',
  components: {
    ReviewComment
  },
  data() {
    return {
      review: null,
      reviewcomment : '',
    }
  },
  created() {
    this.ReviewRead()
  },
  methods: {
    ReviewRead() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/reviews/${this.$route.params.id}/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then((res) => {
          // console.log(res.data)
          // console.log(this.$route.params.id)
          this.review = res.data
          console.log()
          this.message = res.data.message
        })
        .catch((err) => {
          console.log(err)
        })
    },
    CreateReviewComment() {
      this.$axios({
        method:'post',
        url: `${this.$API_URL}/reviews/${this.$route.params.id}/reviewscomments/`,
        data:{
          content : this.reviewcomment
        },
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => {
          this.reviewcomment = ''
          this.ReviewRead()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    MoveUpdate() {
      this.$router.push({ name:'updateview' , params: { id: this.review.id }})
    },
    DeleteReview() {
      this.$axios({
        method:'DELETE',
        url: `${this.$API_URL}/reviews/${this.$route.params.id}/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => {
          this.$router.push({ name:'reviewlatest'})

        })
        .catch((err) => {
          console.log(err)
        })
    },
    LikeReview(){
      this.$axios({
        method: 'Post',
        url: `${this.$API_URL}/reviews/${this.review.id}/review_like/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.ReviewRead()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReviewComment(comment) {
      console.log(comment)
      this.$axios({
        method:'DELETE',
        url: `${this.$API_URL}/reviews/comments/${comment.id}/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => {
          // console.log('잘 전달됬다.')
          this.ReviewRead()
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