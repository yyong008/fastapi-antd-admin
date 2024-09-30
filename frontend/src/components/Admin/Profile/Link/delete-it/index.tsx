import { Button, Form, Popconfirm, message } from "antd";

import{ DeleteOutlined }  from "@ant-design/icons";
import { deleteProfileLinkCategoryByIds } from "@/apis/admin/profile/link/category"

type DeleteItProps = {
  refetch: any;
  record: any;
  title: string;
};

export function DeleteIt(props: DeleteItProps) {
  const { record, title, refetch } = props
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const result: any = await deleteProfileLinkCategoryByIds([record.id]);
          if (result && result?.code === 0) {
            message.success(result?.message);
            refetch();
            return false;
          }
          message.error(result?.message);

          return true;
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
