import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { deleteMailByIds } from "@/apis/admin/tools/mail";
import { useState } from "react";

type DeleteItProps = {
  record: any;
  title: string;
  refetch: any
};

export function DeleteIt({ record, title, refetch }: DeleteItProps) {
  const [loading, setLoading] = useState(false);
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          setLoading(true)
          const result: any = await deleteMailByIds([record.id]);
          setLoading(false);
          if (result && result?.code === 0) {
            message.success(result?.message);
            refetch?.();
            return true;
          }

          message.error(result?.message);
          return false;
        }}
      >
        <Button loading={loading} type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
