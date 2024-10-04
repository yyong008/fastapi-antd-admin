import { Button, Form } from "antd";

import { EditOutlined } from "@ant-design/icons";
import { ModalForm } from "@ant-design/pro-components";
import { ModalFormItems } from "./modal-form-items";
import { ResponseStatus } from "@/constants/status";
import { createDictItem } from "@/apis/admin/system/dict-item"

type DictItemModalCreateProps = {
  trigger?: any;
  refetch: (...args: any[]) => void;
  dictId: number
}

export function DictItemModalCreate(props: DictItemModalCreateProps) {
  const { trigger, refetch, dictId } = props;
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
        form.resetFields();
      }}
      trigger={
        trigger ?? (
          <Button
            type={"primary"}
            icon={<EditOutlined />}
          >
            新建
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
        const result: any = await createDictItem({...values, dictionary_id: dictId });
        if(result && result.code === ResponseStatus.S) {
          form.resetFields();
          refetch?.();
          return true;
        }
        form.resetFields();
        return false;
      }}
    >
      <ModalFormItems />
    </ModalForm>
  );
}
