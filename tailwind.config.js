/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  theme: {
    colors: {
      'primary': '#1c84ee',
      'secondary': ' #74788d',

       'success': '#34c38f',
      'info': '#16daf1',
      'warning': '#ffcc5a',
       'danger': '#ef6767',
       'purple': '#6f42c1',

       'light': '#f6f6f6',
       'dark': '#2b3940',

       'white': '#fff',
       'black': '#000',

       inherit: colors.inherit,
       current: colors.current,
       transparent: colors.transparent,
       black: colors.black,
       white: colors.white,
       slate: colors.slate,
       gray: colors.gray,
       zinc: colors.zinc,
       neutral: colors.neutral,
       stone: colors.stone,
       red: colors.red,
       orange: colors.orange,
       amber: colors.amber,
       yellow: colors.yellow,
       lime: colors.lime,
       green: colors.green,
       emerald: colors.emerald,
       teal: colors.teal,
       cyan: colors.cyan,
       sky: colors.sky,
       blue: colors.blue,
       indigo: colors.indigo,
       violet: colors.violet,
       purple: colors.purple,
       fuchsia: colors.fuchsia,
       pink: colors.pink,
       rose: colors.rose,
    },
    extend: {},
  },
  plugins: [],
  extend: {
    screens: {
      'xs': '400px',
      'ssm': '576px',

      // 'bootstrap-md': '768px',
      // 'bootstrap-lg': '992px',
      // 'bootstrap-xl': '1200px',
      // 'bootstrap-xxl': '1400px'

      // sm	640px	
      // md	768px
      // lg	1024px
      // xl	1280px
      // 2xl	1536px
    }
  }
}