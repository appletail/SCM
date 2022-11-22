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
    
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

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
