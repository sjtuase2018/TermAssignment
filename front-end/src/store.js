import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    camera: 1
  },
  mutations: {
    changeCamera(state, cameraid) {
      state.camera = cameraid;
    }
  },
  actions: {

  }
})
