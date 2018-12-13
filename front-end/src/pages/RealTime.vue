<template>
  <v-container>
    <div>
      <div class="player">
        <v-layout row wrap>
          <v-flex>
            <swiper :options="swiperOptionTop" class="gallery-top" ref="swiperTop">
              <swiper-slide class="slide-1">
                <img class="videoImg" src="http://localhost:5000/api/video_feed/">
              </swiper-slide>
              <swiper-slide class="slide-2">

              </swiper-slide>
              <swiper-slide class="slide-3"></swiper-slide>
              <swiper-slide class="slide-4"></swiper-slide>
              <swiper-slide class="slide-5"></swiper-slide>
              <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
              <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>
            </swiper>
            <!-- swiper2 Thumbs -->
            <swiper :options="swiperOptionThumbs" class="gallery-thumbs" ref="swiperThumbs">
              <swiper-slide class="slide-1">1</swiper-slide>
              <swiper-slide class="slide-2">2</swiper-slide>
              <swiper-slide class="slide-3">3</swiper-slide>
              <swiper-slide class="slide-4">4</swiper-slide>
              <swiper-slide class="slide-5">5</swiper-slide>
            </swiper>
          </v-flex>
        </v-layout>
      </div>
      
      <v-btn @click="modelSwitch()"/>
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
        imgUrl: '',
        id: 1,
        model: '',
        swiperOptionTop: {
          spaceBetween: 10,
          loop: true,
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
      setTimeout(() => {
          console.log('dynamic change options', this.player)
          // this.player.muted(false)
        }, 5000),
        this.$nextTick(() => {
          const swiperTop = this.$refs.swiperTop.swiper
          const swiperThumbs = this.$refs.swiperThumbs.swiper
          swiperTop.controller.control = swiperThumbs
          swiperThumbs.controller.control = swiperTop
        })
    },
    created() {
      // this.getImg();
    },
    methods: {
      modelSwitch() {

        console.log('getimg ')
        const path = `http://localhost:5000/api/modelSwitch/`;
        axios.get(path, {
          model: this.model
        }).then(response => {
          console.log(response)
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
      background-image: url('https://surmon-china.github.io/vue-quill-editor/static/images/surmon-1.jpg');
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
</style>