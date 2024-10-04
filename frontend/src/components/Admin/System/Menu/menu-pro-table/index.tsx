import MenuModal from "../create-menu-modal";
import { ProTable } from "@ant-design/pro-components";
import { createColumns } from "./create-columns";

export type Status = {
  color: string;
  text: string;
};

export type TableListItem = {
  id: number;
  parentId: number;
  key: number;
  name: string;
  icon: string;
  containers: number;
  orderNo: number;
  path: string;
  creator: string;
  status: Status;
  createdAt: number;
  updatedAt: number;
  isLink: 0 | 1;
};

type SystemMenuProps = {
  // menu: any[];
  // roles: any[];
  menuRaw: any[];
  menuNotPerm: any[];
  loading: boolean;
  refetch: any;
};

export function MenuProTable(props: SystemMenuProps) {
  const { menuRaw = [], menuNotPerm = [], refetch } = props;
  return (
    <ProTable<TableListItem>
      size="small"
      columns={createColumns({ refetch, menuNotPerm }) as any}
      scroll={{ x: 1300 }}
      dataSource={menuRaw}
      rowKey="id"
      pagination={false}
      search={false}
      dateFormatter="string"
      loading={props.loading}
      headerTitle="菜单管理"
      options={{
        reload: props.refetch,
      }}
      rowClassName={(record) => {
        return record.parentId ? "bg-yellow-50" : "";
      }}
      toolBarRender={() => [
        <MenuModal
          key="menu-modal"
          menuNotPerm={menuNotPerm}
          refetch={refetch}
        />,
      ]}
    />
  );
}
