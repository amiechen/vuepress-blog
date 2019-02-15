<template>
  <header>
    <nav
      class="font-sans bg-white text-center flex justify-between my-4 mx-auto container overflow-hidden"
    >
      <router-link
        :to="'/'"
        class="block text-left no-underline font-bold text-black uppercase"
      >{{$site.title}}</router-link>
      <ul class="text-sm text-grey-dark list-reset flex items-center">
        <li v-for="item in $site.themeConfig.nav">
          <router-link
            :to="item.link"
            class="inline-block py-2 px-3 text-grey-darkest hover:text-grey-dark no-underline"
          >{{item.text}}</router-link>
        </li>
      </ul>
    </nav>
  </header>
</template>
