<template>
  <div >
    <router-link
      @click.native="lookup"
     :to="{ name: 'detailview', params: { id: review.id } } ">
      {{review}}
    </router-link>
  </div>
</template>

<script>
export default {
  name:'ReviewsListItem',
  props: {
    review:Object,
  },
  methods: {
  }
}
</script>

<style>

</style>