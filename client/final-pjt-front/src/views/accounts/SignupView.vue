<template>
  <div>
    <h1>Signup page</h1>
    <form @submit.prevent="signup">
      <input type="text" placeholder="아이디" v-model="username"><br>
      <input type="text" placeholder="닉네임" v-model="nickname"><br>
      <input type="password" placeholder="비밀번호" v-model="password"><br>
      <input type="password" placeholder="비밀번호 확인" v-model="password_confirm">
      <button>회원가입</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      nickname: null,
      password: null,
      password_confirm: null,
    }
  },
  methods: {
    signup() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/accounts/signup/`,
        data: {
          username: this.username,
          nickname: this.nickname,
          password: this.password,
          password_confirm: this.password_confirm,
        }
      })
        .then(() => {
          this.$router.push({ name:'login' })
        })
        .catch((err) => {
          console.log(err.response.data)
        })
    }
  },

}
</script>

<style>

</style>