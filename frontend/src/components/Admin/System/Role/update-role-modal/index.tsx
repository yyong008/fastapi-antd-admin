import { Button, Form, message } from "antd";
import { useEffect, useMemo, useState } from "react";

import { EditOutlined } from "@ant-design/icons";
import { FormItems } from "./form-items.tsx";
import { ModalForm } from "@ant-design/pro-components";
import { ResponseStatus } from "@/constants/status.ts";
import { updateRoleById } from "@/apis/admin/system/role";

type UpdateRoleModalProps = {
  trigger?: React.ReactNode;
  record: any;
  menu: any[];
  refetch: (...args: any[]) => void;
};

export function UpdateRoleModal(props: UpdateRoleModalProps) {
  const { trigger, record, menu } = props;
  console.log(props);
  const [form] = Form.useForm();
  const [checkedKeys, setCheckedKeys] = useState<any[]>([]);

  const onCheck = (checkedKeys: any) => {
    setCheckedKeys(checkedKeys);
  };

  const initCheckKeys = useMemo(() => {
    if (record.id) {
      return record.menus?.map((r) => r.id);
    } else {
      return [];
    }
  }, [record]);

  useEffect(() => {
    if (record.id) {
      setCheckedKeys(initCheckKeys);
    }
  }, [initCheckKeys, record.id]);

  return (
    <ModalForm
      title="创建角色"
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
      onOpenChange={(e) => {
        if (e) {
          form.setFieldsValue({
            ...record,
            menus: record.menus?.map((r) => ({
              id: r.id,
              key: r.id,
              value: r.id,
            })),
          });
          if (record.id) {
            const keys: any[] = record.menus?.map((r) => r.id);
            setCheckedKeys(keys);
          }
        }
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
        const result: any = await updateRoleById(record.id, vals);
        if (result && result.code === ResponseStatus.S) {
          message.success("更新成功");
          props.refetch?.();
          return true;
        }
        message.error("更新失败");
        return false;
      }}
    >
      <FormItems menu={menu} checkedKeys={checkedKeys} onCheck={onCheck} />
    </ModalForm>
  );
}
