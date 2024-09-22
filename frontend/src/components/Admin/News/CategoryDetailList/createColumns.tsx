import { ButtonLink } from "@/components/common/button-link";
import { Link } from "@tanstack/react-router";
import { NewsCategoryListPopconfirmDelete } from "./NewsCategoryListPopconfirmDelete";
import { Space } from "antd";

export const createNewsCategoryColumns = ({ refetch }) => [
  {
    dataIndex: "title",
    title: "新闻标题",
    renderText(_, record: any) {
      return <Link to={`/news/${record.id}`}>{record.title}</Link>;
    },
  },
  {
    dataIndex: "content",
    title: "新闻内容",
    render(_, record) {
      return <div>{record.content?.slice(0, 20)}</div>;
    },
  },
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
  },
  {
    dataIndex: "viewCount",
    title: "查看次数",
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
