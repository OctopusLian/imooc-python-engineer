import axios from 'axios'

export const ajax = axios.create({
  headers: {
    source: 'h5',
    icode: 'acbd',
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  withCredentials: true
})
ajax.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  console.log('请求拦截到了')
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error)
})

ajax.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  console.log('响应拦截到了')
  return response
}, function (error) {
  // 对响应错误做点什么
  if (error.response) {
    if (error.response.status === 401) {
      window.alert('未登录，即将跳转到登录页面')
    } else if (error.response.status === 500) {
      window.alert('服务器正忙，请稍后重试')
    }
  }
  return Promise.reject(error)
})
