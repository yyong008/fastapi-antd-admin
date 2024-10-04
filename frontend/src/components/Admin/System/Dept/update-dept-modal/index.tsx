import { Button, Form, message } from "antd";

import { EditOutlined } from "@ant-design/icons";
import { ModalForm } from "@ant-design/pro-components";
import { ModalFormItems } from "./modal-form-items";
import { ResponseStatus } from "@/constants/status";
import { updateDept } from "@/apis/admin/system/dept"

export function UpdateDeptModal({ options, trigger, record, refetch }: any) {
  const [form] = Form.useForm();
  return (
    <ModalForm
      key={Date.now()}
      preserve={false}
      title={"修改部门"}
      onOpenChange={(c) => {
        if (!c || !record.id) {
          return;
        }
        form.setFieldsValue({
          ...record,
        });
      }}
      trigger={
        trigger ?? (
          <Button type={record ? "primary" : "link"} icon={<EditOutlined />}>
            {record ? "新建" : ""}
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
        const result: any = await updateDept(record.id, values)
        if (result && result?.code === ResponseStatus.S) {
          message.success(result?.message || "修改成功")
          refetch()
          form.resetFields()
          return true
        }
        message.error(result?.message || "修改失败")
        return false;
      }}
    >
      <ModalFormItems options={options}/>
    </ModalForm>
  );
}
