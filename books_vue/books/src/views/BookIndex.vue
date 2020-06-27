<template>
    <div id="BookIndex">
        <Header />
            <b-container class="mt-4" v-if="items.indexItems.length == 1">
                <b-row class="mb-3">
                    <b-col clos="12" md="4"> <!-- 放图片 -->
                        <b-img thumbnail fluid class="p-3" style="width:80%; margin-left:10%" :src="items.indexItems[0].image_urls" alt="Image 1"></b-img>
                    </b-col>
                    <b-col  clos="12" md="8"> <!-- 放图书信息 -->
                        
                            <b-jumbotron header-level="0" class="pt-3">
                                <template v-slot:header class="mt-1 mb-3">{{ items.indexItems[0].book_name }}</template>

                                <div class="mb-3">作者：{{ items.indexItems[0].book_author }}</div>
                                <div class="mb-3">最新章节：{{ items.indexItems[0].book_newest_name }}</div>
                                <div class="mb-3">最新更新时间：{{ dateFormat(items.indexItems[0].book_last_update_time) }}</div>
                                <div class="mb-3">本书状态：{{ items.indexItems[0].book_status }}</div>

                                

                                <hr class="my-4">

                                <p v-text="items.indexItems[0].book_desc">
                                </p>


                                <b-button pill variant="primary" class="left"  style="float:left; margin-left:5px" :href="'/book/'+items.indexItems[0].book_id+'/'+ items.allCapItems[0].sort_id">开始阅读</b-button>
                                <b-button pill variant="success" class="right" style="float:right; margin-right:5px"  href="#">加入收藏夹</b-button>
                            </b-jumbotron>
                            
                        
                    </b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col class="normal-center"><h4>最近更新的20章图书</h4></b-col> 
                </b-row>
                <b-row class="mb-4">
                    <b-col clos="12" md="4" v-for="item in items.newest20CapItems" :key="item.id"><a :href="'/book/'+item.book_id+'/'+item.sort_id ">{{ item.detail_title }}</a></b-col>
                </b-row>


                <b-row class="mb-2 ">
                    <b-col class="normal-center"><h4>所有章节的内容</h4></b-col>
                </b-row>
                <b-row class="mb-2">
                    <b-col clos="12" md="4" v-for="item in items.allCapItems" :key="item.id"><a :href="'/book/'+item.book_id+'/'+item.sort_id ">{{ item.detail_title }}</a></b-col>
                    
                </b-row>

               
            </b-container>
            <b-container class="mt-4" v-else>
                        哦哦，您要查看的图书不存在
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
// import 的时候什么时候没有{}： export default 出现在最后一行的时候，就没有{}
// 什么时候有{}: export 很多个fanctions的时候，就有{}

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
            indexItems:[],
            allCapItems:[],
            newest20CapItems:[]
        })

        GetInfoPost(indexParams).then(resp =>{
            console.log("In bookindex resp.data = ", resp.data)
            items.indexItems = resp.data.data

        });
        // .then(error=>{
        //     axios
        // });

        GetInfoPost(capAllParams).then(resp =>{
            console.log("In bookindex resp.data = ", resp.data)
            items.allCapItems = resp.data.data

        });

        GetInfoPost(cap20Params).then(resp =>{
            console.log("In bookindex resp.data = ", resp.data)
            items.newest20CapItems = resp.data.data

        });

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