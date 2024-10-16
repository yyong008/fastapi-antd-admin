import { Space, Tag } from "antd";

import ChangeLogUpdateModal from "../ChangeLogModalUpdate";
import { DeleteIt } from "../delete-it";
import { FormatTime } from "@/components/common/format-time";

const typeMap = {
  1: {
    color: "blue",
    text: "重大更新",
  },
  2: {
    color: "green",
    text: "功能更新",
  },
  3: {
    color: "volcano",
    text: "Bug 修复",
  },
};

export const createChangeLogColumns = ({ refresh }) =>  [
    {
      dataIndex: "publish_version",
      title: "版本",
      render(_: any, record: any) {
        return <Tag color="green">{record.publish_version}</Tag>;
      }
    },
    {
      dataIndex: "publish_name",
      title: "发布者",
    },
    {
      dataIndex: "type",
      title: "更新类型",
      render: (_: any, record: { type: 1 | 2 | 3 }) => (
        <Tag color={typeMap?.[record.type]?.color}>
          {typeMap?.[record.type]?.text}
        </Tag>
      ),
    },
    {
      dataIndex: "content",
      title: "发布内容",
      ellipsis: true,
    },
    {
      dataIndex: "url",
      title: "跳转链接",
      ellipsis: true,
      render(_: any, record: any) {
        return <a href={record.url}>{record.url}</a>;
      },
    },
    {
      dataIndex: "publish_time",
      title: "发布时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.publish_time} />;
      },
    },
    {
      dataIndex: "created_at",
      title: "创建时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.created_at} />;
      },
    },
    {
      dataIndex: "updated_at",
      title: "更新时间",
      render(_: any, record: any) {
        return <FormatTime timeStr={record.updated_at} />;
      },
    },
    {
      dataIndex: "op",
      title: "操作",
      render(_: any, record: any) {
        return (
          <Space>
            <ChangeLogUpdateModal
              key="changelog-modal-modify"
              record={record}
              refetch={refresh}
            />
            <DeleteIt record={record} title={""} refetch={refresh} />
          </Space>
        );
      },
    },
  ];
