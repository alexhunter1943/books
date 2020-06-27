import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import HomeCate from "../views/HomeCate.vue";
import BookIndex from "../views/BookIndex.vue";
import BookDetail from "../views/BookDetail.vue";
import BookSearch from "../views/BookSearch.vue"

Vue.use(VueRouter);

const routes = [
  { // 网站首页
    path: "/",
    name: "Home",
    component: Home
  },

  // 搜索结果页面
  {
    path: "/search",
    name: "BookSearch",
    component: BookSearch
  },

  // 网站分类页面 search
  {
    path: "/:cate_id",
    name:"HomeCate",
    component: HomeCate
  },

  // 图书首页
  {
    path: "/book/:book_id",
    name: "BookIndex",
    component: BookIndex,
  },

  // 图书详情页
  {
    path: "/book/:book_id/:sort_id",
    name: "BookDetail",
    component: BookDetail
  },



  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
