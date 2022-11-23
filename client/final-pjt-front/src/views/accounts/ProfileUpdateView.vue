<template>
  <div>
    <h1>회원정보수정</h1>
    <form @submit.prevent="updateProfile">
      <img :src="profile_img_url" alt="프로필 이미지"><br>
      <input type="text" placeholder="닉네임을 입력해주세요" v-model="nickname"><br>
      <input type="password" placeholder="비밀번호" v-model="password"><br>
      <input type="password" placeholder="비밀번호 확인" v-model="password_confirm"><br>
      <textarea cols="30" rows="10" placeholder="자기소개" v-model="introduce"></textarea><br>
      <input type="file" @change="onFileChange"><br>
      <button>회원정보 수정</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ProfileUpdateView',
  data() {
    return {
      profile_img: null,
      profile_img_url: null,
      userName: null,
      nickname: null,
      password: null,
      password_confirm: null,
      introduce: null,
    }
  },
  methods: {
    getProfile(userName) {
      this.$axios({
        method: "get",
        url: `${this.$API_URL}/accounts/${userName}/update/`,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${this.access_token}`,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.profile_img_url = `${this.$API_URL}/${res.data.profile_img}`;
          this.nickname = res.data.nickname;
          this.introduce = res.data.introduce;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateProfile() {
      const formData = new FormData();
      if (this.profile_img) {
        formData.append('profile_img', this.profile_img, this.profile_img.name)
      }
      formData.append('nickname', this.nickname)
      formData.append('password', this.password)
      formData.append('password_confirm', this.password_confirm)
      formData.append('introduce', this.introduce)

      this.$axios({
        method: 'put',
        url: `${this.$API_URL}/accounts/${this.userName}/update/`,
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `Bearer ${this.access_token}`,
        },
        data: formData
      })
        .then(() => {
          this.$router.push({ name:'profile-item', params:{ userName: this.userName }})
        })
        .catch((err) => {
          console.log(err.response.data)
        })
    },
    onFileChange(event) {
      this.profile_img = event.target.files[0]
      this.profile_img_url = URL.createObjectURL(this.profile_img)
    }
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
    this.getProfile(to.params.userName);
    next();
  },
  created() {
    this.userName = this.$route.params.userName;
    this.getProfile(this.userName);
  }
}
</script>

<style>

</style>