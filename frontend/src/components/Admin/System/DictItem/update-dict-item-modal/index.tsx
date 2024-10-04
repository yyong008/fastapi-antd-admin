import { Button, Form } from "antd";

import { EditOutlined } from "@ant-design/icons";
import { ModalForm } from "@ant-design/pro-components";
import { ModalFormItems } from "./modal-form-items";
import { ResponseStatus } from "@/constants/status";
import { updateDictItemById } from "@/apis/admin/system/dict-item";

type DictItemModalUpdateProps = {
  trigger?: any;
  refetch: (...args: any[]) => void;
  record: any;
  dictId: number;
};

export function DictItemModalUpdate(props: DictItemModalUpdateProps) {
  const { trigger, refetch, record, dictId } = props;
  const [form] = Form.useForm();
  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title={"修改字典"}
      onOpenChange={(c) => {
        if (!c) {
          return;
        }
        form.setFieldsValue({
          ...props.record,
        });
      }}
      trigger={
        trigger ?? <Button type={"link"} icon={<EditOutlined />}></Button>
      }
      form={form}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => form.resetFields(),
      }}
      submitTimeout={2000}
      onFinish={async (values: any) => {
        const result: any = await updateDictItemById(record.id, {
          ...values,
          dictionary_id: dictId,
        });
        if (result && result.code === ResponseStatus.S) {
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
