<template>
  <div id="app">
    <el-button type="primary" @click="test">主要按钮</el-button>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  sockets: {
    connect () {
      const id = this.$socket.client.id
      console.log(id + ' connected!')
    }
  },
  methods: {
    test () {
      this.$socket.client.emit('message', 'whoami')
    }
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
