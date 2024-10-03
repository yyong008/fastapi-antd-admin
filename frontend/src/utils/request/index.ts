import * as eventTypes from "../event/event-type"

import { UN_AUTH_CODE } from "./httpStatus";
import axios from "axios";
import { eventCenter } from "../event";

const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 50000,
  headers: {
    "Content-Type": "application/json",
  },
});

request.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token"); // 假设你的令牌存储在 localStorage
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 添加响应拦截器
request.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    if (error.response && error.response.status === UN_AUTH_CODE) {
      eventCenter.emit(eventTypes.USER_AUTHORIZED, error.response?.data?.message)
    } else if (error.response.data.code === 1) {
      eventCenter.emit(eventTypes.DATA_ERROR, error.response?.data?.message)
    }

    return Promise.reject(error);
  }
);

export default request;
