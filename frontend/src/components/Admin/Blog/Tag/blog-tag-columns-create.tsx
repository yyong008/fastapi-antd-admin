import { BlogTagDeleteIt } from "./blog-tag-delete-it";
import { BlogTagModalUpdate } from "./blog-tag-modal-update";
import { Link } from "@tanstack/react-router";
import { Space } from "antd";
import { TagOutlined } from "@ant-design/icons";

export const blogTagColumnsCreate = (refetch: any) => [
  {
    dataIndex: "name",
    title: "标签名字",
    renderText(_: any, record: any) {
      return (
        <Link to={`/admin/blog?tag=${record.id}`}>
          <Space>
            <TagOutlined />
            <span>{record.name}</span>
          </Space>
        </Link>
      );
    },
  },
  {
    dataIndex: "description",
    title: "描述",
  },
  {
    dataIndex: "op",
    title: "操作",
    render(_: any, record: any) {
      return (
        <Space>
          <BlogTagModalUpdate record={record} refetch={refetch} />
          <BlogTagDeleteIt refetch={refetch} record={record} title={""} />
        </Space>
      );
    },
  },
];
