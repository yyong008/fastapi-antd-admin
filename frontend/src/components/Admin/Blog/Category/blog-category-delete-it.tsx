import * as ic from "@ant-design/icons";

import { Button, Form, Popconfirm, message } from "antd";

const { DeleteOutlined } = ic;

type DeleteItProps = {
  record: any;
  title?: string;
  refetch: any;
};

export function BlogCategoryDeleteIt({
  record,
  title,
  refetch,
}: DeleteItProps) {
  const [deleteBlog] = [(...args: any) => args]
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const data = { ids: [record.id] };

          const result: any = await deleteBlog(data);

          if (result.data.code === 1) {
            message.error(result.data.message);
            return false;
          }

          message.success(result.data.message);
          refetch();
          return false;
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
