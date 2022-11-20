<template>
  <div>
    {{review}}
    
    <div>
      <button @click="MoveUpdate()">Update</button>
      <button @click="DeleteReview()">DELETE</button>

    </div>  
  </div>
</template>

<script>
export default {
  name: 'ReviewDetailView',
  data() {
    return {
      review: null,
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
    
  }
}
</script>

<style>

</style>