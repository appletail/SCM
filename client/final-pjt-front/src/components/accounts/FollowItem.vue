<template>
  <div class="d-flex justify-content-between">
    <div class="d-flex justify-content-start">
      <span>
        <img :src="profile_img" alt="프로필 사진" style="width: 50px; height: 50px">
      </span>
      <span>
        <div>
          <span>{{ followItem.username }}</span>
          <span style="font-size: 0.7em;" class="text-blueGray-600 ml-2">{{ followItem.nickname }}</span>
        </div>
        <div style="font-size: 0.7em;">
          {{ followItem.introduce }}
        </div>
      </span>
    </div>
    <span>
      <button @click="follow">{{ is_follow }}</button>
    </span>

    
  </div>
</template>

<script>
export default {
  name: 'FollowItem',
  props: {
    followItem: Object,
  },
  data() {
    return {
      is_follow: null,
      profile_img: null,
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
    if (this.followItem.profile_img) {
      this.profile_img = `${this.$API_URL}/${this.followItem.profile_img}`
    } else {
      this.profile_img = 'https://media.istockphoto.com/id/826793062/es/foto/foto-vertical-de-agradable-pocos-gatito-blanco-semanas-de-edad-con-manchas-tabby-en-la-cara-el.jpg?s=170667a&w=0&k=20&c=6LvzyI6Txp8Ai9lOpY6vJiSfktWfdSAf9ZqKpiinM5M='
    }
  }
}
</script>

<style>

</style>