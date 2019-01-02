<template>
  <div id="root" dark>
    
      <router-view/>
  </div>
</template>

<script>

export default {
  name: "App",
  created () {
            document.title = "智能人形识别系统";
        },
  data: () => ({
      drawer: true,
      items: [
      {
        icon: 'account_circle',
        href: '#',
        title: 'Profile',
        click: (e) => {
          console.log(e);
        }
      },
      {
        icon: 'settings',
        href: '#',
        title: 'Settings',
        click: (e) => {
          console.log(e);
        }
      },
      {
        icon: 'fullscreen_exit',
        href: '#',
        title: 'Logout',
        click: (e) => {
          window.getApp.$emit('APP_LOGOUT');
        }
      }
    ],
    }),
    props: {
      source: String
    },
    components: {
      
    },
    methods: {

    }  
}
</script>
