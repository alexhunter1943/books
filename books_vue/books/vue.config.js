const path = require("path");
module.exports = {
  publicPath: "/",
  // 输出文件目录
  outputDir: "dist",
  assetsDir: "assets",
  lintOnSave: false,
  chainWebpack: config => {
    config.resolve.symlinks(true); //热更新
  },
  configureWebpack: config => {
    if (process.env.NODE_ENV === "production") {
      // 为生产环境修改配置...
      config.mode = "production";
      // 将每个依赖包打包成单独的js文件
      let optimization = {
        runtimeChunk: "single",
        splitChunks: {
          chunks: "all",
          maxInitialRequests: Infinity,
          minSize: 20000,
          cacheGroups: {
            vendor: {
              test: /[\\/]node_modules[\\/]/,
              name(module) {
                const packageName = module.context.match(
                  /[\\/]node_modules[\\/](.*?)([\\/]|$)/
                )[1];
                return `npm.${packageName.replace("@", "")}`;
              }
            }
          }
        }
      };
      Object.assign(config, {
        optimization
      });
    } else {
      // 为开发环境修改配置...
      config.mode = "development";
    }
    Object.assign(config, {
      // 开发生产共同配置
      resolve: {
        extensions: [".js", ".vue", ".json"], //请求本地json
        alias: {
          "@": path.resolve(__dirname, "./src"),
          "@c": path.resolve(__dirname, "./src/components"),
          "@p": path.resolve(__dirname, "./src/pages")
        } // 别名配置
      }
    });
  },
  // 生产环境是否生成 sourceMap 文件
  productionSourceMap: true,
  css: {
    // 是否使用css分离插件 ExtractTextPlugin
    extract: true,
    // 开启 CSS source maps?是否在构建样式地图，false将提高构建速度
    sourceMap: false,
    // 如果你想去掉文件名中的.module
    // requireModuleExtension: true,
    // 启用 CSS modules for all css / pre-processor files.
    // modules: false,
    // css预设器配置项
    loaderOptions: {
      sass: {
        // data: '@import "./src/styles/main.scss";'  // 3.0 用这个
        prependData: `@import "./src/styles/main.scss";` // 4.0 用这个
        // 当前是没有这个路径，也没有这个文件的，不要奇怪
        // 我们去创建它
      },
      scss: {
        prependData: `@import "./src/styles/main.scss";`
      }
    }
  },
  parallel: require("os").cpus().length > 1,
  // webpack-dev-server 相关配置
  devServer: {
    open: process.platform === "darwin",
    host: "localhost",
    port: 8081,
    https: false,
    hotOnly: false,
    overlay: {
      warnings: false,
      errors: false
    },
    proxy: {
      "/api": {
        // 目标 API 地址
        target: process.env.VUE_APP_URL,
        // target:'http://127.0.0.1:5000/',
        // 如果要代理 websockets
        // ws: false,
        changeOrigin: true, // 允许websockets跨域
        pathRewrite: {
          // 正则匹配，把到/devapi之前的所有替换成空
          "^/api": ""
        }
      }
    },
    // 代理转发配置，用于调试环境
    disableHostCheck: true
  }
};
