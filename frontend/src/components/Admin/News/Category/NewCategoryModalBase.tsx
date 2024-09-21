import { Form, message } from "antd";

import { ModalForm } from "@ant-design/pro-components";
import { NewsCategoryModalFormItem } from "./NewsModalFormItem";

type NewCategoryModalBaseProps = {
  loading: boolean;
  refetch: () => void;
  title: string;
  onOpenChange: (open: boolean, form: any) => void;
  trigger: JSX.Element;
  submitTimeout?: number;
  onFinish: (values: any) => Promise<boolean>;
}

export function NewsCategoryModalBase({ refetch, ...props }: NewCategoryModalBaseProps) {
  const [form] = Form.useForm();
  return (
    <ModalForm
      form={form}
      loading={props.loading}
      key={Date.now()}
      preserve={false}
      title={props.title}
      onOpenChange={(c) => props.onOpenChange(c, form)}
      trigger={props.trigger}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => form.resetFields(),
      }}
      submitTimeout={props?.submitTimeout || 2000}
      onFinish={async (values: any) => {
        const result: any = await props.onFinish(values);
        if (result && result?.code !== 0) {
          message.error(result?.message);
          return false;
        }
        message.success(result?.message);
        refetch();
        form.resetFields();
        return true;
      }}
    >
      <NewsCategoryModalFormItem />
    </ModalForm>
  );
}
