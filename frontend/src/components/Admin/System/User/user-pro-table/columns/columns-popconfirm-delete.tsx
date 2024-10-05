import { Button, Popconfirm, message } from "antd";

import { DeleteOutlined } from "@ant-design/icons";
import { ResponseStatus } from "@/constants/status";
import { deleteUserByIds } from "@/apis/admin/system/user";

export function ColumnsPopConfirmDelete({ record, reload }: any) {
  return (
    <Popconfirm
      key="del"
      title="Are your sure?"
      onConfirm={async () => {
        const ids = [record.id];
        const result: any = await deleteUserByIds(ids);
        if (result && result?.code === ResponseStatus.S) {
          message.success(result?.message);
          reload?.();
          return true;
        }
        message.error(result?.message);
        return false;
      }}
    >
      <Button danger type="link" icon={<DeleteOutlined />}></Button>
    </Popconfirm>
  );
}
