<script src="https://cdnjs.cloudflare.com/ajax/libs/vue/2.5.2/vue.min.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<template>
  <div id="app">
    <appHeader></appHeader>
    <appBody></appBody>
    <appFooter></appFooter>
  </div>
</template>

<script>

import appHeader from './components/Header.vue'
import appBody from './components/Body.vue'
import appFooter from './components/Footer'

export default {
  name: 'app',
  components: {
    appHeader,
    appBody,
    appFooter
  }
}
</script>

<style>

</style>
