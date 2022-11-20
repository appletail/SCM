<template>
  <div>
    <h1>follower page</h1>
    <p>{{ followers }}</p>
    <FollowItems/>
  </div>
</template>

<script>
import FollowItems from '@/components/accounts/FollowItems'

export default {
  name: 'FollowerView',
  components: {
    FollowItems,
  },
  props: {
    followers: Array,
  },
  data() {
    return {

    }
  },
  methods: {
    follow() {

    },
  }
}
</script>

<style>

</style>