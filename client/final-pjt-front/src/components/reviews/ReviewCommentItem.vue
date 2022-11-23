<template>
  <div>
    <p v-if="!is_update">
      {{content}}
      <!-- {{comment.user}} -->
      <!-- <button @click="deleteReviewComment(comment)">DELETE</button>
      <button @click="isUpdate">UPDATE</button> -->
      <md-button class="md-button-content" @click="isUpdate">
        <i class="md-icon md-icon-font md-theme-default">update</i>
      </md-button>
      <md-button class="md-button-content" @click="deleteReviewComment(comment)">
        <i class="md-icon md-icon-font md-theme-default">delete</i>
      </md-button>
    </p>
    <form @submit.prevent="commentUpdate" v-if="is_update">
      <input type="text" v-model="content">
      <!-- <button>UPDATE</button> -->
      <md-button class="md-button-content" @click="isUpdate">
        <i class="md-icon md-icon-font md-theme-default">update</i>
      </md-button>
    </form>
    

  </div>
</template>

<script>
export default {
  name : 'ReviewCommentItem',
  data() {
    return {
      is_update : false,
      content : this.comment.content
    }
  },
  props :{
    comment : Object,
  },
  methods: {
    deleteReviewComment(comment) {
      this.$emit('delete-review-comment', comment)
    },
    isUpdate() {
      this.is_update = !this.is_update
    },
    commentUpdate() {
      this.$axios({
        method:'put',
        url: `${this.$API_URL}/reviews/comments/${this.comment.id}/`,
        data: {
          content : this.content
        },
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => {
          this.is_update = !this.is_update
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>

</style>