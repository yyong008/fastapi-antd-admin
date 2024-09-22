import { Button, Result } from "antd";
import {
  createFileRoute,
  useNavigate,
  useRouterState,
} from "@tanstack/react-router";

import confetti from "canvas-confetti";
import { useEffect } from "react";

export const Route = createFileRoute("/admin/news/result")({
  component: ResultRoute,
});

export function ResultRoute() {
  const state = useRouterState();

  const nav = useNavigate();
  useEffect(() => {
    setTimeout(() => {
      confetti({
      particleCount: 100,
      spread: 70,
      origin: { y: 0.6 },
    });
    }, 300)
  }, []);
  return (
    <Result
      title={`新闻创建成功`}
      subTitle={`《${(state.location.state as any)?.title}》`}
      extra={[
        <Button
          type="primary"
          key="console"
          onClick={() => {
            const id = (state.location.state as any)?.id;
            if (id) {
              nav({ to: `/news/${id}` });
            }
          }}
        >
          查看新闻
        </Button>,
        <Button
          key="buy"
          onClick={() => {
            nav({ to: `/admin/news/edit` });
          }}
        >
          再次创建新闻
        </Button>,
      ]}
    />
  );
}
