<template>
  <md-table-row @click="reviewDetail" style="cursor: pointer;">
    <md-table-cell md-numeric>{{review.title}}</md-table-cell>
    <md-table-cell md-numeric>{{review.movie.title}}</md-table-cell>
    <md-table-cell md-numeric>{{review.username}}</md-table-cell>
    <md-table-cell md-numeric>{{review1_created_at}}</md-table-cell>
    <md-table-cell md-numeric>{{review.Lookup_cnt}}</md-table-cell>
  </md-table-row>
</template>

<script>
export default {
  name:'ReviewsListItem',
  props: {
    review:Object,
  },
  data() {
    return {
      review1_created_at : this.review.created_at.substr(0,10),
      movie : null,
    }
  },
  created() {
  },
  methods: {
    reviewDetail() {
      this.$router.push({ name: 'detailview', params: { id: this.review.id } })
    },
    
  }
}
</script>

<style>

</style>