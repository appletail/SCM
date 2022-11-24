import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import ProfileItemView from '@/views/accounts/ProfileItemView.vue'
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
    component: ProfileView,
    children: [
      {
        path: '',
        name: 'profile-item',
        component: ProfileItemView,
        props: true
      },
      {
        path: '/accounts/:userName/:follow/',
        name: 'profile-follow',
        component: FollowView,
        props: true
      },
    ]
  },
  {
    path: '/:userName/update/',
    name: 'profile-update',
    component: ProfileUpdateView,
    props: true
  },
]
