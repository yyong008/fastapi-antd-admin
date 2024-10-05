import { DeleteIt } from "@/components/common/delete-it";
import { Link } from "@tanstack/react-router";
import { Space } from "antd";
import { StatusType } from "@/components/common/status-type";
import { UpdateRoleModal } from "../update-role-modal";

export const createColumns = ({ menus, menuRoles }: any) => [
  {
    title: "角色名",
    dataIndex: "name",
  },
  {
    title: "角色值",
    dataIndex: "value",
  },
  {
    title: "角色描述",
    dataIndex: "description",
  },
  {
    dataIndex: "status",
    title: "状态",
    width: 100,
    ellipsis: true,
    render(_: any, record: any) {
      return <StatusType status={record.status} />;
    },
  },
  {
    title: "查看该权限用户",
    width: 200,
    ellipsis: true,
    render(_: any, record: any) {
      return <Link to={`/admin/system/user?role=${record.id}`}>查看</Link>;
    },
  },
  {
    title: "操作",
    render(_: any, record: any) {
      return (
        <Space>
          <UpdateRoleModal
            record={record}
            key="create-role-modal"
            menu={menus}
            menuRoles={menuRoles}
          />
          <DeleteIt
            title="确定要删除次角色吗？"
            fetcher={() => {}}
            record={record}
          />
        </Space>
      );
    },
  },
];
