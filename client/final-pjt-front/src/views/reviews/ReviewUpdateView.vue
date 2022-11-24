<template>
  <div>
    <div class='back'>
      <form @submit.prevent="UpdateReview">
        <md-field style="width:80%; margin-left: auto; margin-right: auto;">
          <label>Title</label>
          <md-input v-model="title"></md-input>
        </md-field>

        <md-field 
        style="width:80%; margin-left: auto; margin-right: auto;">
          <label>{{movie_title}}</label>
          <md-input disabled></md-input>
        </md-field>

        <div style="margin-left: auto; margin-right: auto;">
          <label for="content"></label>
          <ckeditor v-model="content" :config="editorConfig"></ckeditor><br>
        </div>
        <!-- <md-field style="width:80%; margin-left: auto; margin-right: auto;">
          <label>Content</label>
          <md-textarea v-model="content"></md-textarea>
        </md-field> -->
        <div style="padding: 10px 0px;">
          <button type="submit" class="btn btn-dark centering" 
          style="width:80%; margin-left: auto; margin-right: auto;">제출</button>
        </div>
      </form>
    </div> 
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
        height: '25rem', 
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
          this.movie_title = res.data.movie.title
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

<style scoped>
  .back {
    margin: 20px;
    background-color : white ;
    border-radius: 20px;
  };
</style>