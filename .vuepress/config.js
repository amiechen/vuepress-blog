module.exports = {
  title: "Vuepress Blog Example",
  description: "just another blog",
  themeConfig: {
    nav: [{ text: "Blog", link: "/blog/" }, { text: "About", link: "/" }]
  },
  plugins: ["vuepress-plugin-reading-time"],
  postcss: {
    plugins: [
      require("tailwindcss")("./tailwind.config.js"),
      require("autoprefixer")
    ]
  }
};
