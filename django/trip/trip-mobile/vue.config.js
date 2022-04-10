
// Node.js里面的模块
module.exports = {
  // http://localhost:8080/api/test
  // =>
  // http://localhost:8000/test

  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
        pathRewrite: { 
          '^/api': ''   //需要rewrite重写的URL
        }
      }
    }
  }
}