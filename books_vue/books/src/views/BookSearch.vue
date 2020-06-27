<template>
<div id="BookSearch">
    <Header />

    <b-container class="mt-4">
        <b-row><b-col><h4>查询结果</h4></b-col></b-row>
        <b-row>
            <b-col v-if="searhResult.items.length > 0">
                <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover" id="__BVID__6249"><!----><!---->
                    <thead role="rowgroup" class=""><!---->
                        <tr role="row" class="">
                            <th role="columnheader" scope="col" aria-colindex="1" class=""><div>图书名字</div></th>
                            <th role="columnheader" scope="col" aria-colindex="2" class=""><div>作者</div></th>
                            <th role="columnheader" scope="col" aria-colindex="3" class=""><div>最新章节</div></th>
                        </tr>
                    </thead>
                    <tbody role="rowgroup"><!---->
                        <tr role="row" v-for="item in searhResult.items" :key="item.id">
                            <td aria-colindex="1" role="cell" class=""><a :href="'/book/'+item.book_id">{{ item.book_name }}</a></td>
                            <td aria-colindex="2" role="cell" class=""><a :href="'/book/'+item.book_id">{{ item.book_author }}</a></td>
                            <td aria-colindex="3" role="cell" class=""><a :href="'/book/'+item.book_id+'/'+item.book_newest_url">{{ item.book_newest_name }}</a></td>
                        </tr>
                        
                    </tbody><!---->
                </table>
            </b-col>
            <b-col v-else>
                您要查询的图书不存在，请您确认后，重新查询哦
            </b-col>
        </b-row>
    </b-container>

    <Footer />

</div>
    
</template>

<style lang="scss" scoped>

</style>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import { reactive } from '@vue/composition-api';
import { GetInfoPost } from "../apis/read.js";

export default {
  name: "BookSearch",
  components: {
    Header,
    Footer
  },

  setup(props, context){
      const searchParma = reactive({
          url: "/search",
          key: context.root.$route.query.q  // context.root = this
      });

      const searhResult = reactive({
          items:[]
      })
      GetInfoPost(searchParma).then(resp => {
          console.log("in Search resp.data.data = ", resp.data.data);
          searhResult.items = resp.data.data
      });

      return {
          searhResult
      }
  }
};
</script>