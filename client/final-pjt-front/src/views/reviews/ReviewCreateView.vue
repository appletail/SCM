<template>
  <div>
    <div class='back'>
      <form @submit.prevent="createReview">
        <md-field style="width:80%; margin-left: auto; margin-right: auto;">
          <label>Title</label>
          <md-input v-model="title"></md-input>
        </md-field>

        <md-autocomplete v-model="movie_title" :md-options="movies"
        style="width:80%; margin-left: auto; margin-right: auto;">
        <label>Movie</label>
        </md-autocomplete>

        <div style="margin-left: auto; margin-right: auto;">
          <label for="content"></label>
          <ckeditor v-model="content" :config="editorConfig"></ckeditor><br>
        </div>
        <md-field style="width:80%; margin-left: auto; margin-right: auto;">
          <label>Content</label>
          <md-textarea v-model="content"></md-textarea>
        </md-field>
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
      movie_title:null,
      content: null,
      movies: [],
      test_value: '',
      editorConfig: {
 
      },
    }
  },
  created() {
    this.popularMovies()
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
    },
    popularMovies() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/movies/popular/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
        .then((res) => {
          this.movies = res.data.slice(0,500).map(element => Object.values(element)[1])
          // console.log(res.data.map(element => Object.values(element)[1]))

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
  .centering{
    width:80%; 
    margin-left: auto; 
    margin-right: auto;
    margin-bottom: 10px;
  }
  
</style>