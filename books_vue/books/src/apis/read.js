import service from "../utils/request.js";


export function GetCates(){
    return service.request({
        method: "get",
        url: "/books_cates"
    });
};

export function GetInfoPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            key: postParams.key, // newest 
            secretKey: '大家好，我是secretKey' // 预留字段给加密用
        }
    })
}