<template class="d-flex justify-content-center alias-item-center">
<div :class="[{ 'right-panel-active': is_panel_active }, 'container', 'sign']" id="container">
	<div class="form-container sign-up-container">
		<form @submit.prevent="signup">
			<h1>Create Account</h1>
			<input type="text" placeholder="username" v-model="signup_username"/>
			<input type="password" placeholder="Password" v-model="signup_password"/>
			<input type="password" placeholder="password confirm" v-model="signup_password_confirm"/>
			<div v-show="signup_err_msg">
				<span class="d-flex justify-content-center align-items-center">
					<svg aria-hidden="true" focusable="false" width="19px" height="19px" viewBox="0 0 24 24" fill="red">
					<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"></path>
					</svg>
					<span style="font-size: 17px">
						{{ signup_err_msg }}
					</span>
				</span>
			</div>
			<button>Sign Up</button>
		</form>
	</div>
	<div class="form-container sign-in-container">
		<form @submit.prevent="login">
			<h1>Sign In</h1>
			<span>아이디와 비밀번호를 입력해주세요</span>
			<input type="text" placeholder="username" v-model="login_username"/>
			<input type="password" placeholder="Password" v-model="login_password"/>
			<div v-show="login_err_msg">
				<span>
					<svg aria-hidden="true" focusable="false" width="16px" height="16px" viewBox="0 0 24 24" fill="red">
					<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"></path>
					</svg>
				</span>{{ login_err_msg }}
			</div>
			
			<button>Sign In</button>
		</form>
	</div>

	<div class="overlay-container">
		<div class="overlay">
			<div class="overlay-panel overlay-left">
				<h1>Welcome Back!</h1>
				<p>다시 돌아와서 반가워요!</p>
				<button class="ghost" id="signIn" @click="panelActive">Sign In</button>
			</div>
			<div class="overlay-panel overlay-right">
				<h1>Hello, Friend!</h1>
				<p>저희와 함께 영화의 세계로 떠나요~</p>
				<button class="ghost" id="signUp" @click="panelActive">Sign Up</button>
			</div>
		</div>
	</div>
