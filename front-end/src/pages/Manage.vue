<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer v-model="drawer" clipped fixed app>
      <v-list dense>
        <v-list-tile v-for="(item,index) in memus" :to="item.href" @click="item.click" ripple="ripple" :disabled="item.disabled"
          :target="item.target" rel="noopener" :key="index">
          <v-list-tile-action v-if="item.icon">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <router-view />
    </v-content>
    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>智能人形识别系统</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu offset-y origin="center center" :nudge-bottom="10" transition="scale-transition">
        <v-btn icon large flat slot="activator">
          <v-avatar size="30px">
            <v-icon medium>notifications</v-icon>
          </v-avatar>
        </v-btn>
        <v-list class="pa-0">
          <v-list-tile v-for="(item,index) in items" :to="item.href" @click="item.click" ripple="ripple" :disabled="item.disabled"
            :target="item.target" rel="noopener" :key="index">
            <v-list-tile-action v-if="item.icon">
              <v-icon large>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>
    <v-footer app fixed>
      <span>&copy; 2018</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      drawer: true,
      memus: [{
          icon: 'dashboard',
          href: 'realTime',
          title: '实时展示',
          click: (e) => {
            console.log(e);
          }
        },
        {
          icon: 'bar_chart',
          href: 'chart',
          title: '报表分析',
          click: (e) => {
            console.log(e);
          }
        },
        {
          icon: 'data_usage',
          href: 'logs',
          title: '日志',
          click: (e) => {
            console.log(e);
          }
        },
        {
          icon: 'settings',
          href: 'setting',
          title: '设置',
          click: (e) => {
            console.log(e);
          }
        }
      ],
      items: [
        {
          icon: 'fullscreen_exit',
          href: 'login',
          title: '退出',
          click: () => {
            // window.getApp.$emit('APP_LOGOUT');
          }
        }
      ],
    }),
    props: {
      source: String
    },
    methods: {

    }
  }
</script>