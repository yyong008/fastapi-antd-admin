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
    dataIndex: "created_at",
    title: "创建时间",
    ellipsis: true,
    // render(_, record) {
    //   return <div><FormatTime timeStr={record.created_at} /></div>
    // },
  },
  {
    dataIndex: "updated_at",
    title: "创建时间",
    ellipsis: true,
    // render(_, record) {
    //   return <FormatTime timeStr={record.updated_at} />;
    // },
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
