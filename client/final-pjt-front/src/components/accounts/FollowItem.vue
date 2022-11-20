<template>
  <div>
    {{ followItem.username }}
    {{ followItem.nickname }}
    {{ followItem.introduce }}
    <button @click="follow">{{ is_follow }}</button>
  </div>
</template>

<script>
export default {
  name: 'FollowItem',
  props: {
    followItem: Array,
  },
  data() {
    return {
      is_follow: null,
    }
  },
  methods: {
    follow() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/accounts/${this.followItem.username}/follow/`,
        headers: {Authorization: `Bearer ${localStorage.getItem('jwt')}`,}
      })
        .then((res) => {
          this.is_follow = res.data.message
        })
        .catch((err) => {
          alert(err.response.data.message)
        })
    },
  },
  created() {
    this.is_follow = this.followItem.is_follow
  }
}
</script>

<style>

</style>