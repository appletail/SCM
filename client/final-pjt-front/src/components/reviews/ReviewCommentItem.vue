<template>
  <div>
    {{comment}}
    <button @submit.prevent="deleteComment">DELETE</button>
  </div>
</template>

<script>
export default {
  name : 'ReviewCommentItem',
  props :{
    comment : Object,
  },
  method: {
    // deleteComment() {
    //   console.log('여기는 작동합니다.')
    //   this.$emit('delete-comment',this.comment)
      
    // }
  }
}
</script>

<style>

</style>