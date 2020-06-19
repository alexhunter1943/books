<template>
    <b-container>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">嗨小说</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item v-for="item in headData.headers" :key="item.id" :href="item.url">{{ item.text }}</b-nav-item>
            
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="输入图书名字或者作者名字"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">开始查询</b-button>
            </b-nav-form>

          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </b-container>
</template>

<script>
import { GetCates } from "../apis/read.js";
import { reactive, ref } from "@vue/composition-api";  // ref 定义常量; reactive：定义对象

export default {
    name:"Header",
    setup(props, context){ // setup相当与beforecreate、created; props：来自爸爸的爱（父组件传入的内容）;context：当前组件拥有的内容

      const headData = reactive({
        headers:[]
      });
      GetCates().then(reponse =>{
        console.log("In Header reponse = ", reponse.data.data);
        headData.headers = reponse.data.data;
        console.log("headData.headers = ", headData.headers)
      });

      return {
        headData
      }

    }
}
</script>

<style lang="scss" scoped> // lang告诉解释其css符合什么编译器的语法; scoped：当前vue文件生效，没有scoped则全局生效

</style>