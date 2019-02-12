<template>
  <div class="flex flex-col h-full">
    <Nav/>
    <ul class="flex-1 container mx-auto leading-normal">
      <router-link
        :to="post.path"
        v-for="post in posts"
        :key="post.frontmatter.date"
        class="max-w-md w-full lg:flex mb-8 block mx-auto no-underline shadow-lg"
      >
        <div
          class="h-48 lg:h-auto lg:w-48 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden"
          style="background-image: url('https://source.unsplash.com/user/iamrbn/daily')"
          title="Random Photo"
        ></div>
        <div
          class="border-r border-b border-l border-grey-light lg:border-l-0 lg:border-t lg:border-grey-light bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal"
        >
          <div class="mb-8">
            <div class="text-black font-bold text-xl mb-2">{{post.title}}</div>
            <p class="text-grey-darker text-base" v-html="post.excerpt"></p>
          </div>
          <div class="flex items-center">
            <div class="text-sm">
              <p class="text-grey-dark">{{formateDate(post.frontmatter.date)}}</p>
            </div>
          </div>
        </div>
      </router-link>
    </ul>
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
  },
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