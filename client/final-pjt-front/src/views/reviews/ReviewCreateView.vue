<template>
  <div>
    <h3>영화 리뷰 작성</h3>
    <form @submit.prevent="createReview">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="movietitle">영화제목 : </label>
      <input type="text" id="movietitle" v-model.trim="movie_title"><br>
      <label for="content">내용 : </label>
      <ckeditor v-model="content" :config="editorConfig"></ckeditor><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
export default {
  name : 'ReviewCreateView',
  data() {
    return {
      title: null,
      movie_title:null,
      content: null,
      editorConfig: {
        extraPlugins: 'autogrow',
        autoGrow_bottomSpace: 50,
        autoGrow_minHeight: 450,
        autoGrow_maxHeight: 600,
        autoGrow_onStartup: true,
        width: '90%',
      },
    }
  },
  methods: {
    createReview() {
      const title = this.title
      const content = this.content
      const movie_title = this.movie_title
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      } else if (!movie_title) {
        alert('영화제목을 입력해주세요')
      }
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/reviews/create/`,
        data: {
          title: title,
          content: content,
          movie: movie_title,
          // user: this.$store.state.accountsStore.username
        },
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => {
          // console.log(res)
          this.$router.push({ name:'reviewlatest'})
        })
        .catch((err) => {
          console.log('안되요')
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>