<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light d-flex justify-content-evenly">

      <router-link to="/">
        <div class="content">
          <h2>SCM</h2>
          <h2>SCM</h2>
        </div>
      </router-link>
      <div>
        <router-link :to="{ name: 'login' }" v-if="!is_login">Login |</router-link>
        <router-link :to="{ name: 'logout' }" v-if="is_login">logout |</router-link>
        <router-link :to="{ name : 'reviewlatest'}">review |</router-link>
        <router-link :to="{ name: 'profile-item', params:{ userName: username() } }" v-if="is_login">profile |</router-link>
      </div>
    <i class="fa fa-thumbs-up" aria-hidden="true"></i>
      <div style="display:flex;">
        <md-autocomplete v-model="search_value" :md-options="movies"
        style="width:80%; margin-left: auto; margin-right: auto;">
        <label>Serach</label>
        </md-autocomplete>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      movies : [],
      search_value : ''
    }
  },
  methods: {
    username() {
      return localStorage.getItem('username')
    },
    saveMovies() {
      this.$axios({
        method: 'get',
        url: `${this.$API_URL}/movies/popular/`,
        // headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`},
      })
        .then((res) => {
          const movies = res.data
          this.$store.dispatch('moviesStore/saveMovies', movies)
        })
        .catch((err) => {
          console.log(err.response.data)
        })
    },
    popularMovies() {
      this.$axios({
        method:'get',
        url: `${this.$API_URL}/movies/popular/`,
        // headers: {
        //   Authorization: `Bearer ${localStorage.getItem('jwt')}`
        // }
      })
        .then((res) => {
          this.movies = res.data.slice(0,500).map(element => Object.values(element)[1])
          // console.log(res.data.map(element => Object.values(element)[1]))

        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  computed: {
    is_login() {
      return this.$store.state.accountsStore.is_login
    },
  },
  created() {
    this.$store.dispatch('accountsStore/login')
    this.saveMovies()
    this.popularMovies()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

@import url("https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900");

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: "Poppins", sans-serif;
}

.content {
	position: relative;
}

.content h2 {
	color: #fff;
	font-size: 7em;
	position: absolute;
	transform: translate(-50%, -50%);
}

.content h2:nth-child(1) {
	color: transparent;
	-webkit-text-stroke: 2px #8338ec;
}

.content h2:nth-child(2) {
	color: #c19bf5;
	animation: animate 4s ease-in-out infinite;
}

@keyframes animate {
	0%,
	100% {
		clip-path: polygon(
			0% 45%,
			16% 44%,
			33% 50%,
			54% 60%,
			70% 61%,
			84% 59%,
			100% 52%,
			100% 100%,
			0% 100%
		);
	}

	50% {
		clip-path: polygon(
			0% 60%,
			15% 65%,
			34% 66%,
			51% 62%,
			67% 50%,
			84% 45%,
			100% 46%,
			100% 100%,
			0% 100%
		);
	}
}

</style>
