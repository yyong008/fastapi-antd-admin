import { Button, Form, message } from "antd";
import { useEffect, useState } from "react";

import { EditOutlined } from "@ant-design/icons";
import { MenuModalFormItems } from "./menu-modal-form-items";
import { ModalForm } from "@ant-design/pro-components";
import { ResponseStatus } from "@/constants/status";
import { updateMenuById } from "@/apis/admin/system/menu";

type MenuModalProps = {
  trigger?: () => void;
  record?: any;
  menuNotPerm?: any[];
  refetch?: () => void;
};

export default function MenuModalUpdate({
  trigger,
  record,
  menuNotPerm,
  refetch,
}: MenuModalProps) {
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
      title={record?.id ? "修改菜单" : "创建菜单"}
      onOpenChange={(c) => {
        if (!c || !record.id) {
          return;
        }
        let parentId: null | number = null;
        if (record.id && record.parent_menu_id) {
          parentId = record.parent_menu_id;
        } else if (record.parent_menu_id === null) {
          parentId = -1;
        }
        form.setFieldsValue({
          ...record,
          parentId,
          type: Number(record.type),
        });
      }}
      trigger={
        trigger ??
        ((
          <Button
            type={!record.id ? "primary" : "link"}
            icon={<EditOutlined />}
          >
            {!record.id ? "新建" : ""}
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
        const result: any = await updateMenuById(record.id, values);

        if (result && result.code === ResponseStatus.S) {
          message.success(result.message || "修改成功")
          refetch?.();
          form.resetFields();
          return true;
        }

        message.error(result.message || "修改失败");
        return false;
      }}
    >
      <MenuModalFormItems innerMenuNotPerm={innerMenuNotPerm} record={record} />
    </ModalForm>
  );
}
