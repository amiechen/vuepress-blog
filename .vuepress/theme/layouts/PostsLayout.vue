<template>
  <div class="flex flex-col h-full">
    <Nav/>
    <ul class="flex-1 max-w-xl mx-auto leading-normal">
      <li v-for="post in posts">
        <router-link :to="post.path">{{ post.title }}</router-link>
      </li>
    </ul>
    <Footer class="pin-b"/>
  </div>
</template>

<script>
import Nav from "@theme/components/Nav";
import Footer from "@theme/components/Footer";
export default {
  components: { Nav, Footer },
  name: "Layout",
  computed: {
    posts() {
      return this.$site.pages
        .filter(x => x.path.startsWith("/blog/") && !x.frontmatter.blog_index)
        .sort(
          (a, b) => new Date(b.frontmatter.date) - new Date(a.frontmatter.date)
        );
    }
  }
};
</script>

<style lang="stylus">
@import '../styles/theme.styl';
</style>