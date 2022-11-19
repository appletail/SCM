<template>
  <div class="login">
    <h1>Login page</h1>
    <form @submit.prevent="login">
      <input type="text" placeholder="아이디" v-model="username"><br>
      <input type="password" placeholder="비밀번호" v-model="password">
      <button>로그인</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/api/token/`,
        data: {
          username: this.username,
          password: this.password,
        }
      })
        .then((res)=>{
          localStorage.setItem('jwt', res.data.access)
          localStorage.setItem('username', this.username)
          this.$store.dispatch('accountsStore/login')
          this.$router.push({ name: 'home' })
        })
        .catch((err) => {
          console.log(err.response.data)
        })
    },
  },
}
</script>

<style>

</style>