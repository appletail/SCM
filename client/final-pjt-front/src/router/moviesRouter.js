import MovieListBaseView from '@/views/movies/MovieListBaseView.vue'
import MovieListItemsView from '@/views/movies/MovieListItemsView.vue'


export default [

  {
    path: '/movies/:movieListName/',
    component: MovieListBaseView,
    children: [
      {
        path: '',
        name: 'MovieListItems',
        component: MovieListItemsView,
        props: true
      },
    ]
  },

]
