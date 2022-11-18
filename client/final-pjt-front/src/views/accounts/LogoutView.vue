<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
    }
  },
  created() {
    localStorage.removeItem('jwt'),
    this.$router.push({ name: 'home' })
  }
}
</script>

<style>

</style>