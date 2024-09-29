import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { deleteDocsChangelogByIds } from "@/apis/admin/docs/changelog";

type DeleteItProps = {
  refetch: any;
  record: any;
  title: string;
};

export function DeleteIt(props: DeleteItProps) {
  const { record, title, refetch } = props;
  const [form] = Form.useForm();
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const data = {
            ids: [] as number[],
          };
          if (record.id) {
            data.ids = [record.id];
          }

          const result: any = await deleteDocsChangelogByIds([record.id]);
          if (result?.code !== 0) {
            message.error(result?.message);
            return false;
          }
          message.success(result?.message);
          refetch();
          form.resetFields();
          return true;
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
