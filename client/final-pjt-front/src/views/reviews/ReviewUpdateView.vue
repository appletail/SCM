<template>
  <div>
    <h3>영화 리뷰 작성</h3>
    <form @submit.prevent="UpdateReview">
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
  name : 'ReviewUpdateView',
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
          this.title = res.data.title
          this.movie_title = res.data.movie
          this.content = res.data.content
        })
        .catch((err) => {
          console.log(err)
        })
    },
    UpdateReview() {
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
        method: 'PUT',
        url: `${this.$API_URL}/reviews/${this.$route.params.id}/`,
        data: {
          title: title,
          content: content,
          movie: movie_title,
        },
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => {
          this.$router.push({ name: 'detailview', params: { id: this.$route.params.id } })
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