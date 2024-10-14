import { Space, Tag } from "antd";

import { ButtonLink } from "@/components/common/button-link";
// import { FormatTime } from "@/components/common/format-time";
import { Link } from "@tanstack/react-router";
import { NewsCategoryListPopconfirmDelete } from "./NewsCategoryListPopconfirmDelete";

export const createNewsCategoryColumns = ({ refetch, newsCategoryData }) => [
  {
    dataIndex: "title",
    title: "新闻标题",
    ellipsis: true,
    renderText(_, record: any) {
      return <Link to={`/news/${record.id}`}>{record.title}</Link>;
    },
  },
  {
    dataIndex: "description",
    title: "新闻简介",
    ellipsis: true,
    render(_, record) {
      return <div>{record.description?.slice(0, 20) ?? "-"}</div>;
    },
  },
  // {
  //   dataIndex: "content",
  //   title: "新闻内容",
  //   render(_, record) {
  //     return <div>{record.content?.slice(0, 20)}</div>;
  //   },
  // },
  {
    dataIndex: "author",
    title: "作者",
  },
  {
    dataIndex: "source",
    title: "新闻来源",
  },
  {
    dataIndex: "newsId",
    title: "新闻分类",
    render(_, record) {
      const name = newsCategoryData.list.filter((item) => item.id === record.category_id)[0]?.name;
      return <Tag color="green">{name}</Tag>;
    },
  },
  {
    dataIndex: "view_count",
    title: "查看次数",
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
    render(_, record) {
      return (
        <Space>
          <ButtonLink type="edit" to={`/admin/news/edit/${record.id}`} />
          <NewsCategoryListPopconfirmDelete
            refetch={refetch}
            record={record}
            title={""}
          />
        </Space>
      );
    },
  },
];
