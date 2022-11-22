<template>
  <div class="d-flex">
    <div class="mx-5">
      <h1>This is profile page</h1>
      <img :src="profile_img" alt="프로필 이미지">
      <p>{{ profile?.username }}</p>
      <p>{{ profile?.nickname }}</p>
      <p>{{ profile?.introduce }}</p>
      <button v-if="userName != loginUser" @click="follow">{{ is_follow }}</button>
      <p>
        <router-link
          :to="{ name: 'profile-follow', 
          params: {
            userName: userName,
            follow: 'followers',
          } }"
        >
        {{ profile?.followers }}
          followers |
        </router-link>
        <router-link 
          :to="{ name: 'profile-follow', 
          params: {
            userName: userName,
            follow: 'followings',
          } }"
        >
        {{ profile?.followings }}
          followings
        </router-link>
      </p>

      <div v-if="loginUser === userName">
        <button @click="deleteUser">회원탈퇴</button>
        <router-link
          :to="{ name: 'profile-update', params: { userName: loginUser } }"
        >
          <button>회원정보수정</button>
        </router-link>
      </div>
    </div>
    <div class="mx-3 d-flex justify-content-center">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileView",
  data() {
    return {
      profile: null,
      profile_img: null,
      userName: null,
      is_follow: null,
    };
  },
  methods: {
    getProfile() {
      this.$axios({
        method: "get",
        url: `${this.$API_URL}/accounts/${this.userName}`,
        headers: {Authorization: `Bearer ${this.access_token}`,},
      })
        .then((res) => {
          this.profile = res.data;
          this.is_follow = res.data.is_follow
          if (this.profile.profile_img) {
            this.profile_img = `${this.$API_URL}/${this.profile.profile_img}`
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteUser() {
      this.$axios({
        method: "DELETE",
        url: `${this.$API_URL}/accounts/${this.userName}`,
        headers: {Authorization: `Bearer ${this.access_token}`,},
        data: {
          username: this.userName,
        },
      })
        .then((res) => {
          console.log(res.data.delete_user);
          console.log("아직 좀 더 작업할 것");
          this.$router.push({ name: "logout" });
        })
        .catch((err) => {
          console.log(err.response.data.faild);
        });
    },
    follow() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/accounts/${this.userName}/follow/`,
        headers: {Authorization: `Bearer ${this.access_token}`,}
      })
        .then((res) => {
          this.is_follow = res.data.message
          this.getProfile()
        })
        .catch((err) => {
          alert(err.response.data.message)
        })
    },
  },
  computed: {
    access_token() {
      return localStorage.getItem("jwt");
    },
    loginUser() {
      return localStorage.getItem("username");
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName;
    this.getProfile();
    next();
  },
  created() {
    this.profile_img = `${this.$API_URL}/media/images/default_profile_img/1.jpg`
    this.userName = this.$route.params.userName;
    this.getProfile();
  },
};
</script>

<style>
</style>