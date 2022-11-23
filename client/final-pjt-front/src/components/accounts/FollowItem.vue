<template>
  <div class="d-flex justify-content-between my-2 p-2 follow-item">
    <div class="d-flex justify-content-start">
      <div @click="goToProfile" class="pointer">
        <img :src="profile_img" alt="..." class="rounded-circle mr-3" style="width: 50px; height: 50px">
      </div>
      <div @click="goToProfile">
        <div class="d-flex justify-content-start align-items-end pointer">
          <div>{{ followItem.username }}</div>
        </div>
        <div style="font-size: 0.7em;">
          {{ followItem.introduce }}
        </div>
      </div>
    </div>
    <div>
      <button @click="follow">{{ is_follow }}</button>
    </div>

    
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
    goToProfile() {
      this.$router.push({ name: 'profile-item', params: { userName: this.followItem.username } })
    }
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

<style scoped>
.follow-item:hover {
  background-color: #DBCDCF;
  transition: background-color 0.35s;
  
  border-radius: 1rem;
}
.pointer{
  cursor : pointer;
}
</style>