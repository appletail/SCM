<template>
  <div>

    {{movie}}
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.ReadMovie()
  },
  methods : {
    ReadMovie() {
      this.$axios({
        method: 'get',
        url: `${this.$API_URL}/movies/${this.$route.params.id}/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`},
      })
        .then((res) => {
          this.movie = res.data
          console.log(this.movie)
        })
        .catch((err) => {
          console.log(err.response.data)
        })
    },
  }
}
</script>

<style scoped>

</style>