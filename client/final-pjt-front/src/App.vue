<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light">
      <router-link to="/">Home |</router-link>
      <router-link :to="{ name: 'login' }" v-if="!is_login">Login |</router-link>
      <router-link :to="{ name: 'signup' }" v-if="!is_login">Signup |</router-link>
      <router-link :to="{ name: 'logout' }" v-if="is_login">logout |</router-link>
      <router-link :to="{ name: 'profile', params:{ userName: username() } }" v-if="is_login">profile |</router-link>
      <router-link :to="{ name : 'reviewlatest'}">review |</router-link>
      
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'LogoutView',
  data() {
    return {
    }
  },
  methods: {
    username() {
      return localStorage.getItem('username')
    },
  },
  computed: {
    is_login() {
      return this.$store.state.accountsStore.is_login
    },
  },
  created() {
    this.$store.dispatch('accountsStore/login')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
