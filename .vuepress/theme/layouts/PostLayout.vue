<template>
  <div class="flex flex-col h-full">
    <Nav/>
    <article class="flex-1 mx-auto leading-normal container">
      <label class="text-grey-dark">{{$page.readingTime.text}}</label>
      <Content/>
    </article>
    <Footer class="pin-b"/>
  </div>
</template>

<script>
import Nav from "@theme/components/Nav";
import Footer from "@theme/components/Footer";
export default {
  components: { Nav, Footer },
  name: "Layout"
};
</script>

<style lang="stylus">
@import '../styles/theme.styl';
</style>