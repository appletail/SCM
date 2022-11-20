import ReviewsLatestView from '@/views/reviews/ReviewsLatestView.vue'
import ReviewsPopularView from '@/views/reviews/ReviewsPopularView.vue'
import ReviewsViewsView from '@/views/reviews/ReviewsViewsView.vue'
import ReviewsView from '@/views/reviews/ReviewsView.vue'
import ReviewCreateView from '@/views/reviews/ReviewCreateView.vue'

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
      {
        path: '/reviews/create',
        name: 'reviewcreateview',
        component: ReviewCreateView
      }
    ]
  },



]
