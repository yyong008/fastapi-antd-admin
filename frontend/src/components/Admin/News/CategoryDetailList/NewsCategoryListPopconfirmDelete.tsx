import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { deleteNewsByIds } from "@/apis/admin/news/news";

type DeleteItProps = {
  refetch: any;
  record: any;
  title?: string;
  handleDelete?: (id: string | { ids: string[] }) => any;
};

export function NewsCategoryListPopconfirmDelete(props: DeleteItProps) {
  const { record, title, refetch } = props;
  const handleDeleteItems = ({ ids }) => {
    const result = deleteNewsByIds({ ids });
    return result;
  };
  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const result: any = await handleDeleteItems({ ids: [record.id] });
          if (result?.code !== 0) {
            message.error(result?.message);
            return false;
          }
          message.success(result?.message);
          refetch();
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
