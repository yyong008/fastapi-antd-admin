import { Tag } from "antd";
import { formatDate } from "@/utils/utils";

export const createColumns = () => [
  {
    dataIndex: "name",
    title: "用户名",
    ellipsis: true,
    render(_: any, record: any) {
      return <Tag color="blue">{record.name}</Tag>;
    },
  },
  {
    dataIndex: "login_at",
    title: "登录时间",
    ellipsis: true,
    render(_: any, record: any) {
      return <Tag  color="purple">{record.login_at ? formatDate(record.login_at) : "-"}</Tag>;
    },
  },
  {
    dataIndex: "ip",
    title: "ip",
    ellipsis: true,
  },
  {
    dataIndex: "address",
    title: "地址",
    ellipsis: true,
  },
  {
    dataIndex: "system",
    title: "系统",
    ellipsis: true,
  },
  {
    dataIndex: "browser",
    title: "浏览器",
    ellipsis: true,
  },

];
