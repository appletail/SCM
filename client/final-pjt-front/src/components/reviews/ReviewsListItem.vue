<template>
  <md-table-row @click="reviewDetail">
    <md-table-cell md-numeric>{{review.title}}</md-table-cell>
    <md-table-cell md-numeric>{{review.movie}}</md-table-cell>
    <md-table-cell md-numeric>{{review.username}}</md-table-cell>
    <md-table-cell md-numeric>{{review1_created_at}}</md-table-cell>
    <md-table-cell md-numeric>{{review.Lookup_cnt}}</md-table-cell>
  </md-table-row>
</template>

<script>
export default {
  name:'ReviewsListItem',
  props: {
    review:Object,
  },
  data() {
    return {
      review1_created_at : this.review.created_at.substr(0,10),
      movie : null,
    }
  },
  created() {
    // this.getMovie()
  },
  methods: {
    reviewDetail() {
      this.$router.push({ name: 'detailview', params: { id: this.review.id } })
    },
    // getMovie() {
    //   this.$axios({
    //     method:'get',
    //     url: `${this.$API_URL}/movies/${this.review.movie}/`,
    //     headers: {
    //       Authorization: `Bearer ${localStorage.getItem('jwt')}`
    //     }
    //   })
    //     .then((res) => {
    //       this.movie = res.data
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // }
    
  }
}
</script>

<style>

</style>