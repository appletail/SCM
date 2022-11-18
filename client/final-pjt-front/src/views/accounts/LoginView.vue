<template>
  <div class="login">
    <h1>Login page</h1>
    <form>
      <input type="text" placeholder="아이디"><br>
      <input type="password" placeholder="비밀번호">
    </form>
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