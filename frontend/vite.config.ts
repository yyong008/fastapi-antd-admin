import path from "path";
import dayjs from "dayjs";
import pkg from "./package.json";
import { defineConfig } from "vite-plus";
import react from "@vitejs/plugin-react";
import { tanstackRouter } from "@tanstack/router-plugin/vite";

// https://vitejs.dev/config/
export default defineConfig({
  lint: {},
  fmt: {
    singleQuote: false,
    trailingComma: "es5",
    printWidth: 80,
    tabWidth: 2,
    sortPackageJson: false,
    ignorePatterns: ["node_modules", "dist"],
  },
  plugins: [react(), tanstackRouter()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  define: {
    __APP_INFO__: JSON.stringify({
      pkg,
      lastBuildTime: dayjs().format("YYYY-MM-DD HH:mm:ss"),
    }),
  },
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
        followRedirects: true, // 确保代理会跟随重定向
        // rewrite: (path) => path.replace(/^\/api/, "/api")
      },
      "/static": {
        target: "http://localhost:8000",
        changeOrigin: true,
        followRedirects: true, // 确保代理会跟随重定向
        rewrite: (path) => path.replace(/^\/static/, "/static"),
      },
    },
  },
});
