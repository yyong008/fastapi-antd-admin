import { Button, Form, message } from "antd";

import { EditOutlined } from "@ant-design/icons";
import { ModalForm } from "@ant-design/pro-components";
import { ModalFormItems } from "./modal-form-items";
import { createDict } from "@/apis/admin/system/dict"

type DictModalCreateProps = {
  trigger?: JSX.Element;
  refetch: (...args: any[]) => void;
}

export function DictModalCreate({ trigger, refetch }: DictModalCreateProps) {
  const [form] = Form.useForm();
  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title={"创建字典"}
      onOpenChange={(c) => {
        if (!c) {
          return;
        }
      }}
      trigger={
        trigger ?? (
          <Button
            type={"primary"}
            icon={<EditOutlined />}
          >
            新建字典
          </Button>
        )
      }
      form={form}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => form.resetFields(),
      }}
      submitTimeout={2000}
      onFinish={async (values: any) => {
        const result: any = await createDict(values);
        if (result && result.code === 0) {
          message.success(result?.message || "创建成功");
          form.resetFields();
          refetch?.();
          return true;
        }
        message.error(result?.message || "创建失败");
        return false;
      }}
    >
      <ModalFormItems />
    </ModalForm>
  );
}
