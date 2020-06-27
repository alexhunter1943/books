<template>
    <b-container>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">嗨小说</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item v-for="item in headData.headers" :key="item.id" :href="item.url" :class="item.url == now_url ? 'active':''">{{ item.text }}</b-nav-item>
            
          </b-navbar-nav>

          <ul  class="navbar-nav ml-auto">
            <li  class="form-inline">
              <div  class="form-inline">
                <input v-model="search.key" type="text" placeholder="输入图书名字或者作者名字" class="mr-sm-2 form-control form-control-sm" >
                <button @click="onSearch" type="submit" class="btn my-2 my-sm-0 btn-secondary btn-sm">开始查询</button>
              </div>
            </li>
          </ul>
        </b-collapse>
      </b-navbar>
    </b-container>
</template>

<script>
import { GetCates } from "../apis/read.js";
import { reactive, ref, onMounted } from "@vue/composition-api";  // ref 定义常量; reactive：定义对象
import { stripscript } from "../apis/validate.js";

export default {
    name:"Header",
    setup(props, context){ // setup相当与beforecreate、created; props：来自爸爸的爱（父组件传入的内容）;context：当前组件拥有的内容
      const now_url = ref(context.root.$route.path);

      const headData = reactive({
        headers:[]
      });
      GetCates().then(reponse =>{
        console.log("In Header reponse = ", reponse.data.data);
        headData.headers = reponse.data.data;
        console.log("headData.headers = ", headData.headers)
      });

      onMounted(()=>{
        console.log("in Header search.key = ", search.key);
      });

      const search = reactive({
        key:''
      });

      const onSearch = () =>{
          console.log("in Header search.key = ", search.key);
          if(stripscript(search.key) == false || search.key == ''){
            alert("您输入的信息有误，请确认后重新输入");
          }else{
            context.root.$router.push({
              path: '/search',
              query:{
                q:search.key
              }
            });
          }

      }

      return {
        headData,
        now_url,
        search,
        onSearch
      }

    }
}
</script>

<style lang="scss" scoped> // lang告诉解释其css符合什么编译器的语法; scoped：当前vue文件生效，没有scoped则全局生效

</style>