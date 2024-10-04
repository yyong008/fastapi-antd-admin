import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined }from "@ant-design/icons";
import { deleteDictItemByIds } from "@/apis/admin/system/dict-item"

type DeleteItProps = {
  record: any;
  title?: string;
  refetch: (...args: any[]) => void;
};

export function DeleteIt({ record, title, refetch }: DeleteItProps) {
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const ids = [record.id];
          const result: any = await deleteDictItemByIds(ids);

          if(result && result.code === 200) {
            message.info(result.message)
            refetch?.()
            return false
          }
          message.error(result.message)
          return false
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
