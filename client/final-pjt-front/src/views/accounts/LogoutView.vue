<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'LogoutView',
  data() {
    return {
    }
  },
  created() {
    localStorage.removeItem('jwt')
    localStorage.removeItem('username')
    this.$store.dispatch('accountsStore/login')
    this.$router.push({ name: 'home' })
  }
}
</script>

<style>

</style>