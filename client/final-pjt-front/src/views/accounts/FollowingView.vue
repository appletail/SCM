<template>
  <div>
    <h1>following page</h1>
      <p>{{ followings }}</p>
    <FollowItems/>
  </div>
</template>

<script>
import FollowItems from '@/components/accounts/FollowItems'

export default {
  name: 'FollowingView',
  components: {
    FollowItems,
  },
  props: {
    followings: Array,
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