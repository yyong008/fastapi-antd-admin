import { Space, Tag } from "antd";

import { FormatTime } from "@/components/common/format-time";
import { Link } from "@tanstack/react-router";
import { NewsCategoryModalUpdate } from "./NewsCategoryModalUpdate";
import { NewsCategoryPopconfirmDelete } from "./NewsCategoryPopconfirmDelete";

export const createNewsCategoryColumns = ({ refetch }) => [
  {
    dataIndex: "name",
    title: "新闻分类名",
    render(_, record: any) {
      return (
        <Link to={`/admin/news/category/${record.id}`}>
          <Tag color="blue">{record.name}</Tag>
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
    render(_, record: any) {
      return <FormatTime timeStr={record.created_at} />;
    }
  },
   {
    dataIndex: "updatd_at",
    title: "更新时间",
    render(_, record: any) {
      return <FormatTime timeStr={record.updated_at} />;
    }
  },
  {
    dataIndex: "op",
    title: "操作",
    render(_, record) {
      return (
        <Space>
          <NewsCategoryModalUpdate
            key="news-category-modal-modify"
            record={record}
            refetch={refetch as any}
          />
          <NewsCategoryPopconfirmDelete record={record} refetch={refetch} />
        </Space>
      );
    },
  },
];
