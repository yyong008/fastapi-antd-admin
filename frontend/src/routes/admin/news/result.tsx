import { Button, Result } from "antd";
import { createFileRoute, useLocation, useNavigate, useRouter } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/news/result')({
  component: () => <div>Hello /admin/news/result!</div>
})


export function ResultRoute() {
  const router = useRouter()
  const state = useLocation().state as any;
  const nav = useNavigate();
  if (!state || !state?.title) {
    return router.history.go(-1);
  }
  return (
    <Result
      status="success"
      title="新闻创建成功"
      subTitle={state?.title}
      extra={[
        <Button
          type="primary"
          key="console"
          onClick={() => {
            nav({ to: `/news/${state.id}`});
          }}
        >
          Go Read
        </Button>,
        <Button
          key="buy"
          onClick={() => {
            nav({ to: `/admin/news/edit`});
          }}
        >
          To Create News Again
        </Button>,
      ]}
    />
  );
}
