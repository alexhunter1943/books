<template>
    <div id="BookIndex">
        <Header />
        <b-container>
            <b-row>
                <b-col md="4"> <!-- 放图片 -->
                    <b-img thumbnail fluid src="https://picsum.photos/250/250/?image=54" alt="Image 1"></b-img>
                </b-col>
                <b-col md="8"> <!-- 放图书信息 -->
                    <b-jumbotron header-level="0">
                        <template v-slot:header>{{ items.indexItems[0].book_name }}</template>

                        <div>作者：{{ items.indexItems[0].book_author }}</div>
                        <div>最新章节：{{ items.indexItems[0].book_newest_name }}</div>
                        <div>最新更新时间：{{ dateFormat(items.indexItems[0].book_last_update_time) }}</div>
                        <div>本书状态：{{ items.indexItems[0].book_status }}</div>

                        

                        <hr class="my-4">

                        <p>
                        小说简介：This is a simple hero unit, a simple jumbotron-style component for calling extra attention to
                        featured content or information.
                        </p>


                        <b-button pill variant="primary" class="left"  style="float:left; margin-left:5px" href="#">开始阅读</b-button>
                        <b-button pill variant="success" class="right" style="float:right; margin-right:5px"  href="#">加入收藏夹</b-button>
                    </b-jumbotron>
                </b-col>
            </b-row>
            {{ items.indexItems }}
        </b-container>
       <Footer />
    </div>
</template>

<style lang="scss" scoped>

</style>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import { GetInfoPost } from "../apis/read.js";
import { reactive, ref, onMounted } from "@vue/composition-api";
import dateFormat from "../utils/date.js";
 
export default {
    name:'BookIndex',
    components:{
        Header,
        Footer
    },
    setup(props, context){
        const now_url = ref(context.root.$route.path)
        

        const indexParams = reactive({
            url: now_url.value,
            key: 'index'
        });

        const cap20Params = reactive({
            url: now_url.value,
            key: 'cap20'
        });

        const capAllParams = reactive({
            url: now_url.value,
            key: 'all'
        });      
        
        const items = reactive({
            indexItems:[]
        })

        GetInfoPost(indexParams).then(resp =>{
            console.log("In bookindex resp.data = ", resp.data)
            items.indexItems = resp.data.data

        })
        // .then(error=>{
        //     axios
        // });

        onMounted(()=>{
            console.log("context.root.$router.path = ", context.root.$route.path)
        });

        return {
            items,
            dateFormat
        }
    }

}


</script>