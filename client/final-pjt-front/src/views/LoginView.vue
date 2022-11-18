<template>
  <div class="login">
    <h1 class="m-5">This is a login page</h1>
    <button type="button" class="btn btn-primary">Primary</button>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {

    }
  },
  created() {
    this.$axios({
      method: 'get',
      url: 'https://api.themoviedb.org/3/movie/popular?api_key=e7a312d46e2782333a636321caf87745&language=ko-KR&page=1'
    })
    .then((res)=>{
      console.log(res)
    })
  }
}
</script>

<style>

</style>