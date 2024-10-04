import { Button, Form, Popconfirm, message } from "antd";

import  { DeleteOutlined } from "@ant-design/icons";
import { ResponseStatus } from "@/constants/status";
import { deleteMenuByIds } from "@/apis/admin/system/menu"

type DeleteItProps = {
  record: any;
  title: string;
  refetch: (...args: any[]) => void
};

export function DeleteIt(props: DeleteItProps) {
  const { refetch, record, title } = props
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const result: any = await deleteMenuByIds([record.id])
          if (result && result.code === ResponseStatus.S) {
            message.success(result.message ||"删除成功")
            refetch?.()
            return true
          }
          message.error(result.message ||"删除失败")
          return false
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
