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
export default {
  name: "Home",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    document.title = '风华绝代的alexhunter';
    document.querySelector('meta[name="keywords"]').setAttribute("content", "风华绝代的keywords");
    document.querySelector('meta[name="description"]').setAttribute("content", "风华绝代的description");
  }

};
</script>