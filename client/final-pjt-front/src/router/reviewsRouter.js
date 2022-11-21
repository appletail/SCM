import ReviewsLatestView from '@/views/reviews/ReviewsLatestView.vue'
import ReviewsPopularView from '@/views/reviews/ReviewsPopularView.vue'
import ReviewsViewsView from '@/views/reviews/ReviewsViewsView.vue'
import ReviewsView from '@/views/reviews/ReviewsView.vue'
import ReviewCreateView from '@/views/reviews/ReviewCreateView.vue'
import ReviewDetailView from '@/views/reviews/ReviewDetailView.vue'
import ReviewUpdateView from '@/views/reviews/ReviewUpdateView.vue'

export default [
  {
    path: '/reviews',
    name: 'review',
    component: ReviewsView,
    children: [
      {
        path: '/reviews/latest',
        name: 'reviewlatest',
        component: ReviewsLatestView
      },
      {
        path: '/reviews/popular',
        name: 'reviewpopular',
        component: ReviewsPopularView
      },
      {
        path: '/reviews/view',
        name: 'reviewview',
        component: ReviewsViewsView
      },
    ]
  },
  {
    path: '/reviews/create',
    name: 'reviewcreateview',
    component: ReviewCreateView
  },
  {
    path: '/reviews/:id/update',
    name: 'updateview',
    component: ReviewUpdateView
  },
  {
    path: '/reviews/:id/',
    name: 'detailview',
    component: ReviewDetailView
  },

]
