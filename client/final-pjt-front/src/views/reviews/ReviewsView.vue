<template>
  <div>
    <nav>
      <router-link :to="{ name: 'reviewlatest' }">최신순</router-link> | 
      <router-link :to="{ name: 'reviewpopular' }">인기순</router-link> | 
      <router-link :to="{ name: 'reviewview' }">조회순</router-link> |
      <router-link :to="{ name: 'reviewcreateview' }">[CREATE]</router-link>
    
    </nav>
    <router-view/>
  </div>
</template>

<script>


export default {
  name: 'reviewsView',
}
</script>

<style>

</style>
