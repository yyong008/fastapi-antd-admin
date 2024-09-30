import { Space, Tag } from "antd";

import { DeleteIt } from "../delete-it";
import { Link } from "@tanstack/react-router";
import { LinkCategoryModalUpdate } from "../link-category-modal-update";

function LinkTag({ record }: any) {
  return (
    <Link to={`/admin/profile/link/category/${record?.id}`}>
      <Tag color="blue">{record?.name}</Tag>
    </Link>
  );
}

export const createProfileLinkCategories = ({ refetch }) => [
  {
    dataIndex: "name",
    title: "链接分类名",
    render(_, record) {
      return <LinkTag record={record} />;
    },
  },
  {
    dataIndex: "description",
    title: "描述",
  },
  {
    dataIndex: "op",
    title: "操作",
    render(_, record) {
      return (
        <Space>
          <LinkCategoryModalUpdate
            key="link-category-modal-modify"
            record={record}
            refetch={refetch}
          />
          <DeleteIt record={record} refetch={refetch} title="删除" />
        </Space>
      );
    },
  },
];
