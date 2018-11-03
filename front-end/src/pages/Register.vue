<template>
  <div id="login">
    <v-app id="inspire">
      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                <v-toolbar dark color="primary">
                  <v-toolbar-title>Register</v-toolbar-title>

                </v-toolbar>
                <v-card-text>
                  <v-form>
                    <v-text-field prepend-icon="person" name="login" label="Login" id="username" type="text" v-model="username"></v-text-field>
                    <v-text-field prepend-icon="lock" name="password" label="Password" id="password" type="password" v-model="password"></v-text-field>
                    <v-text-field prepend-icon="lock" name="repassword" label="rePassword" id="repassword" type="password" v-model="repassword"></v-text-field>
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <!-- <v-btn color="primary" @click="register" :loading="loading">Regi</v-btn> -->
                  <router-link to='/login'><p>&nbsp;&nbsp;go to login?</p></router-link>
                  <v-spacer></v-spacer>
                  
                  <v-btn color="primary" @click="register" :loading="loading">Register</v-btn>
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
      loading: false,
      username: '',
      password: '',
      repassword: '',
      hello: ''
    }),

    methods: {
      register() {
        this.loading = true;
        if (this.password != this.repassword) {
            alert('密码不一致！')
            return 0;
        }
        const path = `http://localhost:5000/api/register/`;
        axios.post(path, {
            username: this.username,
            password: this.password
          }).then(response => {
            console.log(response.data)
            this.hello = response.data.hello
            if (parseInt(response.data.code) === 200){
              this.$router.push('/login')              
            }
          })
          .catch(error => {
            console.log(error)
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