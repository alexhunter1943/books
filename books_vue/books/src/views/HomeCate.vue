<template>
<div id="HomeCate">
    <Header />
    <b-container class="mt-4 mb-2">
        <div v-if="items.newestItems.length == 0">
            您要查询的分类页面不存在哦
        </div>
        <div v-else>
            <b-row>
                <b-col cols="12" md="7">
                        <h4>最新更新的小说</h4>
                        <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover" ><!----><!---->
                            <thead role="rowgroup" class=""><!---->
                            <tr role="row" class="">
                                <th role="columnheader" scope="col" aria-colindex="1" class=""><div>小说</div></th>
                                <th role="columnheader" scope="col" aria-colindex="2" class=""><div>最新章节</div></th>
                                <th role="columnheader" scope="col" aria-colindex="3" class=""><div>更新时间</div></th></tr>
                            </thead>
                            <tbody role="rowgroup"><!---->
                                <tr role="row" v-for="item in items.newestItems" :key="item.id">
                                <td aria-colindex="1" role="cell" class=""><a :href="'/book/'+ item.book_id">{{ item.book_name }}</a></td>
                                <td aria-colindex="2" role="cell" class=""><a :href="'/book/'+ item.book_id + '/'+ item.book_newest_url">{{ item.book_newest_name }}</a></td>
                                <td aria-colindex="3" role="cell" class="">{{ dateFormat(item.book_last_update_time) }}</td></tr>
                                
                            </tbody><!---->
                        </table>
                </b-col>
                <b-col cols="12" md="1">
                </b-col>
                <b-col cols="12" md="4">
                        <h4>最多阅读的小说</h4>
                        <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover" ><!----><!---->
                            <thead role="rowgroup" class=""><!---->
                            <tr role="row" class="">
                                <th role="columnheader" scope="col" aria-colindex="1" class=""><div>小说</div></th>
                                <th role="columnheader" scope="col" aria-colindex="2" class=""><div>作者</div></th>
                                </tr>
                            </thead>
                            <tbody role="rowgroup"><!---->
                                <tr role="row" v-for="item in items.mostItems" :key="item.id">
                                <td aria-colindex="1" role="cell" class=""><a :href="'/book/'+ item.book_id">{{ item.book_name }}</a></td>
                                <td aria-colindex="2" role="cell" class=""><a :href="'/book/'+ item.book_id + '/'+ item.book_newest_url">{{ item.book_author }}</a></td>
                                
                                </tr>
                                
                            </tbody><!---->
                        </table>
                </b-col>
            </b-row>
            </div>
    </b-container>
    <Footer />
</div>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { GetInfoPost } from "../apis/read.js";
import dateFormat from "../utils/date.js";

export default {
    name:"HomeCate",
    components:{
        Header,
        Footer
    },

    setup(props, context){
        const now_url = ref(context.root.$route.path);

        const newstParams = reactive({
            url: now_url.value,
            key: 'newest'
        });


        const mostParams = reactive({
            url: now_url.value,
            key: 'most'
        });

        const items = reactive({
            newestItems:[],
            mostItems:[]
        });

        GetInfoPost(newstParams).then(resp => {
            // console.log("resp.data.data", resp.data.data);
            items.newestItems = resp.data.data
        });

        GetInfoPost(mostParams).then(resp => {
            console.log("most : resp.data.data", resp.data.data);
            items.mostItems = resp.data.data
        });



        onMounted(()=>{
            console.log("In HomeCate now_url = ", now_url);
            console.log("In HomeCate now_url.value = ", now_url.value)
        });

        return {
            items,
            dateFormat
        }
    }
    
}
</script>

<style lang="scss" scoped>

</style>