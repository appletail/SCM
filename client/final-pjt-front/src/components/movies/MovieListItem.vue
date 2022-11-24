<template>
  <div class="card col p-2 m-1">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <div class="image">
      <img :src="movie.img_url"/>
    </div>
    <div class="details" @click="moveMovie(movie)">
      <div class="center">
        <h1>{{ movie.title }}<br><span>{{ movie.release_date }}</span></h1>
        <p>{{ description }}</p>
        <ul>
          <span @click.stop="toggleLikeMovie" style="cursor: pointer;">
            <li v-show="!like"><a><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a></li>
            <li v-show="like"><a><i class="fa fa-thumbs-up" aria-hidden="true"></i></a></li>
          </span>
          <span @click.stop="toogleWatchList" style="cursor: pointer;">
            <li v-show="!watch"><a><i class="fa fa-eye-slash" aria-hidden="true"></i></a></li>
            <li v-show="watch"><a><i class="fa fa-eye" aria-hidden="true"></i></a></li>
          </span>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
    is_watchlist: Boolean,
    is_like: Boolean,
  },
  data() {
    return {
      like: this.is_like,
      watch: this.is_watchlist
    }
  },
  methods: {
    toogleWatchList() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/accounts/watchlist/${this.movie.id}/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`,}
      })
        .then((res) => {
          this.watch = res.data.message
        })
        .catch((err) => {
          console.log(err)
        })
    },
    toggleLikeMovie() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/accounts/likemovie/${this.movie.id}/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`,}
      })
        .then((res) => {
          this.like = res.data.message
        })
        .catch((err) => {
          console.log(err.response.data)
        })
    },
    moveMovie(movie) {
      this.$router.push({ name: 'moviedetail', params: { id: movie.id } })

    }
  },
  computed: {
    description() {
      let res = _.truncate(
        this.movie.description , {
          'length': 65,
          'omission': '...'
        }
      );
      return res
    },
    loginUser() {
      return localStorage.getItem('username')
    }
  },
  created() {
  }
}
</script>

<style scoped>
.card {
  width: 20rem;
  height: 30rem;
}
.card .image {
  width: 100%;
  height: 100%;
  border-radius: 0.3rem;
  overflow: hidden;
}
.card .image img {
  width: 100%;
  transition: .5s;
}
.card:hover .image img {
  opacity: .5;
  transform: translateX(30%);/*100%*/
}
.card .details {
  position: absolute;
  border-start-start-radius: 0.3rem;
  top: 0;
  left: 0;
  width: 70%;/*100%*/
  height: 100%;
  background: #ffc107;
  transition: .5s;
  transform-origin: left;
  transform: perspective(2000px) rotateY(-90deg);
}
.card:hover .details {
  transform: perspective(2000px) rotateY(0deg);
}
.card .details .center {
  padding: 20px;
  text-align: center;
  background: #fff;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.card .details .center h1 {
  margin: 0;
  padding: 0;
  color: #ff3636;
  line-height: 20px;
  font-size: 20px;
  text-transform: uppercase;
}
.card .details .center h1 span {
  font-size: 14px;
  color: #262626;
}
.card .details .center p {
  margin: 10px 0;
  padding: 0;
  color: #262626;
}
.card .details .center ul {
  margin: 10px auto 0;
  padding: 0;
  display: table;
}
.card .details .center ul li {
  list-style: none;
  margin: 0 5px;
  float: left;
}
.card .details .center ul li a {
  display: block;
  background: #262626;
  color: #fff;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  transform: .5s;
}
.card .details .center ul li a:hover {
  background: #ff3636;
}
</style>