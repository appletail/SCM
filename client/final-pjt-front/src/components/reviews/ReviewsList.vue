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

        <md-table-pagination
          :md-page-size="rowsPerPage"
          :md-page-options="[3, 5, 10, 15]"
          :md-update="updatePagination"
          :md-data.sync="users"
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
    this.updatePagination(1, this.rowsPerPage)
  },
  methods: {
    updatePagination (page, pageSize, sort, sortOrder) {
        console.log('pagination has updated', page, pageSize, sort, sortOrder);
        // Example of response - in case the service goes down.
        // {"page":1,"per_page":5,"total":12,"total_pages":3,"data":[{"id":1,"first_name":"George","last_name":"Bluth","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"},{"id":2,"first_name":"Janet","last_name":"Weaver","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"},{"id":3,"first_name":"Emma","last_name":"Wong","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg"},{"id":4,"first_name":"Eve","last_name":"Holt","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg"},{"id":5,"first_name":"Charles","last_name":"Morris","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/stephenmoon/128.jpg"}]}
        this.$http.get(`https://reqres.in/api/users?page=${page}&per_page=${pageSize}`).then(({data: resp}) => {
          this.rowsPerPage = resp.per_page
          this.users = {
            mdCount: resp.total,
            mdPage: resp.page,
            mdData: resp.data
          }
        })
    }
  }

    
  
}
</script>

<style>
</style>



