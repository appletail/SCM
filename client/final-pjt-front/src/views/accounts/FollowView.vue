<template>
  <div>
    <h1>{{ pageName }}</h1>
    <FollowItem
      v-for="followItem in followItems"
      :key="followItem.username"
      :followItem="followItem"
    />
  </div>
</template>

<script>
import FollowItem from '@/components/accounts/FollowItem'

export default {
  name: 'FollowerView',
  components: {
    FollowItem,
  },
  data() {
    return {
      userName: null,
      pageName: null,
      followItems: null,
    }
  },
  methods: {
    follow() {
      this.$axios({
        method: 'get',
        url: `${this.$API_URL}/accounts/${this.userName}/${this.pageName}/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`,},
      })
        .then((res) => {
          this.followItems = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName;
    this.pageName = to.params.follow;
    this.follow()
    next();
  },
  created() {
    this.userName = this.$route.params.userName;
    this.pageName = this.$route.params.follow;
    this.follow()
  },
}
</script>

<style>

</style>