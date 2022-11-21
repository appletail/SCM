<template>
  <div>
    {{review}}
    
    <div>
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
      reviewcomment : ''
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
          console.log(res.data)
          // console.log(this.$route.params.id)
          this.review = res.data
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
    }
    ,
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
      console.log('좋아요.')
      console.log(localStorage.getItem('username'))
      console.log(localStorage.getItem('jwt'))
      
      if (this.review.like_users.indexOf(localStorage.getItem('username')) != -1) {
        console.log('이미 포함되어있어요.')
        this.review.like_users.splice(this.review.like_users.indexOf(localStorage.getItem('username')),1)
      } else {
        this.review.like_users.push(localStorage.getItem('username'))
      }
    }
    // deleteComment(comment) {
    //   console.log(comment)
      // this.$axios({
      //   method:'DELETE',
      //   url: `${this.$API_URL}/reviews/comments/${comment.id}/`,
      //   headers: {
      //     Authorization: `Bearer ${localStorage.getItem('jwt')}`
      //   }
      // })
      //   .then(() => {
      //     console.log('잘 전달됬다.')
      //     this.ReviewRead()
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
        // }
    
  }
}
</script>

<style>

</style>