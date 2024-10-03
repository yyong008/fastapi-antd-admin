import { Button, Form, message } from "antd";

import { EditOutlined } from "@ant-design/icons";
import { ModalForm } from "@ant-design/pro-components";
import { ModalFormItems } from "./modal-form-items";
import { ResponseStatus } from "@/constants/status";
import { updateDict } from "@/apis/admin/system/dict"

export function UpdateDictModal({ refetch, trigger, record }: any) {
  const [form] = Form.useForm<{ name: string; company: string }>();

  return (
    <ModalForm
      title="修改字典"
      trigger={
        trigger ?? (
          <Button type="link">
            <EditOutlined />
          </Button>
        )
      }
      onOpenChange={(c) => {
        if (!c) {
          return;
        }
        form.setFieldsValue({
          key: record.name,
          value: record.code,
          ...record,
        });
      }}
      form={form}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => console.log(""),
      }}
      submitTimeout={2000}
      onFinish={async (values) => {
        const result: any = await updateDict(record.id, values);
        if (result && result.code === ResponseStatus.S) {
          message.success(result?.message || "创建成功");
          form.resetFields();
          refetch?.()
          return true;
        }
        message.error(result.message || "创建失败");
        return false;
      }}
    >
      <ModalFormItems />
    </ModalForm>
  );
}
