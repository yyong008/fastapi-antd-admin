import * as ic from "@ant-design/icons";

import { BlogCategoryDeleteIt } from "./blog-category-delete-it";
import BlogCategoryModalUpdate from "./blog-category-modal-update";
import { Link } from "@tanstack/react-router";
import { Space } from "antd";

const { SwitcherOutlined } = ic;

export const blogCategoryColumnsCreate = (refetch: any) => [
  {
    dataIndex: "name",
    title: "分类名字",
    renderText(_: any, record: any) {
      return (
        <Link to={`/admin/blog?category=${record.id}`}>
          <Space>
            <SwitcherOutlined />
            <span>{record.name}</span>
          </Space>
        </Link>
      );
    },
  },
  {
    dataIndex: "description",
    title: "标签内容",
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
          <BlogCategoryModalUpdate record={record} refetch={refetch} />
          <BlogCategoryDeleteIt record={record} refetch={refetch} />
        </Space>
      );
    },
  },
];
