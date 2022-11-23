<template>
  <div>
    <router-link :to="{ name : 'MovieListItems', params: { movieListName: 'popular' } }">popular |</router-link>
    <router-link :to="{ name : 'MovieListItems', params: { movieListName: 'latest' } }">latest |</router-link>
    <!-- <router-link :to="{ name : 'MovieListItems', params: { movieListName: 'genre' } }">movies |</router-link> -->
    <router-link :to="{ name : 'MovieListItems', params: { movieListName: 'personal' } }">personal |</router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'MovieListBaseView'
}
</script>

<style>

</style>