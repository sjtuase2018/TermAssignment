<template>
  <v-container class="container">
    <div>
      <div class="player">
        <v-layout row wrap>
          <v-flex>
            <!-- <div  v-if="cameras.length>0"> -->
            <swiper v-if="cameras.length>0" :options="swiperOptionTop" class="gallery-top" ref="swiperTop">
              
              <swiper-slide v-for="(camera, index) in cameras" :key="index" class="slide-1">
                <img class="videoImg" :src="imgUrl+camera">
              </swiper-slide>
              <!-- <swiper-slide class="slide-1">
                <img class="videoImg" src="http://localhost:5000/api/video_feed/?cameraId=1">
              </swiper-slide>
              <swiper-slide class="slide-2">

              </swiper-slide>
              <swiper-slide class="slide-3"></swiper-slide>
              <swiper-slide class="slide-4"></swiper-slide>
              <swiper-slide class="slide-5"></swiper-slide> -->
              <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
              <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>
            </swiper>
            
            <!-- swiper2 Thumbs -->
            
            <swiper v-if="cameras.length>0" :options="swiperOptionThumbs" class="gallery-thumbs" ref="swiperThumbs">
              <!-- <swiper-slide v-for="camera in cameras" class="slide-1"> -->
              <swiper-slide v-for="(camera, index) in cameras" :key="index" :style="{ backgroundImage: 'url(' + backgroundImg[index] + ')' }">
                <v-btn fab small class="switch" v-bind:color="green[index]" @click="modelSwitch(camera, index)">
                  {{index+1}}
                </v-btn> 
              </swiper-slide>
              <!-- <swiper-slide class="slide-1">
                <v-btn fab small class="switch" v-bind:color="green[0]" @click="modelSwitch(1)">1

                </v-btn>
              </swiper-slide>
              <swiper-slide class="slide-2">
                <v-btn fab small class="switch" v-bind:color="green[1]" @click="modelSwitch(2)">2
                  
                </v-btn>
              </swiper-slide>
              <swiper-slide class="slide-3">
                <v-btn fab small class="switch" v-bind:color="green[2]" @click="modelSwitch(3)">3
                 
                </v-btn>
              </swiper-slide>
              <swiper-slide class="slide-4">
                <v-btn fab small class="switch" v-bind:color="green[3]" @click="modelSwitch(4)">4
                  
                </v-btn>
              </swiper-slide>
              <swiper-slide class="slide-5">
                <v-btn fab small class="switch" v-bind:color="green[4]" @click="modelSwitch(5)">5
                  
                </v-btn>
              </swiper-slide> -->
            </swiper>
            <!-- </div> -->
          </v-flex>
        </v-layout>
      </div>
      
      
      <!-- <img style="-webkit-user-select: none;" src="http://localhost:5000/api/video_feed/?camid=1" width="1037" height="583"> -->
    </div>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import 'swiper/dist/css/swiper.css'
  import {
    swiper,
    swiperSlide
  } from 'vue-awesome-swiper'

  export default {
    components: {
      swiper,
      swiperSlide
    },
    data() {
      return {
        imgUrl: 'http://localhost:5000/api/video_feed/?cameraId=',
        backgroundImg: ['http://localhost:83/2018/2/20/pic0.jpg',
        'http://localhost:83/2018/2/20/pic0.jpg',
        'http://localhost:83/2018/2/20/pic24.jpg',
        'http://localhost:83/2018/2/20/pic48.jpg',
        'http://localhost:83/2018/2/20/pic48.jpg',
        'http://localhost:83/2018/2/20/pic48.jpg',
        'http://localhost:83/2018/2/20/pic48.jpg',
        'http://localhost:83/2018/2/20/pic96.jpg',
        'http://localhost:83/2018/2/20/pic48.jpg',        
        'http://localhost:83/2018/2/20/pic48.jpg'],
        id: 1,
        model: '',
        cameras: [],
        desserts: [],
        cameraOn: [],
        green: ['','','','',''],
        swiperOptionTop: {
          spaceBetween: 10,
          loop: true,
          centeredSlides: true,
          loopedSlides: 5, //looped slides should be the same
          navigation: { 
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        swiperOptionThumbs: {
          spaceBetween: 10,
          slidesPerView: 4,
          touchRatio: 0.2,
          loop: true,
          loopedSlides: 5, //looped slides should be the same
          slideToClickedSlide: true,
        }
      }
    },
    mounted() {
      
      this.$nextTick(() => {
        const swiperTop = this.$refs.swiperTop.swiper
        const swiperThumbs = this.$refs.swiperThumbs.swiper

        swiperTop.controller.control = swiperThumbs
        swiperThumbs.controller.control = swiperTop
      })
    },
    created() {
      this.getCamera();
      // this.swiperOptionTop.loopedSlides = this.desserts.length;
      // this.swiperOptionThumbs.loopedSlides = this.desserts.length;
      const path = `http://localhost:5000/api/deactive/`;
      axios.post(path, {
          cameraId: 0
        }).then(response => {
          this.cameraOn = response.data.cameraOn;
          for (var i = 0; i < 5; i++) {
            if(this.cameraOn[i]) {
              this.$set(this.green, i , "green");
              // this.green[i] = 'green';
            } else {
              this.$set(this.green, i , "");
              // this.green[i] = 'dark';
            }
          }
          const swiperTop = this.$refs.swiperTop.swiper
        const swiperThumbs = this.$refs.swiperThumbs.swiper

        swiperTop.controller.control = swiperThumbs
        swiperThumbs.controller.control = swiperTop
          console.log(this.green);
          
        })
    },
    methods: {
      modelSwitch(cameraId, index) {
        // window.open("http://localhost:8080/#/detector","_blank","toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width=100, height=100, top=450");
        // let windowObj = window.open()
        // windowObj.location = 'http://localhost:8080/#/realTime' //弹出一个你要打开的页面
        //在你弹出的那个页面关那个页面使用：
        // window.close()
        //在当前页面关闭刚才弹出的页面使用：
        // windowObj.close()
        // window.opener = null;
        // window.open("http://localhost:8080/#/profile");
        // window.close();
        // this.model = '检测中'
        console.log('getimg ')
        console.log(cameraId);
        const path = `http://localhost:5000/api/deactive/`;
        axios.post(path, {
          cameraId: cameraId,
          index: index
        }).then(response => {
          this.$store.commit('changeCamera', cameraId);
          const url = "http://localhost:5000/#/detector?cameraId=" + cameraId;
          let windowObj = window.open(url,"_blank","toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width=100, height=100, top=450");
          console.log(response)
          console.log(windowObj);
          // windowObj.close();
          console.log(windowObj.closed);
          if (windowObj.closed) {
            this.$set(this.green, cameraId , "");
          }
          this.cameraOn = response.data.cameraOn;
          for (var i = 0; i < this.cameraOn.length; i++) {
            if(this.cameraOn[i]) {
              this.$set(this.green, i , "green");
              // this.green[i] = 'green';
            } else {
              this.$set(this.green, i , "");
              // this.green[i] = 'dark';
            }
          }
          console.log(this.green);
          
        })
      },
      getCamera() {
        const path = `http://localhost:5000/api/getCamera/`;
        axios.get(path, {

          }).then(response => {
            // console.log(response.data)
            this.desserts = response.data
            console.log(this.desserts)
            this.desserts.forEach(element => {
              this.cameras.push(element.id);
              // this.cameraOn.push(false);
              console.log(this.cameras);
            });
            const swiperTop = this.$refs.swiperTop.swiper
        const swiperThumbs = this.$refs.swiperThumbs.swiper

        swiperTop.controller.control = swiperThumbs
        swiperThumbs.controller.control = swiperTop
          })
          .catch(error => {
            console.log(error)
          })
      },
      getImg() {
        const config = {
          headers: {
            'Content-Type': 'multipart/x-mixed-replace; boundary=frame'
          }
        };
        console.log('getimg ')
        const path = `http://localhost:5000/api/video_feed/?camid=1`;
        axios.get(path, config).then(response => {
          console.log(response)
        })
      },

      // player is ready
      playerReadied(player) {
        // seek to 10s
        console.log('example player 1 readied', player)
        player.currentTime(10)
        // console.log('example 01: the player is readied', player)
      }
    }


  }
</script>

<style lang="scss" scoped>
  .swiper-container {
    background-color: #000;
  }

  .swiper-slide {
    background-size: cover;
    background-position: center;

    &.slide-1 {
      background-image: url('http://localhost:83/2018/2/20/pic48.jpg');
      // background-image: url();
      // height: 600px;
      // width: 800px;
    }

    &.slide-2 {
      background-image: url('https://surmon-china.github.io/vue-quill-editor/static/images/surmon-2.jpg');
    }

    &.slide-3 {
      background-image: url('https://surmon-china.github.io/vue-quill-editor/static/images/surmon-3.jpg');
    }

    &.slide-4 {
      background-image: url('https://surmon-china.github.io/vue-quill-editor/static/images/surmon-4.jpg');
    }

    &.slide-5 {
      background-image: url('https://surmon-china.github.io/vue-quill-editor/static/images/surmon-5.jpg');
    }
  }

  .gallery-top {
    height: 80% !important;
    width: 100%;
  }

  .gallery-thumbs {
    height: 20% !important;
    box-sizing: border-box;
    padding: 10px 0;
  }

  .gallery-thumbs .swiper-slide {
    width: 25%;
    height: 100%;
    opacity: 0.4;
  }

  .gallery-thumbs .swiper-slide-active {
    opacity: 1;
  }

  .videoImg {
    width: 100%;
    height: 100%;
  }

  .player {
    position: relative;
    z-index: 1;

  }

  .container {
    width: 800px;
    position: relative;
    z-index: 1;
  }

  .switch {
    z-index: 10000;
  }

  .green {
    color: green;
  }
</style>