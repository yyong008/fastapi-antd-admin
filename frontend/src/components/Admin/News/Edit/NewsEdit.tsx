import { DrawerForm } from "@ant-design/pro-components";
import { NewsEditItem } from "./NewsEditItem";

export function NewsEditDrawer(props: any) {
  return (
    <DrawerForm
      title="创建新闻"
      trigger={props.trigger}
      onFinish={async (values) => {
        props.onFinish(values);
      }}
    >
      <NewsEditItem />
    </DrawerForm>
  );
}
