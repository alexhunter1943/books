import service from "../utils/request.js";


export function GetCates(){
    return service.request({
        method: "get",
        url: "/books_cates"
    });
};