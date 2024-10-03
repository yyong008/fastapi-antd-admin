import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { deleteDictByIds } from "@/apis/admin/system/dict"
import { useState } from "react";

type DeleteItProps = {
  record: any;
  title?: string;
  refetch: (...args: any[]) => void;
};

export function DeleteIt({ record, title, refetch }: DeleteItProps) {
  const [loading, setLoading] = useState(false)
  return (
    <Form>
      <Popconfirm
        okButtonProps={{
          loading
        }}
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          setLoading(true)
          const result: any = await deleteDictByIds([record.id]);
          setLoading(false)

          if(result && result.code === 0) {
            message.success(result?.message || "删除成功");
            refetch?.()
            return true
          }

          message.error(result?.message || "删除成功");
          return false
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
