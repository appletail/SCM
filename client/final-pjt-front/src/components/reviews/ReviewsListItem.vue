<template>
  <div>
    <router-link :to="{ name: 'detailview', params: { id: review.id } }">
      {{review}}
    </router-link>
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