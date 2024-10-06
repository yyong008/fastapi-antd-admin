import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "FastAPI Antd Admin",
  description: "A VitePress Site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'FastAPI', link: '/fastapi/intro' },
      { text: 'React', link: '/react/intro' },
      { text: 'Pydantic', link: '/pydantic/intro' },
      { text: 'SQLAlchemy', link: '/sqlachemly/intro' },
    ],

    sidebar: [
      {
        text: 'FastAPI Antd Admin',
        items: [
          { text: '简介', link: '/intro' },
        ]
      },
      {
        text: 'FastAPI',
        items: [
          { text: '简介', link: '/fastapi/intro' },
          { text: '分层', link: '/fastapi/layer' },
          { text: 'app', link: '/fastapi/app' },
          { text: 'inner', link: '/fastapi/inner' },
        ]
      },
      {
        text: 'Pydantic',
        items: [
          { text: '简介', link: '/pydantic/intro' },
        ]
      },
      {
        text: 'SQLAlchemy',
        items: [
          { text: '简介', link: '/sqlachemly/intro' },
          { text: '导入', link: '/sqlachemly/import' },
          { text: '异步', link: '/sqlachemly/async' },
        ]
      },
      {
        text: 'React',
        items: [
          { text: 'intro', link: '/react/intro' },
          { text: 'antd', link: '/react/antd/intro' },
          { text: 'tailwindcss', link: '/react/tailwindcss/intro' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
