import { TanStackRouterVite } from "@tanstack/router-plugin/vite";
import dayjs from "dayjs";
import { defineConfig } from "vite";
import path from "path";
import pkg from "./package.json";
import react from "@vitejs/plugin-react-swc";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), TanStackRouterVite()],
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
        target: "http://localhost:8003",
        changeOrigin: true,
        followRedirects: true, // 确保代理会跟随重定向
        // rewrite: (path) => path.replace(/^\/api/, "/api")
      },
    },
  },
});
