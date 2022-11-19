import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import ProfileUpdateView from '@/views/accounts/ProfileUpdateView.vue'

export default [
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/:userName',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/:userName/update/',
    name: 'profile-update',
    component: ProfileUpdateView,
    props: true
  },
]
