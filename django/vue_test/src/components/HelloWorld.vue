<template>
  <div class="hello">
    <h1>组件通信</h1>
    <p>用户名： {{username}}</p>
    <input type="text" v-model="name">
    <input type="button" @click="submit" value="提交">
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  // props: ['username'],
  props: {
    username: {
      type: String,
      required: true,
      default: 'admin'
    }
  },
  data() {
    return {
      name: ''
    }
  },
  methods: {
    submit() {
      this.$emit('myEvent', {name: this.name}) 
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
  li {
    display: inline-block;
    margin: 0 10px;
  }
}
.text-danger {
  color: #f00;
}
.panel {
  background-color: aquamarine;
  padding: 50px;
  p {
    background-color: #fff;
    padding: 20px;
  }
}

</style>
