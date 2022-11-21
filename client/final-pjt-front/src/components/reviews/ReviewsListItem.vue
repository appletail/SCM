<template>
  <div >
    <router-link
      @click.native="lookup"
     :to="{ name: 'detailview', params: { id: review.id } } ">
      {{review}}
    </router-link>
  </div>
</template>

<script>
export default {
  name:'ReviewsListItem',
  props: {
    review:Object,
  },
  methods: {
    lookup() {
      // console.log('뭐라도 좀 나와봐')
      console.log(this.review)
      // this.$axios({
      //   method:'post',
      //   url: `${this.$API_URL}/reviews/${this.review.id}/lookup`,
      //   headers: {
      //     Authorization: `Bearer ${localStorage.getItem('jwt')}`
      //   }
      // })
      //   .then(() => {
      //     console.log(this.review.Lookup_cnt)
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
    }
    
  }
}
</script>

<style>

</style>