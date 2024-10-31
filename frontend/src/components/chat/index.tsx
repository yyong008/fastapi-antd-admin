import { Drawer, FloatButton } from "antd";
import { useEffect, useRef, useState } from "react";

import { OpenAIOutlined } from "@ant-design/icons";
import { ProChat } from "@ant-design/pro-chat";
import { genResponseStream } from "@/utils/stream";
import { getResponse } from "@/apis/chat";
import { useTheme } from "antd-style";

export const AdminChat = () => {
  const theme = useTheme();

  const [open, setOpen] = useState(false);

  const showDrawer = () => {
    setOpen(true);
  };

  const onClose = () => {
    setOpen(false);
  };

  const chatIdRef = useRef(null);
  const firstChatCompleted = async () => {};

  useEffect(() => {
    return () => {
      chatIdRef.current = null;
    };
  }, []);

  return (
    <>
      <FloatButton
        icon={<OpenAIOutlined />}
        type="primary"
        onClick={showDrawer}
      />
      <Drawer
        title="FastAPI Antd Admin 助理"
        onClose={onClose}
        open={open}
        styles={{
          body: {
            padding: 0,
          },
        }}
      >
        <ProChat
          style={{ background: theme.colorBgLayout }}
          request={async (chats) => {
            const messages = chats.map((chat) => ({
              id: chatIdRef.current || "",
              role: chat.role,
              content: chat.content,
            }));
            const response = await getResponse({ messages });
            return new Response(
              genResponseStream(response.clone(), chatIdRef, firstChatCompleted)
            );
          }}
        />
      </Drawer>
    </>
  );
};
