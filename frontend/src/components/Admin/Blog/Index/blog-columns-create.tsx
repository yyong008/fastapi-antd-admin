import { Space, Tag } from "antd";

import { ButtonLink } from "@/components/common/button-link";
import { DeleteIt } from "@/components/common/delete-it";
import { FormatTime } from "@/components/common/format-time";
import { Link } from "@tanstack/react-router";

// import { removeHtmlTag } from "@/utils/utils";

export const blogColumnsCreate = (info: any) => [
  {
    dataIndex: "title",
    title: "文章标题",
    renderText(text: string, record: any) {
      return <Link to={`/blog/${record.id}`}>{text}</Link>;
    },
  },
  {
    dataIndex: "description",
    title: "文章描述",
  },
  // {
  //   dataIndex: "content",
  //   title: "文章",
  //   renderText(text: string) {
  //     return <div>{removeHtmlTag(text ?? "").slice(0, 50)}</div>;
  //   },
  // },
  {
    dataIndex: "author",
    title: "作者",
  },
  {
    dataIndex: "source",
    title: "来源",
  },
  {
    dataIndex: "view_count",
    title: "查看数",
  },
  {
    dataIndex: "published_at",
    title: "发布时间",
    renderText(text: string) {
      return <FormatTime timeStr={text} />;
    },
  },
  // {
  //   dataIndex: "categories",
  //   title: "分类",
  //   renderText() {
  //     return <Tag>{info.categoryName}</Tag>;
  //   },
  // },
  {
    dataIndex: "tags",
    title: "标签",
    renderText(_: string, record: any) {
      return <Tag>{record?.tags?.name}</Tag>;
    },
  },
  {
    dataIndex: "op",
    title: "操作",
    render(_: string, record: any) {
      return (
        <Space>
          <ButtonLink to={`/admin/blog/edit/${record.id}`} type={"edit"} />
          <DeleteIt fetcher={() => {}} record={record} title={""} />
        </Space>
      );
    },
  },
];
