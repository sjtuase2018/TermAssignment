<template>
  <v-container>
    <div class="player">
      <!-- <v-btn @click="getImg()"/> -->
      <img style="-webkit-user-select: none;" src="http://localhost:5000/api/video_feed/?camid=1" width="1037" height="583">
    </div>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    components: {

    },
    data() {
      return {
        imgUrl: '',
        id: 1
      }
    },
    created() {
      this.getImg();
    },
    methods: {
      
      getImg() {
        const config = { headers: { 'Content-Type': 'multipart/x-mixed-replace; boundary=frame' } };
        console.log('getimg ')
        const path = `http://localhost:5000/api/video_feed/?camid=1`;
        axios.get(path, config).then(response => {
          console.log(response)
        })
      }
    }
  

  }
</script>