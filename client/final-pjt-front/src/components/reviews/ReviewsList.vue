<template>
  <div>
    <!-- <h3>Review List</h3> -->
    <div>
      <md-table>
        <md-table-row>
          <md-table-head md-numeric>제목</md-table-head>
          <md-table-head md-numeric>영화 제목</md-table-head>
          <md-table-head md-numeric>작성자</md-table-head>
          <md-table-head md-numeric>작성일자</md-table-head>
          <md-table-head md-numeric>조회수</md-table-head>
        </md-table-row>
        <ReviewsListItem
          v-for="review in reviews"
          :key="review.id"
          :review="review"
        />

      </md-table>
    </div>
  </div>
</template>

<script>
import ReviewsListItem from '@/components/reviews/ReviewsListItem.vue'

export default {
  name: 'ReviewsList',
  components : {
    ReviewsListItem,
  },
  props: {
    reviews: Array,
  },
  data() {
    return {
        users: {
        mdCount: null,
        mdPage: null,
        mdData: []
      },
      rowsPerPage: 3,
    }
  },
  created() {
  },
  methods: {
  }

    
  
}
</script>

<style>
</style>



