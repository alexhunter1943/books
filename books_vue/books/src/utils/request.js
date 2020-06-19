import axios from "axios";

// console.log("in request.js", process.env.NODE_ENV);

// console.log("in request.js", process.env.VUE_APP_URL);

// axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? '' : '/api';  //关键代码
const BASEURL = process.env.NODE_ENV === "production" ? "" : "/api";
// console.log("in request.js: BASEURL = ", BASEURL);

// 创建axios
const service = axios.create({
  baseURL: BASEURL,
  timeout: 1800000
});

// 请求拦截器： 在浏览器发送请求之前的处理; 用处：对真的发送请求之前可以判断，比如是否合法，是否符合请求参数的要求
service.interceptors.request.use(
  function(config) {
    console.log("request.js: request:  config===== ", config);
    return config;
  },
  function(error) {
    return Promise.reject(error);
  }
);

// 响应拦截器： 服务器返回数据后处理
service.interceptors.response.use(
  function(response) {
    console.log("request.js: response = ", response);
    let data = response.data;
    if (data.resCode != 0) {
      // 服务器有响应，但是并不是想要的数据
      // Message.error(data.message);
      console.log("服务器有响应，但是并不是想要的数据");
      return Promise.reject(data.resCode);
    } else {
      // 服务器有响应，并且数据正确
      console.log("服务器有响应，并且数据正确");
      console.log("request.js: data.data = ", data.data);
      return response;
    }

    // return response;
  },
  function(error) {
    // 服务器没有响应 404,405
    return Promise.reject(error);
  }
);

// 对外暴露接口
export default service;
