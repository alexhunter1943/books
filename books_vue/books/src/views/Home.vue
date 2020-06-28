<template>
  <div class="home">
    <Header />

    <b-container>
      <div style="height:1000px;background-color:red">
        body部分
        </div>
      </b-container>


    <Footer />


  </div>


</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import { GetInfoPost } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";


export default {
  name: "Home",
  components: {
    Header,
    Footer
  },
  setup(props, context){

    const titlePramas = reactive({
      url: '/title',
      key: 'index'
    });



    GetInfoPost(titlePramas).then(resp => {
      console.log("In Home title = ", resp.data.data);
      document.title = resp.data.data[0];
      document.querySelector('meta[name="keywords"]').setAttribute("content", resp.data.data[1]);
      document.querySelector('meta[name="description"]').setAttribute("content", resp.data.data[2]);
    });


    // document.title = '风华绝代的alexhunter';
    // document.querySelector('meta[name="keywords"]').setAttribute("content", "风华绝代的keywords");
    // document.querySelector('meta[name="description"]').setAttribute("content", "风华绝代的description");
    

    

    onMounted(()=>{
      console.log(context.root.$route.path)
    });
  }

};
</script>