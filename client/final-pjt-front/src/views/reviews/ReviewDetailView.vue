<template>
  <div>
    <div class="back">
        <md-card>
          <md-card-header style="background-color: black; color: white;">
            <div class="md-title">{{review.title}}</div>
            <div class="md-subhead">{{review.movie}}</div>
          </md-card-header>
          <br>
          <md-card-content style="display: flex; justify-content: center;" v-html="review.content">
            <!-- {{review.content}} -->
          </md-card-content>
          <i class="fa-solid fa-grid-2">넌 또 어디누</i>
          <div 
          style="margin-left:5%; margin-right:2%;
          display: flex; justify-content: space-between;">
            <div class="d-flex">
            <!-- <button @click="LikeReview()">{{ reviewLike }}</button> -->
            <md-button class="md-icon-button md-accent" @click="LikeReview()">
              <!-- <md-icon v-if="reviewLike === '좋아요 취소'">thumb_up</md-icon> -->
              <i class="fa fa-thumbs-up" aria-hidden="true">어디누</i>
              <!-- <md-icon v-if="reviewLike === '좋아요'">thumb_up_off_alt</md-icon> -->
            </md-button>
            <p>{{review.like_users.length}}</p>
            </div>
            <div>
              <button type="button" class="btn btn-dark" @click="MoveUpdate()">Update</button>
              <button type="button" class="btn btn-danger" @click="DeleteReview()">DELETE</button>
            </div>
          </div>
        </md-card>
    </div>
    <!-- 댓글 작성 및 출력 -->
    <div class="back">
        <md-card>
          <md-card-header style="background-color: white; color: white;">
            <form @submit.prevent="CreateReviewComment">
              <md-field style="width:80%; margin-left: auto; margin-right: auto;">
                <label for="reviewcomment">reviewComment</label>
                <md-input v-model="reviewComment" type="text" id="reviewcomment"></md-input>
                <button type="submit" id="submit" class="btn btn-dark" >Submit</button>
              </md-field>
            </form>
            <form @submit.prevent="CreateReviewComment">
              <div>
                <label for="reviewcomment"> 댓글 작성: </label>
                <input type="text" id="reviewcomment" v-model.trim="reviewcomment"><br>
                <input type="submit" id="submit">
              </div>
            </form>
          </md-card-header>
 
          <br>
          <!-- 댓글 출력 -->
          <md-card-content style="display: flex; justify-content: center;">
            <ReviewComment
            :comments="review?.reviewcomment_set"
            @delete-review-comment="deleteReviewComment"
            />
          </md-card-content>
        </md-card>
    </div>
    

    

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
      reviewLike: null,
      reviewId: null,
      reviewcomment : '',
      content: null,
    }
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
          this.review = res.data
          this.reviewLike = res.data.reviewLike
          this.content = res.data.content
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
          this.reviewLike = res.data.message
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
          this.ReviewRead()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    reviewLookUp() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/reviews/${this.reviewId}/lookup/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`}
      })
    },
  },
  created() {
    this.reviewId = this.$route.params.id
    this.ReviewRead()
    this.reviewLookUp()
  },
  beforeRouteUpdate(to, from, next) {
    this.reviewId = this.$route.params.id
    next();
  },
}
</script>

<style scoped>
  .back {
    margin: 20px;
    background-color : white ;
    border-radius: 20px;
  };
</style>