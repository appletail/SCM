import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import ProfileUpdateView from '@/views/accounts/ProfileUpdateView.vue'
import FollowView from '@/views/accounts/FollowView.vue'


export default [
  {
    path: '/accounts/login/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/accounts/logout/',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/accounts/:userName/',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/accounts/:userName/update/',
    name: 'profile-update',
    component: ProfileUpdateView,
    props: true
  },
  {
    path: '/accounts/:userName/:follow/',
    name: 'profile-follow',
    component: FollowView,
    props: true
  },
]
