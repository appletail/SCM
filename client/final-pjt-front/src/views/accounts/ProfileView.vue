<template>
  <div>
    <h1>This is profile page</h1>

    <p>{{ profile?.username }}</p>
    <p>{{ profile?.nickname }}</p>
    <p>{{ profile?.introduce }}</p>
    <button @click="follow">{{ is_follow }}</button>
    <p>
      <router-link
        :to="{ name: 'profile-follower', 
        params: {
           userName: userName,
           following: profile?.followers
        } }"
      >
      {{ profile?.follower.length }}
        followers |
      </router-link>
      <router-link 
        :to="{ name: 'profile-following', 
        params: {
           userName: userName,
           following: profile?.followings
        } }"
      >
      {{ profile?.following.length }}
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
</template>

<script>
export default {
  name: "ProfileView",
  data() {
    return {
      profile: null,
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
    this.userName = this.$route.params.userName;
    this.getProfile();
  },
};
</script>

<style>
</style>