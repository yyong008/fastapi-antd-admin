import { Button, Form, message } from "antd";
import { useEffect, useState } from "react";

import { EditOutlined } from "@ant-design/icons";
import { MenuModalFormItems } from "./menu-modal-form-items";
import { ModalForm } from "@ant-design/pro-components";
import { ResponseStatus } from "@/constants/status";
import { createMenu } from "@/apis/admin/system/menu";

type MenuModalProps = {
  trigger?: () => void;
  record?: any;
  menuNotPerm?: any[];
  refetch: (...args: any[]) => void;
};

export default function MenuModal(props: MenuModalProps) {
  const { trigger, menuNotPerm, refetch } = props;
  const [form] = Form.useForm();

  const [innerMenuNotPerm, setInnerMenuNotPerm] = useState<any>();

  useEffect(() => {
    const n = [
      {
        name: "根目录",
        key: "root",
        id: -1,
        children: menuNotPerm,
      },
    ];

    setInnerMenuNotPerm([...n]);
  }, [menuNotPerm]);
  return (
    <ModalForm
      layout="horizontal"
      labelCol={{ span: 3 }}
      key={Date.now()}
      preserve={false}
      title={"创建菜单"}
      onOpenChange={(c) => {
        if (!c) {
          return;
        }
      }}
      trigger={
        trigger ??
        ((
          <Button type={"primary"} icon={<EditOutlined />}>
            {"新建菜单"}
          </Button>
        ) as any)
      }
      form={form}
      autoFocusFirstInput
      modalProps={{
        destroyOnClose: true,
        onCancel: () => form.resetFields(),
      }}
      submitTimeout={2000}
      onFinish={async (values: any) => {
        const result: any = await createMenu(values);
        if (result && result.code === ResponseStatus.S) {
          message.success(result?.message || "创建成功");
          form.resetFields();
          refetch?.()
          return true;
        }
        message.error(result?.message || "创建失败");
        return true;
      }}
    >
      <MenuModalFormItems innerMenuNotPerm={innerMenuNotPerm} />
    </ModalForm>
  );
}
