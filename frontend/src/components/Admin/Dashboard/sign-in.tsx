import { CheckCircleFilled } from "@ant-design/icons";

import { Button, message } from "antd";

import confetti from "canvas-confetti";
import { useState } from "react";
import { ResponseStatus } from "@/constants/status";
import { createSignInLog } from "@/apis/admin/signin";

export function SignIn({ data: _data, refetch }: any) {
  const [data, setData] = useState(_data);
  const [loading, setLoading] = useState(false);

  const signInHanlder = async () => {
    setLoading(true);
    const result: any = await createSignInLog();
    setLoading(false);
    if (result && result.code === ResponseStatus.S) {
      setData((p) => {
        return {
        ...p,
        isSignIn: true,
      }
      });
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
      });
      refetch?.();
      return true;
    }

    message.error(result.message);
    return false;
  };
  return (
    <div>
      {!data?.isSignIn ? (
        <Button
          onClick={signInHanlder}
          htmlType="submit"
          disabled={data?.isSignIn}
          loading={loading}
        >
          签到
        </Button>
      ) : (
        <Button
          type="primary"
          icon={<CheckCircleFilled />}
          onClick={() => {
            message.success("🤖 已签到，明天再来吧");
          }}
        >
          已签到
        </Button>
      )}
    </div>
  );
}
