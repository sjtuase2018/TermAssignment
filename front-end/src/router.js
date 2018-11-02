import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
  base: '/',
  mode: 'hash',
  //linkActiveClass: 'active',
  routes: [
    {
      path: '*',
      meta: {
        public: true,
      },
      redirect: {
        path: '/404'
      }
    },  
    {
      path: '/404',
      meta: {
        public: true,
      },
      name: 'NotFound',
      component: () => import(
        /* webpackChunkName: "routes" */
        /* webpackMode: "lazy-once" */
        `@/pages/NotFound.vue`
      )
    },
    {
      path: '/',
      meta: { },
      name: 'home',
      redirect: {
        name: 'Login'
      }
    },
    {
      path: '/register',
      meta: {
        public: true,
      },
      name: 'Register',
      component: () => import(
        /* webpackChunkName: "routes" */
        /* webpackMode: "lazy-once" */
        `@/pages/Register.vue`
      )
    },
    {
      path: '/login',
      meta: {
        public: true,
      },
      name: 'Login',
      component: () => import(
        /* webpackChunkName: "routes" */
        /* webpackMode: "lazy-once" */
        `@/pages/Login.vue`
      )
    },
    {
      path: '/manage',
      component: () => import(
        /* webpackChunkName: "routes" */
        /* webpackMode: "lazy-once" */
        `@/pages/Manage.vue`
      ),
      name: 'Manage',
      children: [
        {
          path: '/realTime',
          meta: {
            public: true,
          },
          name: 'RealTime',
          component: () => import(
            /* webpackChunkName: "routes" */
            /* webpackMode: "lazy-once" */
            `@/pages/RealTime.vue`
          )
        },
        {
          path: '/chart',
          meta: {
            public: true,
          },
          name: 'Chart',
          component: () => import(
            /* webpackChunkName: "routes" */
            /* webpackMode: "lazy-once" */
            `@/pages/Chart.vue`
          )
        },
        {
          path: '/logs',
          meta: {
            public: true,
          },
          name: 'Logs',
          component: () => import(
            /* webpackChunkName: "routes" */
            /* webpackMode: "lazy-once" */
            `@/pages/Logs.vue`
          )
        },
        {
          path: '/setting',
          meta: {
            public: true,
          },
          name: 'Setting',
          component: () => import(
            /* webpackChunkName: "routes" */
            /* webpackMode: "lazy-once" */
            `@/pages/Setting.vue`
          )
        },
        {
          path: '/profile',
          meta: {
            public: true,
          },
          name: 'Profile',
          component: () => import(
            /* webpackChunkName: "routes" */
            /* webpackMode: "lazy-once" */
            `@/pages/Profile.vue`
          )
        },
      ]
    },
  ]
})
