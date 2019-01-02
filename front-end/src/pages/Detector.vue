<template>
    <v-btn @click="modelSwitch()">检测中
    </v-btn>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                cameraId: 0
            }
        },
        created() {
            this.cameraId = this.$store.state.camera;
            // console.log(this.camera);
            this.cameraId = this.$route.query.cameraId;
            // console.log(this.camera);
            const path = `http://localhost:5000/api/active/`;
            axios.post(path, {
                    cameraId: this.cameraId
                })
                .then(response => {
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => {
                    window.close();
                });
            // var cameraId = this.getQueryString('cameraId');
            // console.log(cameraId);
        },
        methods: {
            modelSwitch() {
                console.log(this.$store.state.camera)
            },
            // getQueryString(name) {
            //     let reg = `(^|&)${name}=([^&]*)(&|$)`
            //     let r = window.location.search.substr(1).match(reg);
            //     if (r != null) return unescape(r[2]);
            //     return null;
            // }

        }
    }
</script>