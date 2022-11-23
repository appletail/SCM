<template>
 <div class="col imgbox m-1">
    <div>
      <img :src="movie.img_url" :alt="movie.title">
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing:border-box;
}
img {
  width: 80%;
  height: 100%;
  object-fit:cover;
  
  -webkit-box-reflect:below 2px linear-gradient(transparent, transparent, #0004);
  
  transform-origin:center;
  transform:perspective(800px) rotateY(25deg);
  transition:0.5s;
}
.imgbox {
  max-width:600px;
  max-height:350px;
  
  
  
  display:flex;
  justify-content:center;
  align-items:center;
  gap:20px;
  
}
.imgbox:hover img {
  opacity:0.3;
}
.imgbox img:hover {
  transform:perspective(800px)       rotateY(0deg);
  opacity:1;
}
</style>