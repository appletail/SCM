<template>
  <div>
    <div class='back'>
      <form @submit.prevent="createReview">
        <md-field style="width:80%; margin-left: auto; margin-right: auto;">
          <label>Title</label>
          <md-input v-model="title"></md-input>
        </md-field>

        <md-autocomplete v-model="movie_title" :md-options="completed_movies"
        style="width:80%; margin-left: auto; margin-right: auto;">
        <label>Movie</label>
        </md-autocomplete>

        <div style="margin-left: auto; margin-right: auto;">
          <label for="content"></label>
          <ckeditor v-model="content" :config="editorConfig"></ckeditor><br>
        </div>
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
  name : 'ReviewCreateView',
  data() {
    return {
      title: null,
      content: null,
      movie_title:null,
      test_value: '',
      editorConfig: {
        height: '25rem', 
      },
    }
  },
  created() {

  },
  computed: {
    movies() {
      return this.$store.state.moviesStore.savedMovies
    },
    completed_movies() {
      return this.$store.state.moviesStore.completed_movies.slice(0,500)
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
      } else if (this.completed_movies.indexOf(movie_title) === -1) {
        alert('영화제목을 정확히 입력해주세요')
      }
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/reviews/create/`,
        data: {
          title: title,
          content: content,
          movie: this.movies[this.completed_movies.indexOf(this.movie_title)],
        },
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => {
          this.$router.push({ name:'reviewlatest'})
        })
        .catch((err) => {
          console.log('안되요')
          console.log(err)
        })
    },
  }
}
</script>

<style scoped>
  .back {
    margin: 20px;
    background-color : white ;
    border-radius: 20px;
  };
  .centering{
    width:80%; 
    margin-left: auto; 
    margin-right: auto;
    margin-bottom: 10px;
  }
  
</style>