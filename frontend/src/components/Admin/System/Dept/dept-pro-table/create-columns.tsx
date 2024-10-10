import { Button, Space } from "antd";

import { DeleteIt } from "../delete-it";
import { EditOutlined } from "@ant-design/icons";
import { UpdateDeptModal } from "../update-dept-modal";
import { formatDate } from "@/utils/utils";

export const createColumns = ({ refetch, options }) => [
  {
    dataIndex: "name",
    title: "用户名",
  },
  {
    dataIndex: "description",
    title: "描述",
  },
  {
    dataIndex: "parent_department_id",
    title: "父 ID",
  },
  {
    dataIndex: "sorter",
    title: "序号",
  },
  {
    dataIndex: "created_at",
    title: "创建时间",
    render(_: any, record: any) {
      return <div>{record.created_at ? formatDate(record.created_at) : "-"}</div>;
    },
  },
  {
    dataIndex: "updated_at",
    title: "更新时间",
    render(_: any, record: any) {
      return <div>{record.updated_at ? formatDate(record.updated_at) : "-"}</div>;
    },
  },
  {
    dataIndex: "op",
    title: "操作",
    render(_: any, record: any) {
      return (
        <Space>
          <UpdateDeptModal
            refetch={refetch}
            record={record}
            key="dept-modal"
            options={options}
            trigger={<Button type="link" icon={<EditOutlined />} />}
          />
          <DeleteIt
            refetch={refetch}
            title="确定要删除此部门吗?"
            record={record}
          />
        </Space>
      );
    },
  },
];
