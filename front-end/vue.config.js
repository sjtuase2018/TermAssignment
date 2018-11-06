'use strict'
// Template version: 1.1.3
// see http://vuejs-templates.github.io/webpack for documentation.

const path = require('path')



module.exports = {
    /** 区分打包环境与开发环境
     * process.env.NODE_ENV==='production'  (打包环境)
     * process.env.NODE_ENV==='development' (开发环境)
     * baseUrl: process.env.NODE_ENV==='production'?"https://cdn.didabisai.com/front/":'front/',
     */
    // 基本路径
    baseUrl: '/',
    // 输出文件目录
    outputDir: path.resolve(__dirname, '../dist'), // 构建输出目录
    assetsDir: 'static', // 静态资源目录 (js, css, img, fonts
    // eslint-loader 是否在保存的时候检查

    //联调is wrong
    // proxyTable: {
    //     '/api': {
    //         target: '127.0.0.1:5000',  // 真实请求的地址
    //         changeOrigin: true,  // 是否跨域
    //     }
    // }
 
}