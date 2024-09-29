import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { deleteBlogCategoryByIds } from "@/apis/admin/blog/category";

type DeleteItProps = {
  record: any;
  title?: string;
  refetch: any;
};

export function BlogCategoryDeleteIt(props: DeleteItProps) {
  const { record, title, refetch } = props;
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const result: any = await deleteBlogCategoryByIds([record.id]);

          if (result && result.code === 0) {
            message.success(result.message);
            refetch();
            return true;
          }
          message.error(result.message);
          return false;
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
