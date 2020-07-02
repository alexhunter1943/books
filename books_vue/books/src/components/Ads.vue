<template>
<b-container>
    <div id="main-top-ad">
        <a target="_blank" :href="rowAdsData.data.url"><img id="top-img" :src="rowAdsData.data.img_path"  :alt="rowAdsData.data.alt"/></a>
    </div>
    <div id="main-left-ad">
        <a target="_blank" :href="colAdsData.data[0].url"><img id="left-img" :src="colAdsData.data[0].img_path"  :alt="colAdsData.data[0].alt"/></a>
    </div>
    <div id="main-right-ad">
        <a target="_blank" :href="colAdsData.data[1].url"><img id="right-img" :src="colAdsData.data[1].img_path"  :alt="colAdsData.data[1].alt" /></a>
    </div>
</b-container>
    
</template>

<style lang="scss" scoped>

@media (max-width: 500px) {
    #main-left-ad{
        display: none;
    }  
    
    #main-right-ad{
        display: none;
    }  
    #main-top-ad{
        position: fixed;
        bottom: auto;
        top:0;
        left: 0;
        z-index: 99999;
        right: 0;
    }
}
#top-img{
    width: 100%;
}

#main-left-ad{
    position: fixed;
    bottom: auto;
    top:0;
    width: 150px;
    height: 600px;
    z-index: 99999;
    margin-top: 158px;
    left: 0;
}

#main-right-ad{
    position:fixed;
    bottom: auto;
    top:0;
    width: 150px;
    height: 600px;
    z-index: 99999;
    margin-top: 158px;
    right: 0;
}
</style>

<script>
import { GetInfoPost } from "../apis/read.js";
import { reactive } from '@vue/composition-api';


export default {
    name:"Ads",
    setup(props,context){

        const is_PC = () =>{
            if(document.body.clientWidth < 400){
                return 'phone'
            }else{
                return 'pc'
            }
        }

        const adsPrams = reactive({
            url: '/ads',
            key:is_PC()
        });

        const rowAdsData = reactive({
            data:{}
        });

        GetInfoPost(adsPrams).then(resp =>{
            // console.log("in AAAAAAAAAAAAAAAAAAADS resp.data", resp.data);
            rowAdsData.data = resp.data.data
        });


        const colPramas = reactive({
            url:'/colads',
            key:''
        });

        const colAdsData = reactive({
            data:[]
        });

        GetInfoPost(colPramas).then(resp => {
            console.log("in AAAAAAAAAAAAAAAAAAADS resp.data", resp.data);
            colAdsData.data = resp.data.data
        });


        return{
            rowAdsData,
            colAdsData
        }
    }
}
</script>