<template>
  <div>
    <link rel="stylesheet" href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css">
    <link rel="stylesheet" href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css">

    <main class="profile-page">
      <section class="relative block h-500-px">
        <div class="absolute top-0 w-full h-full bg-center bg-cover" style="
                background-image: url('https://images.unsplash.com/photo-1499336315816-097655dcfbda?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=2710&amp;q=80');
              ">
        </div>
          <span id="blackOverlay" class="absolute opacity-50 bg-black" style="height: 100%; width: 100%; left:0%;"></span>
        <div class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px" style="transform: translateZ(0px)">
          <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" version="1.1" viewBox="0 0 2560 100" x="0" y="0">
            <polygon class="fill-current" points="2560 0 2560 100 0 100" style="color: rgb(219, 205, 207)"></polygon>
          </svg>
        </div>
      </section>
      <section class="relative py-16">
        <div class="container mx-auto px-4">
          <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64">
            <div class="px-6">
              <div class="flex flex-wrap justify-center">
                <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                  <div class="relative">
                    <router-link
                      :to="{ name: 'profile-item', params:{ userName: profileName } }"
                    >
                      <img alt="프로필 이미지" :src="profile_img" class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px">
                    </router-link>
                  </div>
                </div>
                <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                  <div class="py-6 px-3 mt-32 sm:mt-0">
                    <button class="bg-pink-500 active:bg-pink-600 uppercase text-white font-bold hover:shadow-md shadow text-xs px-4 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150" type="button" v-if="profileName != loginUser" @click="follow">
                      {{ is_follow }}
                    </button>


                    <button class="bg-pink-500 active:bg-pink-600 uppercase text-white font-bold hover:shadow-md shadow text-xs px-4 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150" type="button" v-if="profileName === loginUser" @click="update">
                      프로필 수정
                    </button>

                  </div>
                </div>
                <div class="w-full lg:w-4/12 px-4 lg:order-1">
                  <div class="flex justify-center py-4 lg:pt-4 pt-8">
                    <div class="mr-4 p-3 text-center">
                      <span class="text-xl font-bold block uppercase tracking-wide text-blueGray-600">{{ profile?.followers }}</span><span class="text-sm text-blueGray-400">
                        <router-link
                          :to="{ name: 'profile-follow', 
                          params: {
                            userName: profileName,
                            follow: 'followers',
                          } }"
                        >
                          followers
                        </router-link>
                      </span>
                    </div>
                    <div class="mr-4 p-3 text-center">
                      <span class="text-xl font-bold block uppercase tracking-wide text-blueGray-600">{{ profile?.followings }}</span><span class="text-sm text-blueGray-400">
                        <router-link
                          :to="{ name: 'profile-follow', 
                          params: {
                            userName: profileName,
                            follow: 'followings',
                          } }"
                        >
                          followings
                        </router-link>
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="text-center mt-12">
                <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                  {{ profile?.username }}
                </h3>
                <div class="mb-2 text-blueGray-600 mt-10">
                  <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>자기소개 <br> {{ profile?.introduce }}
                </div>
              </div>
              <div class="mt-3 py-10 border-blueGray-200 text-center">
                <div class="flex flex-wrap justify-center">
                  <div class="w-full px-4">
                    <div class="mb-4 text-lg leading-relaxed text-blueGray-700">
                      <router-view
                        :watchList="profile?.watchlist_movies"
                        :likeMovies="profile?.like_movies"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: "ProfileView",
  data() {
    return {
      profile: null,
      profile_img: require('@/assets/test.png'),
      profileName: null,
      is_follow: null,
    };
  },
  methods: {
    getProfile() {
      this.$axios({
        method: "get",
        url: `${this.$API_URL}/accounts/${this.profileName}`,
        headers: {Authorization: `Bearer ${this.access_token}`,},
      })
        .then((res) => {
          this.profile = res.data;
          this.is_follow = res.data.is_follow
          if (this.profile.profile_img) {
            this.profile_img = `${this.$API_URL}${this.profile.profile_img}`
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    follow() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/accounts/${this.profileName}/follow/`,
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
    update() {
      this.$router.push({ name: 'profile-update', params: { userName: this.loginUser } })
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
    this.profileName = to.params.userName;
    this.getProfile();
    next();
  },
  created() {
    this.profileName = this.$route.params.userName;
    this.getProfile();
  },
};
</script>

<style>
</style>