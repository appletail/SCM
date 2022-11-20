import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import ProfileUpdateView from '@/views/accounts/ProfileUpdateView.vue'
import FollowerView from '@/views/accounts/FollowerView.vue'
import FollowingView from '@/views/accounts/FollowingView.vue'

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
  {
    path: '/:userName/follower/',
    name: 'profile-follower',
    component: FollowerView,
    props: true
  },
  {
    path: '/:userName/following/',
    name: 'profile-following',
    component: FollowingView,
    props: true
  },
]
