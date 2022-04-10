<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld v-bind:username="username"/>
    <HelloWorld v-on:my-event="dealEvent"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data() {
    return {
      username: '张三'
    }
  },
  methods: {
    dealEvent(data) {
      console.log('从子组件传递过来的数据：', data)
    }
  }
}
</script>
