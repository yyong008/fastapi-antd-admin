import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { ResponseStatus } from "@/constants/status";
import { deleteRoleByIds } from "@/apis/admin/system/role"

type DeleteItProps = {
  refetch: (...args: any[]) => void;
  record: any;
  title: string;
};

export function DeleteIt({ refetch, record, title }: DeleteItProps) {
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const res: any = await deleteRoleByIds([record.id]);
          if(res && res.code === ResponseStatus.S) {
            message.success(res?.message || "删除成功");
            refetch?.();
            return true
          }

          message.error(res?.message || "删除失败");
          return false
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
