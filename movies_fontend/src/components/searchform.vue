<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>test</h2>
    <el-input v-model="input" placeholder="请输入内容"></el-input>
  </div>
</template>

<script>
export default {
  name: 'test',
  data () {
    return {
      msg: 'test root',
      input: ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
