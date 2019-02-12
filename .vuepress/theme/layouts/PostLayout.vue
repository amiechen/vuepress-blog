<template>
  <div class="flex flex-col h-full">
    <Nav/>
    <article class="flex-1 mx-auto leading-normal container">
      <h2>{{$page.frontmatter.title}}</h2>
      <label class="text-grey-dark">
        <span>{{$page.readingTime.text}}</span> •
        <span>{{formateDate($page.frontmatter.date)}}</span>
      </label>

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