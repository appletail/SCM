<template>
  <div>
    <!-- <p>
      {{review}}
    </p> -->
    <router-link :to="{ name: 'detailview', params: { id: review.id } }">
      {{review}}
    </router-link>
    <!-- {{review.user}} -->
  </div>
</template>

<script>
export default {
  name:'ReviewsListItem',
  props: {
    review:Object,
  }
}
</script>

<style>

</style>