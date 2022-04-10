<template>
  <!-- 热门景点 -->
  <div class="home-hot-box">
    <!-- 顶上导航 -->
    <van-cell
      title="热门推荐"
      icon="/static/home/hot/fire.png"
      is-link
      title-style="text-align:left"
      value="全部榜单" />
    <!-- // 顶上导航 -->
    <!-- 景点列表 -->
    <div class="box-main">
      <a href="#" class="hot-item"
        v-for="item in dataList"
        :key="item.id">
        <div class="img">
          <span></span>
          <img :src="item.img" alt="">
        </div>
        <h5 class="van-ellipsis">{{ item.name }}</h5>
        <div class="line-price">
          <span class="price">￥{{ item.price }}</span>起
        </div>
      </a>
    </div>
    <!-- //景点列表 -->
  </div>
</template>
<script>
export default {
  data () {
    return {
      dataList: []
    }
  },
  created () {
    this.dataList = [
      {id: 1, img: '/static/home/hot/h1.jpg', name: '景点名称', price: 65},
      {id: 2, img: '/static/home/hot/h2.jpg', name: '景点名称景点名称', price: 65},
      {id: 3, img: '/static/home/hot/h3.jpg', name: '景点名称', price: 65},
      {id: 4, img: '/static/home/hot/h4.jpg', name: '景点名称', price: 65},
      {id: 5, img: '/static/home/hot/h5.jpg', name: '景点名称景点名称', price: 65},
      {id: 6, img: '/static/home/hot/h6.jpg', name: '景点名称', price: 65},
      {id: 7, img: '/static/home/hot/h7.jpg', name: '景点名称景点名称景点名称', price: 65},
      {id: 8, img: '/static/home/hot/h8.jpg', name: '景点名称', price: 65},
      {id: 9, img: '/static/home/hot/h9.jpg', name: '景点名称', price: 65},
      {id: 10, img: '/static/home/hot/h10.jpg', name: '景点名称', price: 65}
    ]
  }
}
</script>
<style lang="less">
.home-hot-box {
  padding: 0 10px;
  .van-cell {
    padding: 10px 0;
  }
  .box-main{
    width: 100%;
    display: flex;
    padding-top: 10px;
    overflow-x: scroll;
  }
  .hot-item {
    display: flex;
    flex-direction: column;
    width: 100px;
    margin-right: 10px;
    padding-bottom: 10px;

    .img {
      position: relative;

      span {
        position: absolute;
        left: 0;
        top: 0;
        display: inline-block;
        width: 42px;
        height: 20px;
        z-index: 10;
      }

      img {
        width: 100px;
        height: 100px;
      }
    }

    h5 {
      color: #212121;
      padding: 2px 0;
      font-size: 12px;
      margin: 0;
    }

    .line-price {
      color: #212121;
      font-size: 12px;
      .price {
        color: #f50;
        font-size: 13px;
      }
    }
    &:nth-child(1) .img span {
      background: url(/static/home/hot/top1.png) no-repeat;
      background-size: 100% auto;
    }
    &:nth-child(2) .img span {
      background: url(/static/home/hot/top2.png) no-repeat;
      background-size: 100% auto;
    }
    &:nth-child(3) .img span {
      background: url(/static/home/hot/top3.png) no-repeat;
      background-size: 100% auto;
    }
  }
}
</style>
