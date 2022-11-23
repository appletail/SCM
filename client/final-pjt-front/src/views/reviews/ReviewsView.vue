<template>
  <div class='p-5 back'>
    <nav>
      <router-link :to="{ name: 'reviewcreateview' }">[CREATE]</router-link>
    </nav>
    <md-tabs class="md-accent">
      <md-tab id="tab-home" md-label="최신순" @click="reviewLatestList"></md-tab>
      <md-tab id="tab-pages" md-label="인기순" @click="reviewPopularList"></md-tab>
      <md-tab id="tab-posts" md-label="조회순" @click="reviewViewList"></md-tab>

    </md-tabs>
    <router-view/>
  </div>
</template>

<script>


export default {
  name: 'reviewsView',
  methods : {
    reviewLatestList() {
    this.$router.push({ name: 'reviewlatest' })
    },
    reviewPopularList() {
    this.$router.push({ name: 'reviewpopular' })
    },
    reviewViewList() {
    this.$router.push({ name: 'reviewview' })
    },
    
  }
}
</script>

<style scoped>
  /* .back {
    background-image: url("https://image.tmdb.org/t/p/w500//bQXAqRx2Fgc46uCVWgoPz5L5Dtr.jpg");
    background-size: cover;
  } */

  .test {
    background-color : black;
  }
</style>
