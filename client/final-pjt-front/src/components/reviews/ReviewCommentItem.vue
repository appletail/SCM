<template>
  <div>
    {{comment}}
    <button>DELETE</button>
  </div>
</template>

<script>
export default {
  name : 'ReviewCommentItem',
  props :{
    comment : Object,
  },
  method: {
  }
}
</script>

<style>

</style>