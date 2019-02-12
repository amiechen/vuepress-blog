<template>
  <div class="flex flex-col h-full">
    <Nav/>
    <article class="flex-1 mx-auto leading-normal container">
      <label class="text-grey-dark">{{$page.readingTime.text}}</label>
      <label class="text-grey-dark">{{formateDate($page.frontmatter.date)}}</label>
      <Content/>
    </article>
    <Footer class="pin-b"/>
  </div>
</template>

<script>
import moment from "moment";
import Nav from "@theme/components/Nav";
import Footer from "@theme/components/Footer";
export default {
  components: { Nav, Footer },
  name: "Layout",
  methods: {
    formateDate(date) {
      return moment(date).format("MMM Do YYYY");
    }
  }
};
</script>

<style lang="stylus">
@import '../styles/theme.styl';
</style>