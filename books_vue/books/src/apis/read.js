import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa.js";


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
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos') // 预留字段给加密用
        }
    })
}