import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined }  from "@ant-design/icons";
import { deleteBlogTagByIds } from "@/apis/admin/blog/tag"

type DeleteItProps = {
  refetch: any;
  record: any;
  title: string;
};

export function BlogTagDeleteIt(props: DeleteItProps) {
  const { refetch, record, title } = props;
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const result: any = await deleteBlogTagByIds([record.id]);
          if (result && result.code === 0) {
            message.success(result.message);
            refetch();
            return false;
          }

          message.error(result.message);

        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
