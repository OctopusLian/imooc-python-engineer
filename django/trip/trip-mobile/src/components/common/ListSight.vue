<template>
  <a href="#" class="sight-item">
    <img src="/static/home/hot/h1.jpg" alt="">
    <div class="right">
      <h5>{{ item.name }}</h5>
      <van-rate v-model="item.score" readonly/>
      <div class="tips">4人点评 | 100%满意</div>
      <div class="tips light">广东-广州</div>
      <div class="line-price">￥ {{ item.price }} 起</div>
    </div>
  </a>
</template>
<script>
export default {
  props: ['item']
}
</script>
<style lang="less">
// 景点列表
.sight-item {
  display: flex;
  margin-top: 10px;
  border-bottom: 1px solid #f6f6f6;
  img {
    width: 100px;
    height: 100px;
  }
  .right {
    text-align: left;
    flex-grow: 1;
    text-align: left;
    justify-content: left;
    padding-left: 5px;
    position: relative;
  }
  h5 {
    color: #212121;
    font-size: 14px;
    padding: 5px 0;
    margin: 0;
  }
  .line-price {
    position: absolute;
    right: 10px;
    top: 20px;
    display: inline-block;
    color: #f50;
    font-size: 16px;
    font-weight: bold;
  }
  .tips {
    font-size: 12px;
    color: #666;
    &.light {
      color: #999;
    }
  }
}
</style>
