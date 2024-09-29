import { Button, Result } from "antd";
import {
  createFileRoute,
  useNavigate,
  useRouterState,
} from "@tanstack/react-router";

import confetti from "canvas-confetti";
import { useEffect } from "react";

export const Route = createFileRoute("/admin/blog/result")({
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
    }, 300);
  }, []);
  return (
    <Result
      title={`博客创建成功`}
      subTitle={`《${(state.location.state as any)?.title}》`}
      extra={[
        <Button
          type="primary"
          key="console"
          onClick={() => {
            const id = (state.location.state as any)?.id;
            if (id) {
              nav({ to: `/blog/${id}` });
            }
          }}
        >
          查看博客
        </Button>,
        <Button
          key="buy"
          onClick={() => {
            nav({ to: `/admin/blog/edit` });
          }}
        >
          再次创建博客
        </Button>,
      ]}
    />
  );
}
