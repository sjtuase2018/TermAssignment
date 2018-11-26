<template>
  <div id="login">
    <v-app id="inspire">
      <v-content>
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-text>
              <v-alert :value="alertSuccessed" color="success" icon="check_circle" outline>
                注册成功！
              </v-alert>
              <v-alert :value="alertFailure" color="error" icon="warning" outline>
                注册失败！
              </v-alert>
            </v-card-text>
          </v-card>
        </v-dialog>

        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                <v-toolbar dark color="primary">
                  <v-toolbar-title>注册</v-toolbar-title>

                </v-toolbar>
                <v-card-text>
                  <v-form>
                    <v-text-field prepend-icon="person" name="login" label="请输入账号" id="username" type="text" v-model="username"></v-text-field>
                    <v-text-field prepend-icon="lock" name="password" label="请输入密码" id="password" type="password"
                      v-model="password"></v-text-field>
                    <v-text-field prepend-icon="lock" name="repassword" label="请再次输入密码" id="repassword" type="password"
                      v-model="repassword"></v-text-field>
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <!-- <v-btn color="primary" @click="register" :loading="loading">Regi</v-btn> -->
                  <router-link to='/login'>
                    <p>&nbsp;&nbsp;登录?</p>
                  </router-link>
                  <v-spacer></v-spacer>

                  <v-btn color="primary" @click="register" :loading="loading">注册</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'Register',
    props: {
      msg: String
    },
    data: () => ({
      dialog: false,
      alertSuccessed: false,
      alertFailure: false,
      loading: false,
      username: '',
      password: '',
      repassword: '',
      hello: ''
    }),

    methods: {
      register() {
        if (this.username == '') {
          alert('请输入账号！')
          return 0;
        }
        if (this.password == '') {
          alert('请输入密码！')
          return 0;
        }
        if (this.password != this.repassword) {
          alert('密码不一致！')
          return 0;
        }
        this.loading = true;
        const path = `http://localhost:5000/api/register/`;
        axios.post(path, {
            username: this.username,
            password: this.password
          }).then(response => {
            console.log(response.data)
            this.hello = response.data.hello
            if (parseInt(response.data.code) === 200) {
              this.$router.push('/login')
            }
            this.dialog = true;
            this.alertSuccessed = true;
            setTimeout(()=>{
              this.dialog = false
            }, 1000)
          })
          .catch(error => {
            console.log(error)
            this.dialog = true;
            this.alertFailure = true;
            setTimeout(()=>{
              this.dialog = false
            }, 3000)
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h3 {
    margin: 40px 0 0;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>