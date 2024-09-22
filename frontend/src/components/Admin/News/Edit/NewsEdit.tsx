import { DrawerForm } from "@ant-design/pro-components";
import { NewsEditItem } from "./NewsEditItem";

type NewsEditDrawerProps = {
  trigger: any;
  onFinish: any;
  newsCategory: any[]
}

export function NewsEditDrawer(props: NewsEditDrawerProps) {
  return (
    <DrawerForm
      title="创建新闻"
      trigger={props.trigger}
      onFinish={async (values) => {
        props.onFinish(values);
      }}
    >
      <NewsEditItem newsCategory={props.newsCategory || []} />
    </DrawerForm>
  );
}
