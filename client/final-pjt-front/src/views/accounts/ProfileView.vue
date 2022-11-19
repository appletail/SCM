<template>
  <div>
    <h1>This is profile page</h1>
    <p>{{ profile?.username }}</p>
    <p>{{ profile?.nickname }}</p>
    <p>{{ profile?.introduce }}</p>
    <button @click="deleteUser">회원탈퇴</button>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  data() {
    return {
      profile: null,
    }
  },
  methods: {
    getProfile() {
      this.$axios({
        method: 'get',
        url: `${this.$API_URL}/accounts/${this.username}`,
        headers: {
          Authorization: `Bearer ${this.access_token}`
        }
      })
        .then((res) => {
          this.profile = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteUser() {
      this.$axios({
        method: 'DELETE',
        url: `${this.$API_URL}/accounts/${this.profile.username}`,
        headers: {
          Authorization: `Bearer ${this.access_token}`
        }
      })
        .then(() => {
          this.$router.push({ name:'home' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  computed: {
    username() {
      return this.$route.params.userName
    },
    access_token() {
      return localStorage.getItem('jwt')
    },
  },
  created() {
    this.getProfile()
  }
}
</script>

<style>

</style>