import { Space, Tag } from "antd";

import { DeleteIt } from "../delete-it";
import { Link } from "@tanstack/react-router";
import { LinkModalUpdate } from "../link-modal-update";
import LinkSvg from "../link-svg";

export const createLinkCategoryDetailColumns = ({ refetch }) => [
  {
    dataIndex: "name",
    title: "链接名",
  },
  {
    dataIndex: "url",
    title: "链接地址",
    renderText(_, record: any) {
      return (
        <Link to={record.url} target="_blank">
          <Tag className="inline-flex" color="cyan">
            {record.url}
            <LinkSvg className="border-yellow-200 w-[16px]" />
          </Tag>
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
    render(_, record) {
      return (
        <Space>
          <LinkModalUpdate
            refetch={refetch}
            record={record}
            key="modify-linkfr-modal"
          />
          <DeleteIt refetch={refetch} record={record} key="delete-linkfr" />
        </Space>
      );
    },
  },
];
