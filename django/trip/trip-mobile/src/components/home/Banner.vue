<template>
<!-- 首页的轮播图 -->
  <div class="home-banner-box">
    <van-swipe class="my-swipe" :autoplay="3000" indicator-color="white">
      <van-swipe-item v-for="item in bannerList"
        :key="item.id">
        <img :src="item.img_url" alt="">
      </van-swipe-item>
    </van-swipe>
  </div>
</template>
<script>
import { ajax } from '@/utils/ajax'
import { SystemApis } from '@/utils/apis'
export default {
  data () {
    return {
      bannerList: []
    }
  },
  methods: {
    /**
     * 获取轮播图的数据
     */
    getDataList () {
      ajax.get(SystemApis.sliderListUrl).then(res => {
        console.log('res:', res)
        this.bannerList = res.data.objects
      })
    }
  },
  created () {
    // 从接口获取数据
    this.getDataList()
  }
}
</script>
<style lang="less">
.home-banner-box {
  img {
    width: 100%;
    height: auto;
  }
}
</style>
