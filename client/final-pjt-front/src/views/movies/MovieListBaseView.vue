<template>
<div>
  <div class="d-flex justify-content-start mx-3 my-2">
    <router-link :to="{ name : 'MovieListItems', params: { movieListName: 'popular' } }" class="mx-2">popular</router-link>
    <router-link :to="{ name : 'MovieListItems', params: { movieListName: 'latest' } }" class="mx-2">latest</router-link>
    <router-link :to="{ name : 'MovieListItems', params: { movieListName: 'personal' } }" class="mx-2">personal</router-link>
  </div>
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