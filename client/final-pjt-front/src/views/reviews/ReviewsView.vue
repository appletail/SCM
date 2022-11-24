<template>
  <div class='p-5'>
    <nav>
      <router-link :to="{ name: 'reviewcreateview' }" v-if="isLogin">[CREATE]</router-link>
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
  },
  computed: {
    isLogin() {
      return this.$store.state.accountsStore.is_login
    }
  }
}
</script>

<style scoped>
  .test {
    background-color : black;
  }
  .back {
    border-radius: 9rem;
  }
</style>