</div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      login_username: null,
      login_password: null,
			login_err_msg: null,
      signup_username: '',
      signup_password: '',
      signup_password_confirm: '',
			signup_err_msg: null,
      is_panel_active: false,
    }
  },
  methods: {
    login() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/api/token/`,
        data: {
          username: this.login_username,
          password: this.login_password,
        }
      })
        .then((res)=>{
          localStorage.setItem('jwt', res.data.access)
          localStorage.setItem('refresh', res.data.refresh)
          localStorage.setItem('username', this.login_username)
          this.$store.dispatch('accountsStore/login')
          this.$router.push({ name: 'home' })
        })
        .catch((err) => {
					if (err.response.data.username) {
						this.login_err_msg = '아이디를 입력해주세요.'
					} else if (err.response.data.password) {
						this.login_err_msg = '비밀번호를 입력해주세요.'
					} else {
						this.login_err_msg = '아이디 혹은 비밀번호가 일치하지 않습니다.'
					}
        })
    },
    signup() {
      this.$axios({
        method: 'post',
        url: `${this.$API_URL}/accounts/signup/`,
        data: {
          username: this.signup_username,
          password: this.signup_password,
          password_confirm: this.signup_password_confirm,
        }
      })
        .then(() => {
          this.login_username = this.signup_username
          this.login_password = this.signup_password
          this.login()
        })
        .catch((err) => {
					console.log()
					if (!this.signup_username.trim()) {
						this.signup_err_msg = '아이디를 입력해주세요.'
					} else if (err.response.data.username) {
						this.signup_err_msg = '이미 존재하는 아이디입니다.'
					} else if (!this.signup_password.trim()) {
						this.signup_err_msg = '비밀번호를 입력해주세요.'
					} else if (!this.signup_password_confirm.trim()) {
						this.signup_err_msg = '비밀번호 확인을 입력해주세요.'
					} else if (this.signup_password != this.signup_password_confirm) {
						this.signup_err_msg = '비밀번호가 일치하지 않습니다.'
					}	
        })
    },
  panelActive() {
    this.is_panel_active = !this.is_panel_active
  }
  },

}
</script>

<style scoped>
.o6cuMc{
	color: #590817;
}
.sign{
  color: #040102;
	margin: 10% auto;
}

@import url('https://fonts.googleapis.com/css?family=Montserrat:400,800');

* {
	box-sizing: border-box;
}

h1 {
	font-weight: bold;
	margin: 0;
}

h2 {
	text-align: center;
}

p {
	font-size: 14px;
	font-weight: 100;
	line-height: 20px;
	letter-spacing: 0.5px;
	margin: 20px 0 30px;
}

span {
	font-size: 12px;
}

a {
  color: #333;
  font-size: 14px;
  text-decoration: none;
  margin: 15px 0;
}

button {
	border-radius: 20px;
	border: 1px solid #FF4B2B;
	background-color: #FF4B2B;
	color: #FFFFFF;
	font-size: 12px;
	font-weight: bold;
	padding: 12px 45px;
	letter-spacing: 1px;
	text-transform: uppercase;
	transition: transform 80ms ease-in;
}

button:active {
	transform: scale(0.95);
}

button:focus {
	outline: none;
}

button.ghost {
	background-color: transparent;
	border-color: #FFFFFF;
}

form {
	background-color: #FFFFFF;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 50px;
	height: 100%;
	text-align: center;
}

input {
	background-color: #eee;
	border: none;
	padding: 12px 15px;
	margin: 8px 0;
	width: 100%;
}

.container {
	background-color: #fff;
	border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
			0 10px 10px rgba(0,0,0,0.22);
	position: relative;
	overflow: hidden;
	width: 768px;
	max-width: 100%;
	min-height: 480px;
}

.form-container {
	position: absolute;
	top: 0;
	height: 100%;
	transition: all 0.6s ease-in-out;
}

.sign-in-container {
	left: 0;
	width: 50%;
	z-index: 2;
}

.container.right-panel-active .sign-in-container {
	transform: translateX(100%);
}

.sign-up-container {
	left: 0;
	width: 50%;
	opacity: 0;
	z-index: 1;
}

.container.right-panel-active .sign-up-container {
	transform: translateX(100%);
	opacity: 1;
	z-index: 5;
	animation: show 0.6s;
}

@keyframes show {
	0%, 49.99% {
		opacity: 0;
		z-index: 1;
	}
	
	50%, 100% {
		opacity: 1;
		z-index: 5;
	}
}

.overlay-container {
	position: absolute;
	top: 0;
	left: 50%;
	width: 50%;
	height: 100%;
	overflow: hidden;
	transition: transform 0.6s ease-in-out;
	z-index: 100;
}

.container.right-panel-active .overlay-container{
	transform: translateX(-100%);
}

.overlay {
	background: #FF416C;
	background: -webkit-linear-gradient(to right, #FF4B2B, #FF416C);
	background: linear-gradient(to right, #FF4B2B, #FF416C);
	background-repeat: no-repeat;
	background-size: cover;
	background-position: 0 0;
	color: #FFFFFF;
	position: relative;
	left: -100%;
	height: 100%;
	width: 200%;
    transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}

.container.right-panel-active .overlay {
    transform: translateX(50%);
}

.overlay-panel {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 40px;
	text-align: center;
	top: 0;
	height: 100%;
	width: 50%;
	transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}

.overlay-left {
	transform: translateX(-20%);
}

.container.right-panel-active .overlay-left {
	transform: translateX(0);
}

.overlay-right {
	right: 0;
	transform: translateX(0);
}

.container.right-panel-active .overlay-right {
	transform: translateX(20%);
}

</style>