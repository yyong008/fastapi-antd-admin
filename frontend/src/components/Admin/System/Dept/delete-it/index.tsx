import { Button, Form, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { ResponseStatus } from "@/constants/status";
import { deleteDeptByIds } from "@/apis/admin/system/dept"

type DeleteItProps = {
  refetch: any
  record: any;
  title: string;
};

export function DeleteIt(props: DeleteItProps) {
  const { record, title, refetch } = props;

  return (
    <Form>
      <Popconfirm
        title={title || "确定要删除吗?"}
        onConfirm={async () => {
          const result: any = await deleteDeptByIds([record.id]);
          if(result && result.code === ResponseStatus.S){
            message.success(result?.message || "删除成功");
            refetch?.()
            return true
          }
          message.error(result?.message || "删除失败");
          return false
        }}
      >
        <Button type="link" danger icon={<DeleteOutlined />} />
      </Popconfirm>
    </Form>
  );
}
