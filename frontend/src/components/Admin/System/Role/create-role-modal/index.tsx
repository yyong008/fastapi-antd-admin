import { Button, Form, message } from "antd";

import { EditOutlined } from "@ant-design/icons";
import { FormItems } from "./form-items.tsx";
import { ModalForm } from "@ant-design/pro-components";
import { ResponseStatus } from "@/constants/status.ts";
import { createRole }  from "@/apis/admin/system/role"
import { useState } from "react";

type CreateRoleModalProps = {
  trigger?: React.ReactNode;
  menu: any[];
  refetch: (...args: any[]) => void;
};

export function CreateRoleModal(props: CreateRoleModalProps) {
  const { trigger, menu } = props;
  const [form] = Form.useForm();
  const [checkedKeys, setCheckedKeys] = useState<any[]>([]);

  const onCheck = (checkedKeys: any) => {
    setCheckedKeys(checkedKeys);
  };

  return (
    <ModalForm
      title="创建角色"
      trigger={
        trigger ??
        ((
          <Button
            type={"primary"}
            icon={<EditOutlined />}
          >
            {"新建"}
          </Button>
        ) as any)
      }
      form={form}
      autoFocusFirstInput
      onOpenChange={() => {
          form.resetFields()
      }}
      modalProps={{
        destroyOnClose: true,
        onCancel: () => console.log(""),
      }}
      submitTimeout={2000}
      onFinish={async (vals) => {
        if(vals.menus) {
          vals.menus = vals.menus.map((m: any) => m.id)
        }
        const result: any = await createRole(vals);
        if(result && result.code === ResponseStatus.S) {
          message.success(result?.message || "创建成功");
          props.refetch();
          return true
        }

        message.error(result?.message || "创建失败");
        return false
      }}
    >
      <FormItems menu={menu} checkedKeys={checkedKeys} onCheck={onCheck} />
    </ModalForm>
  );
}
