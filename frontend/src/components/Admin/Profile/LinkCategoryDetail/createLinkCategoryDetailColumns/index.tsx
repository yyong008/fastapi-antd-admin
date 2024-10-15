import { Space, Tag } from "antd";

import { DeleteIt } from "../delete-it";
import { Link } from "@tanstack/react-router";
import { LinkModalUpdate } from "../link-modal-update";
import LinkSvg from "../link-svg";
import { ProColumnType } from "@ant-design/pro-components"

export const createLinkCategoryDetailColumns = ({ refetch }) => [
  {
    dataIndex: "name",
    title: "链接名",
    width: 100,
    ellipsis: true
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
    width: 100,
    ellipsis: true
  },
  {
    dataIndex: "created_at",
    title: "创建时间",
    ellipsis: true,
     width: 100,
  },
  {
    dataIndex: "updated_at",
    title: "更新时间",
    ellepsis: true,
     width: 100,
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
] as ProColumnType[] as any;
