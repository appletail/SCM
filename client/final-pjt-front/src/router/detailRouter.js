import MovieDetailView from '@/views/details/MovieDetailView.vue'
import CrewDetailView from '@/views/details/CrewDetailView.vue'

export default [
  {
    path: '/moviedetail/:id',
    name: 'moviedetail',
    component: MovieDetailView
  },
  {
    path: '/crewdetail/:id',
    name: 'crewdetail',
    component: CrewDetailView
  },

]
